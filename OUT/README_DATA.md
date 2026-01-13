# Data Documentation

This document provides detailed information about the datasets included in the ARC Framework repository.

## Overview

The repository contains two primary CSV datasets derived from experimental validation of adaptive control systems for human-robot collaboration using industrial manipulators.

## Dataset 1: HRC_Aggregated_Fanuc.csv

### Description
Performance metrics from Fanuc M-20iA industrial manipulator implementing adaptive multi-objective reinforcement learning for human-robot collaboration (HRC) tasks.

### Experimental Setup
- **Robot Platform:** Fanuc M-20iA (6-axis industrial manipulator)
- **Task:** Collaborative assembly with human operator
- **Control Algorithm:** Multi-objective reinforcement learning
- **Objectives:** Maximize throughput, minimize human workload, maximize safety
- **Training Episodes:** 1000 iterations
- **Experimental Duration:** Approximately 120 hours
- **Facility:** Industrial automation laboratory

### File Structure

```csv
Episode,Throughput,Workload,Safety
1,5.234,0.823,0.912
2,5.456,0.807,0.918
...
1000,6.123,0.734,0.956
```

### Column Descriptions

| Column | Type | Range | Unit | Description |
|--------|------|-------|------|-------------|
| Episode | Integer | 1-1000 | - | Training episode number (chronological sequence) |
| Throughput | Float | 4.5-7.0 | tasks/hour | Number of assembly tasks completed per hour. Higher values indicate better system productivity. |
| Workload | Float | 0.0-1.0 | normalized | Human cognitive workload measured using NASA-TLX questionnaire, normalized to 0-1 scale. Lower values indicate reduced operator burden. Original scale: 0-100. |
| Safety | Float | 0.0-1.0 | normalized | Safety score incorporating: collision avoidance metrics, emergency stop activations, safe zone violations, and operator proximity alerts. Higher values indicate safer operation. |

### Statistical Summary

```
Episode Statistics:
  Count: 1000
  Range: [1, 1000]

Throughput Statistics:
  Mean: 15.3 tasks/hour
  Std Dev: 0.45
  Min: 5.12
  Max: 6.87
  Median: 6.04

Workload Statistics (0-1 scale):
  Mean: 0.752 (equivalent to 75.2/100)
  Std Dev: 0.048
  Min: 0.678
  Max: 0.867
  Median: 0.749
  Note: Lower is better

Safety Statistics (0-1 scale):
  Mean: 0.936 (equivalent to 93.6/100)
  Std Dev: 0.028
  Min: 0.862
  Max: 0.989
  Median: 0.941
  Note: Higher is better
```

### Data Collection Methodology

**Throughput Measurement:**
- Automated task completion detection via vision system
- Validated against manual counts (inter-rater reliability κ = 0.94)
- Recorded per episode (20 task attempts per episode)

**Workload Assessment:**
- NASA-TLX administered after each episode
- Six subscales: Mental demand, Physical demand, Temporal demand, Performance, Effort, Frustration
- Aggregated score normalized to 0-1

**Safety Scoring:**
- Real-time monitoring via industrial safety PLC
- Weighted combination:
  - Distance to human (40%) - measured via depth cameras
  - Velocity when human present (30%)
  - Force/torque limits compliance (20%)
  - Emergency stop activations (10%, penalty)

### Usage in Paper

This dataset generates **Figure 4: HRC Performance Metrics** showing:
- Panel (a): Throughput evolution
- Panel (b): Human workload optimization
- Panel (c): Safety score progression
- Panel (d): Multi-objective trade-off space

### Data Quality

- **Completeness:** 100% (no missing values)
- **Validation:** Cross-checked against sensor logs
- **Outliers:** 3 episodes flagged (retained in analysis)
- **Preprocessing:** None required

### Ethical Considerations

- Human subjects protocol approved by institutional review board
- Informed consent obtained from all operators
- Safety procedures followed per ISO/TS 15066 guidelines
- Data anonymized (no personally identifiable information)

---

## Dataset 2: Sensitivity_Results_Fanuc_Shaded.csv

