#!/bin/bash
# ==============================================================================
# ARC Framework: Generate All Figures
# ==============================================================================
# This script generates all figures from the paper.
# Prerequisites: Python 3.8+, R 4.0+, required packages installed
# Usage: bash generate_all_figures.sh
# ==============================================================================

echo "======================================================================"
echo "ARC Framework: Generating All Figures"
echo "======================================================================"
echo ""

# Store starting directory
START_DIR=$(pwd)

# Check if we're in the repository root
if [ ! -d "code" ] || [ ! -d "data" ] || [ ! -d "figures" ]; then
    echo "ERROR: Please run this script from the repository root directory."
    echo "Expected directory structure:"
    echo "  - code/"
    echo "  - data/"
    echo "  - figures/"
    exit 1
fi

# Check Python installation
echo "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed or not in PATH."
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "  ✓ Python $PYTHON_VERSION found"

# Check required Python packages
echo "Checking Python packages..."
python3 -c "import matplotlib, pandas, numpy" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "ERROR: Required Python packages not installed."
    echo "Please run: pip install -r requirements.txt"
    exit 1
fi
echo "  ✓ matplotlib, pandas, numpy found"

# Check R installation (optional, only needed for Figure 7)
R_INSTALLED=false
if command -v Rscript &> /dev/null; then
    R_VERSION=$(Rscript --version 2>&1 | head -1 | awk '{print $5}')
    echo "  ✓ R $R_VERSION found"
    R_INSTALLED=true
    
    # Check metafor package
    Rscript -e "library(metafor)" 2>/dev/null
    if [ $? -ne 0 ]; then
        echo "  ⚠ R package 'metafor' not installed. Figure 7 will be skipped."
        echo "    To install: Rscript -e \"install.packages('metafor')\""
        R_INSTALLED=false
    else
        echo "  ✓ R package 'metafor' found"
    fi
else
    echo "  ⚠ R not found. Figure 7 will be skipped."
fi

echo ""
echo "======================================================================"
echo "Generating Python Figures (2, 3, 4, 5, 6)"
echo "======================================================================"
echo ""

# Array of Python scripts
PYTHON_SCRIPTS=(
    "Generate_Figure2_Taxonomy.py"
    "Generate_Figure3_CostEffectiveness.py"
    "Generate_Figure4_HRC.py"
    "Generate_Figure5_Sensitivity.py"
    "Generate_Figure6_Competency.py"
)

# Generate Python figures
PYTHON_SUCCESS=0
for script in "${PYTHON_SCRIPTS[@]}"; do
    echo "Running: $script"
    cd "$START_DIR/code/python" || exit 1
    python3 "$script"
    if [ $? -eq 0 ]; then
        echo "  ✓ Success"
        ((PYTHON_SUCCESS++))
    else
        echo "  ✗ Failed"
    fi
    echo ""
    cd "$START_DIR" || exit 1
done

echo ""
echo "======================================================================"
echo "Generating R Figure (7)"
echo "======================================================================"
echo ""

# Generate R figure if R is available
R_SUCCESS=0
if [ "$R_INSTALLED" = true ]; then
    echo "Running: Paper_Figure_7.R"
    cd "$START_DIR/code/r" || exit 1
    Rscript Paper_Figure_7.R
    if [ $? -eq 0 ]; then
        echo "  ✓ Success"
        R_SUCCESS=1
    else
        echo "  ✗ Failed"
    fi
    echo ""
    cd "$START_DIR" || exit 1
else
    echo "Skipping Figure 7 (R not available)"
    echo ""
fi

echo ""
echo "======================================================================"
echo "Summary"
echo "======================================================================"
echo ""
echo "Python figures generated: $PYTHON_SUCCESS / ${#PYTHON_SCRIPTS[@]}"
if [ "$R_INSTALLED" = true ]; then
    echo "R figures generated: $R_SUCCESS / 1"
fi
echo ""
echo "Generated figures are in: figures/"
echo ""

# List generated figures
echo "Files in figures/ directory:"
ls -lh figures/*.png 2>/dev/null | awk '{print "  ", $9, "-", $5}'

TOTAL_SUCCESS=$((PYTHON_SUCCESS + R_SUCCESS))
TOTAL_EXPECTED=$((${#PYTHON_SCRIPTS[@]} + (R_INSTALLED ? 1 : 0)))

if [ $TOTAL_SUCCESS -eq $TOTAL_EXPECTED ]; then
    echo ""
    echo "✓ All figures generated successfully!"
    exit 0
else
    echo ""
    echo "⚠ Some figures failed to generate. Check error messages above."
    exit 1
fi
