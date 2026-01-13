# ARC Framework: Automation-Robotics-Control for Engineering Education

[![DOI](https://img.shields.io/badge/DOI-10.6084%2Fm9.figshare.31053583-blue)](https://doi.org/10.6084/m9.figshare.31053583)
[![GitHub](https://img.shields.io/badge/GitHub-ClaudioUrrea%2FARC--Framework-green)](https://github.com/ClaudioUrrea/ARC-Framework)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## Overview

This repository contains the complete code, data, and supplementary materials for the systematic review:

**"Industrial Robotics and Adaptive Control Systems in STEM Education: Systematic Review of Technology Transfer from Industry to Classroom and Competency Development Framework"**

**Author:** Claudio Urrea  
**Affiliation:** Department of Electrical Engineering, Faculty of Engineering, University of Santiago of Chile  
**Published:** Applied Sciences, 2026

## Citation

If you use this framework or code in your research, please cite:

```bibtex
@article{urrea2026arc,
  title={Industrial Robotics and Adaptive Control Systems in STEM Education: Systematic Review of Technology Transfer from Industry to Classroom and Competency Development Framework},
  author={Urrea, Claudio},
  journal={Applied Sciences},
  year={2026},
  volume={16},
  number={2},
  pages={XXX},
  doi={10.3390/appXXXXXXXX},
  publisher={MDPI}
}
```

## Repository Structure

```
ARC-Framework/
├── README.md                              # This file
├── LICENSE                                # CC BY 4.0 License
├── CITATION.cff                           # Citation metadata
├── requirements.txt                       # Python dependencies
├── environment.yml                        # Conda environment specification
├── INSTALL.md                            # Installation instructions
├── REPRODUCE.md                          # Reproduction instructions
│
├── code/
│   ├── python/
│   │   ├── Generate_Figure2_Taxonomy.py
│   │   ├── Generate_Figure3_CostEffectiveness.py
│   │   ├── Generate_Figure4_HRC.py
│   │   ├── Generate_Figure5_Sensitivity.py
│   │   └── Generate_Figure6_Competency.py
│   └── r/
│       └── Paper_Figure_7.R
│
├── data/
│   ├── HRC_Aggregated_Fanuc.csv
│   ├── Sensitivity_Results_Fanuc_Shaded.csv
│   └── README_DATA.md
│
├── figures/
│   ├── Figure1_PRISMA_Flow_Diagram.png
│   ├── Figure2_Technology_Taxonomy.png
│   ├── Figure3_Cost_Effectiveness.png
│   ├── Figure4_HRC_Performance.png
│   ├── Figure5_Sensitivity_Analysis.png
│   ├── Figure6_Competency_Progression.png
│   ├── Figure7_Forest_Plot.png
│   └── Figure8_ARC_Framework_Implementation_Pathway.png
│
├── paper/
│   └── Paper_Applied_Sciences_13_01_2026.pdf
│
└── supplementary/
    ├── ARC_Framework_Implementation_Guide.pdf
    ├── Assessment_Rubrics.xlsx
    └── Technology_Selection_Decision_Tool.xlsx
```

## Quick Start

### Prerequisites

- Python 3.8 or higher
- R 4.0 or higher
- pip or conda package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/ClaudioUrrea/ARC-Framework.git
cd ARC-Framework

# Install Python dependencies
pip install -r requirements.txt

# Or use conda
conda env create -f environment.yml
conda activate arc-framework
```

### Generate All Figures

```bash
# Python figures
cd code/python
python Generate_Figure2_Taxonomy.py
python Generate_Figure3_CostEffectiveness.py
python Generate_Figure4_HRC.py
python Generate_Figure5_Sensitivity.py
python Generate_Figure6_Competency.py

# R figure
cd ../r
Rscript Paper_Figure_7.R
```

## Key Contributions

### 1. Technology Complexity Taxonomy (5 Levels)
- **Level 1-2:** Educational kits (LEGO, VEX) - Effect size d = 0.59-0.64
- **Level 3:** Advanced educational (Dobot, Arduino) - Effect size d = 0.68
- **Level 4:** Didactic industrial (SCORBOT, UR3) - Effect size d = 0.73
- **Level 5:** Industrial-grade (UR5e, KUKA, ABB) - Effect size d = 0.94

### 2. Meta-Analysis Results
- **Overall pooled effect:** Hedges' g = 0.783 (95% CI: 0.719-0.847)
- **52 empirical studies** analyzed (2019-2025)
- **Heterogeneity:** I² = 32.8% (moderate)
- **Industrial-grade systems:** 26% improvement over educational kits

### 3. Cost-Effectiveness Analysis
- **Remote laboratories:** Optimal ROI at $45/student (g = 0.89)
- **Physical industrial labs:** $280/student (g = 0.94)
- **Impact per $1000:** Remote labs achieve 19.8 vs. 3.4 for physical labs

### 4. ARC Framework Components
- Technology progression pathways
- Competency development model (Novice → Expert)
- Pedagogical strategies matrix
- Implementation decision-support tool

## Data Description

### HRC_Aggregated_Fanuc.csv
Performance metrics from Fanuc M-20iA industrial manipulator implementing adaptive multi-objective reinforcement learning for human-robot collaboration:
- **Episodes:** 1000 training iterations
- **Throughput:** Tasks per hour (mean = 15.3)
- **Workload:** Human cognitive load 0-100 (mean = 45.2, lower is better)
- **Safety:** Safety score 0-100 (mean = 87.6, higher is better)

### Sensitivity_Results_Fanuc_Shaded.csv
Robustness analysis across parameter variations:
- **Parameters tested:** Fatigue rate, reward weights (w₁, w₃), auction frequency
- **Variations:** ±10% from baseline
- **Trials:** 10 independent runs per configuration
- **Metrics:** Throughput, workload, safety with standard deviations

## Reproducibility

All figures and analyses are fully reproducible. See [REPRODUCE.md](REPRODUCE.md) for detailed instructions.

**System Requirements:**
- Python 3.8+ with matplotlib, pandas, numpy
- R 4.0+ with metafor package
- Approximately 2GB RAM
- Execution time: ~5 minutes total

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

You are free to:
- **Share** — copy and redistribute the material
- **Adapt** — remix, transform, and build upon the material

Under the following terms:
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made.

## Contact

**Claudio Urrea**  
Department of Electrical Engineering  
University of Santiago of Chile  
Email: claudio.urrea@usach.cl

## Acknowledgments

This work was supported by the Faculty of Engineering, University of Santiago of Chile. The author thanks the anonymous reviewers for their valuable comments that substantially improved the quality of this manuscript.

## Related Resources

- **FigShare Repository:** https://doi.org/10.6084/m9.figshare.31053583
- **GitHub Repository:** https://github.com/ClaudioUrrea/ARC-Framework
- **Applied Sciences Journal:** https://www.mdpi.com/journal/applsci

## Version History

- **v1.0.0** (January 2026): Initial release with complete systematic review results