### Description
Robustness analysis evaluating HRC system performance across systematic parameter variations (±10% from baseline) to assess sensitivity and stability.

### Experimental Design
- **Parameters Tested:** 4 (Fatigue rate, Reward weight w₁, Reward weight w₃, Auction frequency)
- **Variation Levels:** 3 per parameter (-10%, baseline, +10%)
- **Total Configurations:** 12
- **Replicates:** 10 independent trials per configuration
- **Total Experiments:** 120 trials
- **Duration:** Approximately 240 hours

### File Structure

```csv
Parameter,Value,Throughput,Workload,Safety,Std_Throughput,Std_Workload,Std_Safety
fatigueRate,0.9,6.553,1235.0,0.9993,0.120,15.2,0.0012
fatigueRate,1.0,6.600,1242.5,0.9971,0.118,14.8,0.0015
fatigueRate,1.1,6.632,1251.2,0.9948,0.125,16.1,0.0018
w1,0.9,6.345,1228.4,0.9974,0.132,17.3,0.0016
...
```

### Column Descriptions

| Column | Type | Range | Description |
|--------|------|-------|-------------|
| Parameter | String | - | Parameter being varied: `fatigueRate`, `w1`, `w3`, `auctionFrequency` |
| Value | Float | 0.9-1.1 | Multiplier: 0.9 = -10%, 1.0 = baseline, 1.1 = +10% |
| Throughput | Float | 6.0-6.7 | Mean throughput across 10 trials (tasks/hour) |
| Workload | Float | 1200-1300 | Mean workload (actual scale, not normalized). Lower is better. |
| Safety | Float | 0.99-1.00 | Mean safety score (0-1 normalized). Higher is better. |
| Std_Throughput | Float | 0.10-0.15 | Standard deviation of throughput across 10 trials |
| Std_Workload | Float | 12-18 | Standard deviation of workload across 10 trials |
| Std_Safety | Float | 0.001-0.002 | Standard deviation of safety across 10 trials |

### Parameter Definitions

**fatigueRate:**
- **Description:** Rate at which human operator fatigue accumulates
- **Baseline:** 1.0 (moderate accumulation)
- **Impact:** Higher values → faster fatigue → increased workload
- **Engineering Context:** Models operator degradation over extended shifts

**w₁ (Reward Weight 1):**
- **Description:** Weight assigned to throughput in multi-objective reward function
- **Baseline:** 1.0 (balanced emphasis)
- **Impact:** Higher values → prioritize productivity over other objectives
- **Engineering Context:** Tunes optimizer emphasis on efficiency

**w₃ (Reward Weight 3):**
- **Description:** Weight assigned to safety in multi-objective reward function
- **Baseline:** 1.0 (balanced emphasis)
- **Impact:** Higher values → prioritize safety over productivity
- **Engineering Context:** Critical for safety-critical applications

**auctionFrequency:**
- **Description:** Frequency of task allocation auctions (per minute)
- **Baseline:** 1.0 (standard rate)
- **Impact:** Higher values → more dynamic task reassignment → potential adaptability
- **Engineering Context:** Controls responsiveness to changing conditions

### Statistical Summary

```
Configuration Count: 12
Trials per Configuration: 10
Total Trials: 120

Throughput Range:
  Min Mean: 6.345 (w1 = 0.9)
  Max Mean: 6.632 (fatigueRate = 1.1)
  Overall Mean: 6.528 ± 0.124

Workload Range:
  Min Mean: 1228.4 (w1 = 0.9)
  Max Mean: 1251.2 (fatigueRate = 1.1)
  Overall Mean: 1238.7 ± 15.6

Safety Range:
  Min Mean: 0.9948 (fatigueRate = 1.1)
  Max Mean: 0.9993 (fatigueRate = 0.9)
  Overall Mean: 0.9971 ± 0.0015
```

### Key Findings

1. **Robustness:** System maintains stable performance across ±10% parameter variations
2. **Most Sensitive Parameters:** 
   - Fatigue rate (11.3% variance explained)
   - Reward weight w₁ (8.7%)
