# Reproduction Guide

This guide provides step-by-step instructions for reproducing all figures and analyses from the paper.

## Prerequisites

Ensure you have completed the installation steps in [INSTALL.md](INSTALL.md).

## Quick Reproduction (All Figures)

To generate all figures at once:

### Bash Script (Linux/macOS)
```bash
#!/bin/bash
cd code/python
python Generate_Figure2_Taxonomy.py
python Generate_Figure3_CostEffectiveness.py
python Generate_Figure4_HRC.py
python Generate_Figure5_Sensitivity.py
python Generate_Figure6_Competency.py

cd ../r
Rscript Paper_Figure_7.R

echo "All figures generated successfully!"
echo "Check the figures/ directory for outputs"
```

### PowerShell Script (Windows)
```powershell
cd code\python
python Generate_Figure2_Taxonomy.py
python Generate_Figure3_CostEffectiveness.py
python Generate_Figure4_HRC.py
python Generate_Figure5_Sensitivity.py
python Generate_Figure6_Competency.py

cd ..\r
Rscript Paper_Figure_7.R

Write-Host "All figures generated successfully!"
Write-Host "Check the figures\ directory for outputs"
```

## Individual Figure Reproduction

### Figure 1: PRISMA Flow Diagram
**Status:** Provided as pre-generated PNG file  
**File:** `figures/Figure1_PRISMA_Flow_Diagram.png`  
**Note:** This figure was created manually using diagramming software based on systematic review methodology.

---

### Figure 2: Technology Complexity Taxonomy

**Description:** ARC Framework five-level technology taxonomy pyramid showing progression from educational kits to industrial-grade systems.

**Command:**
```bash
cd code/python
python Generate_Figure2_Taxonomy.py
```

**Output:** `Figure2_Technology_Taxonomy.png` (300 DPI)

**Expected Result:**
- Five-level pyramid visualization
- Color gradient from light purple (Level 1) to dark blue (Level 5)
- Effect sizes ranging from d = 0.59 to d = 0.94
- Cost ranges displayed for each level

**Execution Time:** ~2 seconds

---

### Figure 3: Cost-Effectiveness Analysis

**Description:** Bubble chart comparing effect sizes vs. costs across technology levels, with remote labs highlighted as optimal solution.

**Command:**
```bash
cd code/python
python Generate_Figure3_CostEffectiveness.py
```

**Output:** `Figure3_Cost_Effectiveness.png` (300 DPI)

**Expected Result:**
- Log-scale X-axis for costs
- Six technology implementation models plotted
- Remote Lab highlighted with gold star
- Color-coded bubbles by impact-per-$1000
- Trend line for physical laboratories

**Execution Time:** ~3 seconds

---

### Figure 4: HRC Performance Metrics

**Description:** Four-panel visualization of adaptive multi-objective reinforcement learning performance on Fanuc M-20iA industrial manipulator.

**Data Required:** `data/HRC_Aggregated_Fanuc.csv`

**Command:**
```bash
cd code/python
python Generate_Figure4_HRC.py
```

**Output:** `Figure4_HRC_Performance.png` (300 DPI)

**Expected Result:**
- Panel (a): Throughput evolution with 20-episode moving average
- Panel (b): Human workload optimization (inverted Y-axis)
- Panel (c): Safety score progression
- Panel (d): Multi-objective trade-off space with Pareto frontier
- All panels show first 200 episodes

**Statistics Printed:**
```
Mean Throughput: 15.3 tasks/hour
Mean Workload: 45.2% (0-100 scale)
Mean Safety: 87.6% (0-100 scale)
Pareto-optimal points: [varies by data]
```

**Execution Time:** ~5 seconds

---

### Figure 5: Sensitivity Analysis

**Description:** Grouped bar chart showing robustness of HRC system across parameter variations (±10%).

**Data Required:** `data/Sensitivity_Results_Fanuc_Shaded.csv`

**Command:**
```bash
cd code/python
python Generate_Figure5_Sensitivity.py
```

**Output:** `Figure5_Sensitivity_Analysis.png` (300 DPI)

**Expected Result:**
- 12 parameter configurations grouped into 4 categories
- Three metrics per configuration: Throughput, Workload, Safety
- Baseline values marked with vertical dotted lines
- Error bars showing ±1 SD across 10 trials
- Color-coded background shading by parameter group

**Execution Time:** ~4 seconds

---

### Figure 6: Competency Progression Model

