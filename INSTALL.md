# Installation Guide

This guide provides detailed instructions for setting up the ARC Framework software environment.

## System Requirements

### Minimum Requirements
- **Operating System:** Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **RAM:** 2 GB minimum, 4 GB recommended
- **Disk Space:** 500 MB for software + 100 MB for data
- **Python:** Version 3.8 or higher
- **R:** Version 4.0 or higher (required only for Figure 7)

### Software Dependencies
- Python 3.8+
- pip or conda package manager
- R 4.0+ (optional, only needed for forest plot generation)

## Installation Methods

### Method 1: Quick Installation with pip (Recommended)

```bash
# Clone the repository
git clone https://github.com/ClaudioUrrea/ARC-Framework.git
cd ARC-Framework

# Install Python dependencies
pip install -r requirements.txt

# Verify installation
python -c "import matplotlib; import pandas; import numpy; print('Installation successful!')"
```

### Method 2: Installation with conda

```bash
# Clone the repository
git clone https://github.com/ClaudioUrrea/ARC-Framework.git
cd ARC-Framework

# Create and activate conda environment
conda env create -f environment.yml
conda activate arc-framework

# Verify installation
python -c "import matplotlib; import pandas; import numpy; print('Installation successful!')"
```

### Method 3: Manual Installation

If you prefer to install packages manually:

```bash
# Python packages
pip install numpy>=1.21.0
pip install pandas>=1.4.0
pip install matplotlib>=3.5.0
pip install scipy>=1.8.0
pip install openpyxl>=3.0.0
```

## R Installation (for Figure 7 only)

### Installing R

**Windows:**
1. Download R from https://cran.r-project.org/bin/windows/base/
2. Run the installer and follow prompts
3. Download RStudio (optional): https://www.rstudio.com/products/rstudio/download/

**macOS:**
1. Download R from https://cran.r-project.org/bin/macosx/
2. Install the .pkg file
3. Download RStudio (optional): https://www.rstudio.com/products/rstudio/download/

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install r-base r-base-dev
```

### Installing R Package (metafor)

Open R or RStudio and run:
```r
install.packages("metafor")
library(metafor)  # Verify installation
```

Or from command line:
```bash
Rscript -e "install.packages('metafor', repos='https://cran.r-project.org')"
```

## Verification

### Test Python Installation

```bash
cd code/python
python -c "
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print('NumPy version:', np.__version__)
print('Pandas version:', pd.__version__)
print('Matplotlib version:', plt.matplotlib.__version__)
print('All Python packages installed correctly!')
"
```

### Test R Installation

```bash
cd code/r
Rscript -e "
library(metafor)
cat('metafor version:', as.character(packageVersion('metafor')), '\n')
cat('R installation verified!\n')
"
```

### Test Figure Generation

```bash
# Test Python figure generation
cd code/python
python Generate_Figure2_Taxonomy.py

# Test R figure generation
cd ../r
Rscript Paper_Figure_7.R

# Check that figures were created
ls ../../figures/
```

## Troubleshooting

### Common Issues

#### Issue 1: "ModuleNotFoundError: No module named 'matplotlib'"

**Solution:**
```bash
pip install matplotlib
```

#### Issue 2: "Permission denied" during pip install

**Solution:**
```bash
# Use --user flag
pip install --user -r requirements.txt

# Or create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Issue 3: Conda environment activation fails

**Solution:**
```bash
# Initialize conda for your shell
conda init bash  # or zsh, fish, etc.
# Close and reopen terminal
conda activate arc-framework
```

#### Issue 4: R package installation fails

**Solution:**
```r
# Install from CRAN mirror
install.packages("metafor", repos="https://cloud.r-project.org")

# Or with dependencies
install.packages("metafor", dependencies = TRUE)
```

#### Issue 5: Font warnings in matplotlib

**Solution:**
```python
# Add to Python script if warnings occur
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
```

### Getting Help

If you encounter issues not covered here:

1. **Check existing issues:** https://github.com/ClaudioUrrea/ARC-Framework/issues
2. **Create new issue:** Provide:
   - Operating system and version
   - Python/R versions
   - Complete error message
   - Steps to reproduce
3. **Contact author:** claudio.urrea@usach.cl

## Development Installation

For developers who want to contribute:

```bash
# Clone repository
git clone https://github.com/ClaudioUrrea/ARC-Framework.git
cd ARC-Framework

# Install in development mode
pip install -e .

# Install development dependencies (optional)
pip install pytest pytest-cov black flake8

# Run tests (if available)
pytest tests/
```

## Updating

To update to the latest version:

```bash
cd ARC-Framework
git pull origin main
pip install -r requirements.txt --upgrade
```

## Uninstallation

### Remove Python packages
```bash
pip uninstall numpy pandas matplotlib scipy openpyxl
```

### Remove conda environment
```bash
conda deactivate
conda env remove -n arc-framework
```

### Remove repository
```bash
cd ..
rm -rf ARC-Framework
```

## Next Steps

After successful installation:
1. Read [REPRODUCE.md](REPRODUCE.md) for instructions on reproducing figures
2. Explore the [examples/](examples/) directory for usage examples
3. Review the main [README.md](README.md) for framework documentation

## Version History

- **v1.0.0** (January 2026): Initial release
