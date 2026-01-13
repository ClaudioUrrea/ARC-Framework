# FigShare Upload Instructions

This document provides step-by-step instructions for uploading the ARC Framework repository to FigShare.

## DOI Information

- **Reserved DOI:** 10.6084/m9.figshare.31053583
- **URL:** https://doi.org/10.6084/m9.figshare.31053583

## Pre-Upload Checklist

Ensure all files are present and up-to-date:

### Root Directory Files
- [ ] README.md
- [ ] LICENSE
- [ ] CITATION.cff
- [ ] requirements.txt
- [ ] environment.yml
- [ ] .gitignore
- [ ] INSTALL.md
- [ ] REPRODUCE.md
- [ ] CONTRIBUTING.md
- [ ] CHANGELOG.md
- [ ] generate_all_figures.sh
- [ ] generate_all_figures.ps1
- [ ] figshare_metadata.json
- [ ] DATA_AVAILABILITY_STATEMENT.md
- [ ] FIGSHARE_UPLOAD_INSTRUCTIONS.md (this file)

### Code Directory
- [ ] code/python/Generate_Figure2_Taxonomy.py
- [ ] code/python/Generate_Figure3_CostEffectiveness.py
- [ ] code/python/Generate_Figure4_HRC.py
- [ ] code/python/Generate_Figure5_Sensitivity.py
- [ ] code/python/Generate_Figure6_Competency.py
- [ ] code/r/Paper_Figure_7.R

### Data Directory
- [ ] data/HRC_Aggregated_Fanuc.csv
- [ ] data/Sensitivity_Results_Fanuc_Shaded.csv
- [ ] data/README_DATA.md

### Figures Directory
- [ ] figures/Figure1_PRISMA_Flow_Diagram.png
- [ ] figures/Figure2_Technology_Taxonomy.png
- [ ] figures/Figure3_Cost_Effectiveness.png
- [ ] figures/Figure4_HRC_Performance.png
- [ ] figures/Figure5_Sensitivity_Analysis.png
- [ ] figures/Figure6_Competency_Progression.png
- [ ] figures/Figure7_Forest_Plot.png
- [ ] figures/Figure8_ARC_Framework_Implementation_Pathway.png

### Paper Directory
- [ ] paper/Paper_Applied_Sciences_13_01_2026.pdf

## FigShare Upload Process

### Step 1: Prepare Archive

Create a ZIP archive of the entire repository:

**Linux/macOS:**
```bash
cd /path/to/ARC_Framework_Repository
zip -r ARC_Framework_v1.0.0.zip . -x "*.git*" "*.DS_Store" "__pycache__/*"
```

**Windows (PowerShell):**
```powershell
Compress-Archive -Path . -DestinationPath ARC_Framework_v1.0.0.zip -Force
```

**Expected archive size:** Approximately 8-10 MB

### Step 2: Login to FigShare

1. Go to https://figshare.com
2. Click "Log in" or "Sign up" if you don't have an account
3. Use your institutional credentials or create an account

### Step 3: Create New Item

1. Click "Create a new item" or "Upload"
2. Select item type: **Dataset**
3. Click "Continue"

### Step 4: Upload Files

Two options:

**Option A: Upload ZIP Archive**
1. Drag and drop `ARC_Framework_v1.0.0.zip`
2. Wait for upload to complete
3. FigShare will automatically extract the archive

**Option B: Upload Individual Files** (if archive fails)
1. Upload all files maintaining directory structure
2. This may take longer but ensures all files are accessible

### Step 5: Add Metadata

Fill in the following fields using information from `figshare_metadata.json`:

#### Basic Information

**Title:**
```
ARC Framework: Industrial Robotics and Adaptive Control Systems in STEM Education - Complete Repository
```

**Description:**
```
This repository contains the complete code, data, and supplementary materials for the systematic review "Industrial Robotics and Adaptive Control Systems in STEM Education: Systematic Review of Technology Transfer from Industry to Classroom and Competency Development Framework". 

The ARC (Automation-Robotics-Control) Framework provides evidence-based guidance for integrating industrial-grade robotics and adaptive control systems into engineering education. Based on systematic review of 52 empirical studies (2019-2025), the framework includes: (1) five-level technology complexity taxonomy, (2) competency progression model from novice to expert, (3) pedagogical strategies matrix, and (4) implementation pathways. 

Meta-analysis reveals large positive effects (Hedges' g = 0.783, 95% CI: 0.719-0.847) with industrial-grade systems demonstrating 26% improvement over educational kits. Remote laboratories achieve optimal cost-effectiveness at $45/student versus $280 for physical labs. 

Repository includes: Python and R code for all figures, experimental datasets from Fanuc M-20iA industrial manipulator, complete documentation, and reproduction instructions.
```

**Categories:**
- Education
- Engineering
- Robotics  
- Applied Computer Science
- Automation and Control Engineering

**Keywords (comma-separated):**
```
Industrial robotics, Adaptive control, STEM education, Engineering education, Industry 4.0, Systematic review, Meta-analysis, Competency development, Technology transfer, ARC Framework, Human-robot collaboration, Educational technology, Reinforcement learning, Cost-effectiveness analysis, Remote laboratories
```