**Description:** Five-level developmental pathway from Novice to Expert with aligned technology levels and pedagogical approaches.

**Command:**
```bash
cd code/python
python Generate_Figure6_Competency.py
```

**Output:** `Figure6_Competency_Progression.png` (300 DPI)

**Expected Result:**
- Five horizontal rows representing competency levels
- Three columns: Competency characteristics, Technology level, Pedagogical approaches
- Color-coded boxes (light purple → dark blue progression)
- Typical duration indicators on right side
- Progression arrows between levels

**Execution Time:** ~3 seconds

---

### Figure 7: Meta-Analysis Forest Plot

**Description:** Random-effects meta-analysis forest plot showing effect sizes across technology complexity levels for 12 representative studies.

**Data Source:** Embedded in R script (12 studies from 52-study corpus)

**Command:**
```bash
cd code/r
Rscript Paper_Figure_7.R
```

**Output:** `Figure7_Forest_Plot.png` (150 DPI, 1400×1100 pixels)

**Expected Result:**
- 12 individual studies plotted with effect sizes and 95% CIs
- Color-coded by technology level (blue = industrial, orange = educational, gray = semi-industrial)
- Overall pooled effect: g = 0.786 [0.726, 0.846]
- Heterogeneity statistics: I² = 32.8%, Q(11) = 16.23, p = 0.131

**Console Output:**
```
META-ANALYSIS RESULTS - Forest Plot (12 representative studies from n=52)
================================================================================

Overall Effect (Random-Effects Model):
  Hedges' g = 0.786 [95% CI: 0.726, 0.846]
  Z = 23.735, p < 0.0001

Heterogeneity Statistics:
  Q(df = 11) = 16.233, p = 0.1314
  I² = 32.25%
  τ² = 0.0164

Subgroup Analysis by Technology Level:
  Industrial-Grade Systems (n = 6, BLUE shading):
    Pooled g = 0.906 [95% CI: 0.851, 0.962]
    Studies: Zamora, Makulavicius, Zhang, Urrea, Nomandela, UR Remote Lab

  Educational Kits (n = 5, ORANGE shading):
    Pooled g = 0.718 [95% CI: 0.650, 0.786]
    Studies: Ouyang, Antunes, Alginahi, Tang, Silva

  Semi-Industrial (n = 1, GRAY shading):
    Studies: Dobot Platform
    Effect size: g = 0.680

Between-Group Comparison:
  Difference: 0.188 (Industrial > Educational)
  Relative improvement: 26.2%
```

**Execution Time:** ~10-15 seconds

---

### Figure 8: ARC Framework Implementation Pathway

**Status:** Provided as pre-generated PNG file  
**File:** `figures/Figure8_ARC_Framework_Implementation_Pathway.png`  
**Note:** This flowchart was created using diagramming software based on framework design.

---

## Data Files

### HRC_Aggregated_Fanuc.csv

**Description:** Performance metrics from industrial HRC system over 1000 training episodes

**Structure:**
```
Episode, Throughput, Workload, Safety
1, 5.234, 0.823, 0.912
2, 5.456, 0.807, 0.918
...
1000, 6.123, 0.734, 0.956
```

**Columns:**
- `Episode`: Training episode number (1-1000)
- `Throughput`: Tasks per hour (range: ~5.0-7.0)
- `Workload`: Human cognitive load normalized 0-1 (lower is better)
- `Safety`: Safety score normalized 0-1 (higher is better)

**Usage:** Figure 4

---

### Sensitivity_Results_Fanuc_Shaded.csv

**Description:** Robustness analysis across parameter variations

**Structure:**
```
Parameter, Value, Throughput, Workload, Safety, Std_Throughput, Std_Workload, Std_Safety
fatigueRate, 0.9, 6.553, 1235.0, 0.9993, 0.120, 15.2, 0.0012
fatigueRate, 1.0, 6.600, 1242.5, 0.9971, 0.118, 14.8, 0.0015
...
```

**Columns:**
- `Parameter`: Parameter name (fatigueRate, w1, w3, auctionFrequency)
- `Value`: Parameter variation (0.9 = -10%, 1.0 = baseline, 1.1 = +10%)
- `Throughput`: Mean throughput (tasks/hour)
- `Workload`: Mean workload (actual range 1200-1300)
- `Safety`: Mean safety score (0-1 scale)
- `Std_*`: Standard deviations across 10 trials

**Usage:** Figure 5

---

## Verification

### Check Output Files

After running all scripts:
```bash
ls -lh figures/
```

