# ==============================================================================
# ARC Framework: Generate All Figures (PowerShell)
# ==============================================================================
# This script generates all figures from the paper.
# Prerequisites: Python 3.8+, R 4.0+, required packages installed
# Usage: .\generate_all_figures.ps1
# ==============================================================================

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "ARC Framework: Generating All Figures" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""

# Store starting directory
$START_DIR = Get-Location

# Check if we're in the repository root
if (-not (Test-Path "code") -or -not (Test-Path "data") -or -not (Test-Path "figures")) {
    Write-Host "ERROR: Please run this script from the repository root directory." -ForegroundColor Red
    Write-Host "Expected directory structure:"
    Write-Host "  - code/"
    Write-Host "  - data/"
    Write-Host "  - figures/"
    exit 1
}

# Check Python installation
Write-Host "Checking Python installation..."
try {
    $pythonVersion = (python --version 2>&1).ToString()
    Write-Host "  ✓ $pythonVersion found" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Python is not installed or not in PATH." -ForegroundColor Red
    exit 1
}

# Check required Python packages
Write-Host "Checking Python packages..."
$packagesOk = $true
try {
    python -c "import matplotlib, pandas, numpy" 2>$null
    if ($LASTEXITCODE -ne 0) {
        $packagesOk = $false
    }
} catch {
    $packagesOk = $false
}

if (-not $packagesOk) {
    Write-Host "ERROR: Required Python packages not installed." -ForegroundColor Red
    Write-Host "Please run: pip install -r requirements.txt"
    exit 1
}
Write-Host "  ✓ matplotlib, pandas, numpy found" -ForegroundColor Green

# Check R installation (optional, only needed for Figure 7)
$R_INSTALLED = $false
try {
    $rVersion = (Rscript --version 2>&1 | Select-String -Pattern "version").ToString()
    Write-Host "  ✓ R found" -ForegroundColor Green
    $R_INSTALLED = $true
    
    # Check metafor package
    Rscript -e "library(metafor)" 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  ⚠ R package 'metafor' not installed. Figure 7 will be skipped." -ForegroundColor Yellow
        Write-Host "    To install: Rscript -e `"install.packages('metafor')`""
        $R_INSTALLED = $false
    } else {
        Write-Host "  ✓ R package 'metafor' found" -ForegroundColor Green
    }
} catch {
    Write-Host "  ⚠ R not found. Figure 7 will be skipped." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "Generating Python Figures (2, 3, 4, 5, 6)" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""

# Array of Python scripts
$PYTHON_SCRIPTS = @(
    "Generate_Figure2_Taxonomy.py",
    "Generate_Figure3_CostEffectiveness.py",
    "Generate_Figure4_HRC.py",
    "Generate_Figure5_Sensitivity.py",
    "Generate_Figure6_Competency.py"
)

# Generate Python figures
$PYTHON_SUCCESS = 0
foreach ($script in $PYTHON_SCRIPTS) {
    Write-Host "Running: $script" -ForegroundColor White
    Set-Location "$START_DIR\code\python"
    python $script
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✓ Success" -ForegroundColor Green
        $PYTHON_SUCCESS++
    } else {
        Write-Host "  ✗ Failed" -ForegroundColor Red
    }
    Write-Host ""
    Set-Location $START_DIR
}

Write-Host ""
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "Generating R Figure (7)" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""

# Generate R figure if R is available
$R_SUCCESS = 0
if ($R_INSTALLED) {
    Write-Host "Running: Paper_Figure_7.R" -ForegroundColor White
    Set-Location "$START_DIR\code\r"
    Rscript Paper_Figure_7.R
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✓ Success" -ForegroundColor Green
        $R_SUCCESS = 1
    } else {
        Write-Host "  ✗ Failed" -ForegroundColor Red
    }
    Write-Host ""
    Set-Location $START_DIR
} else {
    Write-Host "Skipping Figure 7 (R not available)" -ForegroundColor Yellow
    Write-Host ""
}

Write-Host ""
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "Summary" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Python figures generated: $PYTHON_SUCCESS / $($PYTHON_SCRIPTS.Count)"
if ($R_INSTALLED) {
    Write-Host "R figures generated: $R_SUCCESS / 1"
}
Write-Host ""
Write-Host "Generated figures are in: figures\"
Write-Host ""

# List generated figures
Write-Host "Files in figures\ directory:"
Get-ChildItem "figures\*.png" -ErrorAction SilentlyContinue | ForEach-Object {
    $size = "{0:N2} KB" -f ($_.Length / 1KB)
    Write-Host "   $($_.Name) - $size"
}

$TOTAL_SUCCESS = $PYTHON_SUCCESS + $R_SUCCESS
$TOTAL_EXPECTED = $PYTHON_SCRIPTS.Count
if ($R_INSTALLED) {
    $TOTAL_EXPECTED++
}

Write-Host ""
if ($TOTAL_SUCCESS -eq $TOTAL_EXPECTED) {
    Write-Host "✓ All figures generated successfully!" -ForegroundColor Green
    exit 0
} else {
    Write-Host "⚠ Some figures failed to generate. Check error messages above." -ForegroundColor Yellow
    exit 1
}