#### Authors

**Author 1:**
- Name: Claudio Urrea
- ORCID: 0000-0002-9716-7380
- Email: claudio.urrea@usach.cl
- Affiliation: University of Santiago of Chile

#### Funding

**Funder:**
- Funder name: Faculty of Engineering, University of Santiago of Chile
- Grant code: N/A (Institutional Support)

#### License

- Select: **CC BY 4.0**
- URL will be auto-populated

#### References

**Link to published article:**
```
Title: Industrial Robotics and Adaptive Control Systems in STEM Education: Systematic Review of Technology Transfer from Industry to Classroom and Competency Development Framework
DOI: 10.3390/appXXXXXXXX
URL: https://www.mdpi.com/journal/applsci
```

#### Custom Fields

Add these as custom metadata:
- Journal: Applied Sciences
- Volume: 16
- Issue: 2
- Year: 2026
- Publisher: MDPI
- Number_of_Studies: 52
- Study_Period: 2019-2025
- Meta_Analysis_Effect_Size: Hedges' g = 0.783 [0.719-0.847]
- GitHub_Repository: https://github.com/ClaudioUrrea/ARC-Framework

#### Related Identifiers

**GitHub Repository:**
- Type: URL
- Relation: is supplemented by
- Identifier: https://github.com/ClaudioUrrea/ARC-Framework

**Published Article:**
- Type: DOI
- Relation: is cited by
- Identifier: 10.3390/appXXXXXXXX

### Step 6: Review and Publish

1. Review all metadata for accuracy
2. Check that all files uploaded correctly
3. Preview how the item will appear
4. Click "Publish" to make publicly available
5. Copy the assigned DOI (should be 10.6084/m9.figshare.31053583)

### Step 7: Post-Publication

1. **Update Paper:** Add FigShare link to Data Availability Statement
2. **Update GitHub:** Add FigShare DOI badge to README
3. **Test Access:** Verify all files are downloadable
4. **Share:** Announce on social media, mailing lists, etc.

## FigShare Best Practices

### File Organization
- Keep directory structure intact
- Use descriptive file names
- Include README files in each directory
- Maximum individual file size: 5 GB
- Maximum total size: 20 GB (well within our ~10 MB)

### Versioning
- FigShare supports versioning
- Update version number in metadata when making changes
- Old versions remain accessible
- DOI resolves to latest version

### Access Statistics
FigShare provides:
- View counts
- Download statistics
- Geographic distribution of users
- Citation tracking

### Embargo Options
- We're publishing immediately (no embargo)
- Can embargo if needed for journal requirements
- Embargo can be lifted later

## Troubleshooting

### Upload Fails
- **Issue:** Large archive fails to upload
- **Solution:** Upload individual files or use multiple smaller archives

### Missing Files
- **Issue:** Some files not visible after upload
- **Solution:** Check file size limits, re-upload missing files individually

### Metadata Errors
- **Issue:** Required fields not accepted
- **Solution:** Check character limits, special characters, formatting

### DOI Not Assigned
- **Issue:** Custom DOI not recognized
- **Solution:** Contact FigShare support with reservation confirmation

## FigShare Support

If you encounter issues:
- **Help Center:** https://help.figshare.com
- **Email:** support@figshare.com
- **Response Time:** Usually within 1 business day

## Verification After Upload

Verify the following after publication:

1. [ ] DOI resolves correctly
2. [ ] All files are downloadable
3. [ ] README displays properly
4. [ ] Metadata is accurate and complete
5. [ ] License is correct (CC BY 4.0)
6. [ ] Author information is correct
7. [ ] Keywords are indexed
8. [ ] Related identifiers link correctly
9. [ ] Download counts are tracking
10. [ ] Item appears in search results

## Post-Upload Actions

### Update Paper
Replace Data Availability Statement with:
```
Data Availability Statement: All data, code, and materials are openly 
available at FigShare: https://doi.org/10.6084/m9.figshare.31053583 and 
GitHub: https://github.com/ClaudioUrrea/ARC-Framework under CC BY 4.0 license.
```

### Update GitHub README
Add FigShare badge:
```markdown
[![DOI](https://img.shields.io/badge/DOI-10.6084%2Fm9.figshare.31053583-blue)]
(https://doi.org/10.6084/m9.figshare.31053583)
```

### Announce Release
- Twitter/X: Share link with key findings
- LinkedIn: Post about framework publication
- ResearchGate: Link to FigShare deposit
- Institutional website: Add to faculty publications
- Mailing lists: ASEE, IEEE Education Society

## Long-Term Maintenance

### Annual Updates
- Review for broken links
- Update with new data if available
- Increment version number
- Update CHANGELOG.md

### Respond to Issues
- Monitor FigShare comments
- GitHub issues may reference FigShare
- Update FAQ if common questions arise

### Citation Tracking
- Google Scholar: Track citations
- FigShare metrics: Monitor downloads
- Altmetrics: Track social media mentions

## Contact

**Repository Maintainer:**
Claudio Urrea  
claudio.urrea@usach.cl  
University of Santiago of Chile

**For FigShare-specific questions:**
Contact FigShare support or the repository maintainer.

---

Last updated: January 13, 2026