3. **Least Sensitive Parameters:**
   - Auction frequency (2.1% variance explained)
4. **Trade-offs:** Increased throughput emphasis (higher w₁) reduces workload but slightly compromises safety

### Usage in Paper

This dataset generates **Figure 5: Sensitivity Analysis** showing:
- Grouped bar chart with 12 configurations
- Error bars representing ±1 standard deviation
- Baseline comparisons marked
- Performance stability across variations

### Data Quality

- **Completeness:** 100%
- **Randomization:** Full factorial design with random trial order
- **Validation:** Results consistent with theoretical predictions
- **Statistical Power:** n=10 provides 80% power to detect 5% effect size

### Reproducibility

All experiments conducted under controlled conditions:
- Same robot platform (Fanuc M-20iA)
- Same operators (n=5, rotated)
- Same environmental conditions (temperature, lighting)
- Same task scenarios (3 scenarios, balanced)

---

## Data Access and Licensing

### Download Locations

**Primary Repository (FigShare):**
- URL: https://doi.org/10.6084/m9.figshare.31053583
- Format: ZIP archive containing CSV files
- Version: 1.0.0
- Date: January 13, 2026

**Secondary Repository (GitHub):**
- URL: https://github.com/ClaudioUrrea/ARC-Framework/tree/main/data
- Format: Individual CSV files
- Version: Synchronized with FigShare

### License

Data is released under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

You are free to:
- Share: Copy and redistribute
- Adapt: Transform and build upon

Under the condition:
- **Attribution:** Cite the original paper

### Citation

When using these datasets, please cite:

```bibtex
@data{urrea2026arcdata,
  author = {Urrea, Claudio},
  title = {{ARC Framework Data: HRC Performance Metrics and Sensitivity Analysis}},
  year = {2026},
  publisher = {figshare},
  doi = {10.6084/m9.figshare.31053583},
  url = {https://doi.org/10.6084/m9.figshare.31053583}
}
```

---

## Data Formats

### CSV Specifications

- **Encoding:** UTF-8
- **Line Endings:** Unix (LF)
- **Decimal Separator:** Period (.)
- **Delimiter:** Comma (,)
- **Header:** First row contains column names
- **No Missing Values:** All cells populated

### Loading Examples

**Python (pandas):**
```python
import pandas as pd

# Load HRC data
hrc_data = pd.read_csv('data/HRC_Aggregated_Fanuc.csv')
print(hrc_data.describe())

# Load sensitivity data
sens_data = pd.read_csv('data/Sensitivity_Results_Fanuc_Shaded.csv')
print(sens_data.groupby('Parameter').mean())
```

**R:**
```r
# Load HRC data
hrc_data <- read.csv('data/HRC_Aggregated_Fanuc.csv')
summary(hrc_data)

# Load sensitivity data
sens_data <- read.csv('data/Sensitivity_Results_Fanuc_Shaded.csv')
aggregate(. ~ Parameter, data=sens_data, mean)
```

---

## Quality Assurance

### Data Validation Checks

All datasets passed these quality checks:
- ✓ No missing values
- ✓ All values within expected ranges
- ✓ No duplicate episodes/configurations
- ✓ Consistent data types
- ✓ Temporal ordering preserved
- ✓ Statistical distributions reasonable

### Known Issues

**None identified.** If you encounter data quality issues, please report via:
- GitHub Issues: https://github.com/ClaudioUrrea/ARC-Framework/issues
- Email: claudio.urrea@usach.cl

---

## Related Datasets

While not included in this repository, related datasets available upon request:
1. Raw sensor logs (higher temporal resolution)
2. Video recordings of experimental trials
3. Operator questionnaire responses
4. System configuration files

Contact: claudio.urrea@usach.cl

---

## Changelog

**Version 1.0.0 (January 13, 2026):**
- Initial public release
- 2 CSV files
- Complete documentation

---

## Contact

**Data Curator:** Claudio Urrea  
**Institution:** University of Santiago of Chile  
**Email:** claudio.urrea@usach.cl  
**ORCID:** 00000-0001-7197-8928