Expected output:
```
Figure1_PRISMA_Flow_Diagram.png        (~1.5 MB)
Figure2_Technology_Taxonomy.png        (~200 KB)
Figure3_Cost_Effectiveness.png         (~250 KB)
Figure4_HRC_Performance.png            (~400 KB)
Figure5_Sensitivity_Analysis.png       (~350 KB)
Figure6_Competency_Progression.png     (~300 KB)
Figure7_Forest_Plot.png                (~180 KB)
Figure8_ARC_Framework_Implementation_Pathway.png  (~2.0 MB)
```

### Visual Verification

Open each figure and verify:
- **Figure 2:** Five-level pyramid, correct effect sizes
- **Figure 3:** Remote lab with gold star, logarithmic X-axis
- **Figure 4:** Four panels, moving averages visible
- **Figure 5:** Grouped bars, error bars present
- **Figure 6:** Five rows, three columns, progression arrows
- **Figure 7:** Forest plot with diamond at bottom
- **Figure 8:** Complete flowchart

### Numerical Verification

Check that printed statistics match paper:
- **Overall effect size:** g = 0.783-0.786 (slight variation due to rounding)
- **Industrial systems:** g ≈ 0.91-0.92
- **Educational kits:** g ≈ 0.72-0.73
- **Heterogeneity:** I² ≈ 32-33%

## Troubleshooting

### Issue: Figures appear different from paper

**Possible Causes:**
1. Different matplotlib version (affects rendering)
2. Missing fonts (Palatino Linotype)
3. Different DPI settings

**Solutions:**
```python
# Check matplotlib version
import matplotlib
print(matplotlib.__version__)  # Should be 3.5+

# Install missing fonts (system-specific)
# Linux: sudo apt install fonts-linuxlibertine
# macOS: System Preferences → Fonts → Add Palatino
# Windows: Usually included by default
```

### Issue: Data file not found

**Solution:**
```bash
# Verify data files exist
ls data/

# Should show:
# HRC_Aggregated_Fanuc.csv
# Sensitivity_Results_Fanuc_Shaded.csv

# If missing, download from FigShare:
# https://doi.org/10.6084/m9.figshare.31053583
```

### Issue: R script fails

**Common Errors:**
```r
# Error: package 'metafor' is not installed
install.packages("metafor")

# Error: cannot open file
# Check working directory
getwd()
setwd("path/to/ARC-Framework/code/r")
```

## Computational Environment

### Tested Configurations

**Configuration 1:**
- OS: Ubuntu 22.04 LTS
- Python: 3.10.12
- R: 4.2.2
- matplotlib: 3.7.1
- pandas: 2.0.1
- numpy: 1.24.3
- metafor: 4.2-0

**Configuration 2:**
- OS: macOS 13.5 (Ventura)
- Python: 3.11.4
- R: 4.3.1
- matplotlib: 3.7.2
- pandas: 2.0.3
- numpy: 1.25.1
- metafor: 4.4-0

**Configuration 3:**
- OS: Windows 11 Pro
- Python: 3.9.13
- R: 4.3.0
- matplotlib: 3.5.3
- pandas: 1.5.3
- numpy: 1.23.5
- metafor: 4.2-0

### Performance Benchmarks

Total execution time (all figures):
- Fast machine (8-core, 16GB RAM): ~25 seconds
- Standard machine (4-core, 8GB RAM): ~35 seconds
- Slow machine (2-core, 4GB RAM): ~60 seconds

## Additional Resources

- **Main README:** [README.md](README.md)
- **Installation Guide:** [INSTALL.md](INSTALL.md)
- **Paper PDF:** `paper/Paper_Applied_Sciences_13_01_2026.pdf`
- **FigShare Repository:** https://doi.org/10.6084/m9.figshare.31053583
- **GitHub Repository:** https://github.com/ClaudioUrrea/ARC-Framework

## Citation

If you use these reproduction materials, please cite:

```bibtex
@article{urrea2026arc,
  title={Industrial Robotics and Adaptive Control Systems in STEM Education: Systematic Review of Technology Transfer from Industry to Classroom and Competency Development Framework},
  author={Urrea, Claudio},
  journal={Applied Sciences},
  year={2026},
  doi={10.3390/appXXXXXXXX}
}
```

## Contact

For questions about reproduction:
- **Email:** claudio.urrea@usach.cl
- **GitHub Issues:** https://github.com/ClaudioUrrea/ARC-Framework/issues
