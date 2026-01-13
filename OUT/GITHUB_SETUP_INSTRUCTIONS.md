# GitHub Repository Setup Instructions

This document provides step-by-step instructions for setting up the ARC Framework repository on GitHub.

## Repository Information

- **Repository Name:** ARC-Framework
- **GitHub URL:** https://github.com/ClaudioUrrea/ARC-Framework
- **Visibility:** Public
- **License:** CC BY 4.0

## Prerequisites

1. GitHub account (https://github.com/join)
2. Git installed on your computer
3. Command line access (Terminal/PowerShell)

## Step 1: Create GitHub Repository

### Option A: Via GitHub Website

1. Log in to GitHub
2. Click the "+" icon in the top right
3. Select "New repository"
4. Fill in:
   - **Repository name:** ARC-Framework
   - **Description:** Industrial Robotics and Adaptive Control Systems in STEM Education: Systematic Review and Competency Development Framework
   - **Visibility:** Public
   - **Initialize:** Do NOT initialize with README (we have our own)
5. Click "Create repository"

### Option B: Via GitHub CLI

```bash
gh repo create ClaudioUrrea/ARC-Framework --public \
  --description "Industrial Robotics and Adaptive Control Systems in STEM Education" \
  --clone=false
```

## Step 2: Initialize Local Repository

Navigate to your repository directory and initialize Git:

```bash
cd /path/to/ARC_Framework_Repository

# Initialize Git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: ARC Framework v1.0.0

- Complete systematic review of 52 studies (2019-2025)
- Five-level technology complexity taxonomy
- Meta-analysis (Hedges' g = 0.783)
- Eight publication-quality figures
- Python and R code for all analyses
- Experimental datasets (Fanuc M-20iA)
- Comprehensive documentation
- FigShare repository integration
"
```

## Step 3: Connect to GitHub

```bash
# Add remote repository
git remote add origin https://github.com/ClaudioUrrea/ARC-Framework.git

# Verify remote
git remote -v

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 4: Configure Repository Settings

### General Settings

1. Go to repository Settings
2. Under "General":
   - Enable "Issues"
   - Enable "Projects"
   - Enable "Wiki" (optional)
   - Disable "Discussions" (optional)

### Branch Protection

1. Go to Settings → Branches
2. Add branch protection rule for `main`:
   - Require pull request reviews before merging
   - Require status checks to pass
   - Include administrators

### Topics/Tags

Add repository topics (Settings → General):
```
industrial-robotics
stem-education
systematic-review
meta-analysis
engineering-education
industry-4.0
adaptive-control
education-research
arc-framework
robotics-education
```

### About Section

Update repository description:
- **Description:** Industrial Robotics and Adaptive Control Systems in STEM Education: Systematic Review and Competency Development Framework
- **Website:** https://doi.org/10.6084/m9.figshare.31053583
- **Topics:** (see above)

## Step 5: Add Badges to README

Badges are already included in the README.md, verify they display correctly:

```markdown
[![DOI](https://img.shields.io/badge/DOI-10.6084%2Fm9.figshare.31053583-blue)](https://doi.org/10.6084/m9.figshare.31053583)
[![GitHub](https://img.shields.io/badge/GitHub-ClaudioUrrea%2FARC--Framework-green)](https://github.com/ClaudioUrrea/ARC-Framework)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
```

Optional additional badges:
```markdown
[![GitHub release](https://img.shields.io/github/v/release/ClaudioUrrea/ARC-Framework)](https://github.com/ClaudioUrrea/ARC-Framework/releases)
[![GitHub last commit](https://img.shields.io/github/last-commit/ClaudioUrrea/ARC-Framework)](https://github.com/ClaudioUrrea/ARC-Framework/commits)
[![GitHub issues](https://img.shields.io/github/issues/ClaudioUrrea/ARC-Framework)](https://github.com/ClaudioUrrea/ARC-Framework/issues)
[![GitHub stars](https://img.shields.io/github/stars/ClaudioUrrea/ARC-Framework)](https://github.com/ClaudioUrrea/ARC-Framework/stargazers)
```

## Step 6: Create GitHub Release

### Create v1.0.0 Release

1. Go to "Releases" (right sidebar)
2. Click "Create a new release"
3. Fill in:

**Tag version:** v1.0.0

**Release title:** ARC Framework v1.0.0 - Initial Public Release

**Description:**
```markdown
# ARC Framework v1.0.0 - Initial Public Release

## Overview
First public release of the ARC (Automation-Robotics-Control) Framework for industrial robotics and adaptive control systems in STEM education.

## Key Features
✅ Systematic review of 52 empirical studies (2019-2025)
✅ Five-level technology complexity taxonomy
✅ Competency progression model (Novice → Expert)
✅ Meta-analysis: Hedges' g = 0.783 (95% CI: 0.719-0.847)
✅ Cost-effectiveness analysis (remote labs optimal at $45/student)
✅ Eight publication-quality figures (300 DPI)
✅ Complete Python and R code
✅ Experimental datasets (Fanuc M-20iA, 1000 episodes)
✅ Comprehensive documentation

## What's Included
- **Code:** Python scripts for Figures 2-6, R script for Figure 7
- **Data:** HRC performance metrics, sensitivity analysis results
- **Figures:** All 8 publication figures in high resolution
- **Documentation:** Installation guide, reproduction instructions, data documentation
- **Paper:** Complete manuscript PDF (Applied Sciences, 2026)

## Quick Start
```bash
git clone https://github.com/ClaudioUrrea/ARC-Framework.git
cd ARC-Framework
pip install -r requirements.txt
bash generate_all_figures.sh
```

## Citation
```bibtex
@article{urrea2026arc,
  title={Industrial Robotics and Adaptive Control Systems in STEM Education},
  author={Urrea, Claudio},
  journal={Applied Sciences},
  year={2026},
  doi={10.3390/appXXXXXXXX}
}
```

## Links
- **Paper:** Applied Sciences (MDPI) - https://www.mdpi.com/journal/applsci
- **Data Repository:** FigShare - https://doi.org/10.6084/m9.figshare.31053583
- **Documentation:** [README.md](README.md)
- **Installation:** [INSTALL.md](INSTALL.md)
- **Reproduction:** [REPRODUCE.md](REPRODUCE.md)

## System Requirements
- Python 3.8+
- R 4.0+ (optional, for Figure 7)
- ~2GB RAM
- ~500MB disk space

## License
CC BY 4.0 - See [LICENSE](LICENSE)

## Contact
**Claudio Urrea**  
University of Santiago of Chile  
claudio.urrea@usach.cl
```

4. Attach files (optional):
   - ARC_Framework_v1.0.0.zip (if you created archive)
5. Check "Set as the latest release"
6. Click "Publish release"

## Step 7: Setup GitHub Pages (Optional)

If you want to create a documentation website:

1. Create `docs/` directory with index.html or use existing README
2. Go to Settings → Pages
3. Select source: main branch, /docs folder
4. Save
5. Site will be available at: https://claudiourrea.github.io/ARC-Framework/

## Step 8: Configure GitHub Actions (Optional)

Create `.github/workflows/test.yml` for automated testing:

```yaml
name: Test Figure Generation

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Generate figures
      run: |
        cd code/python
        python Generate_Figure2_Taxonomy.py
        python Generate_Figure3_CostEffectiveness.py
        python Generate_Figure4_HRC.py
        python Generate_Figure5_Sensitivity.py
        python Generate_Figure6_Competency.py
    
    - name: Check figures exist
      run: |
        test -f Figure2_Technology_Taxonomy.png
        test -f Figure3_Cost_Effectiveness.png
        test -f Figure4_HRC_Performance.png
        test -f Figure5_Sensitivity_Analysis.png
        test -f Figure6_Competency_Progression.png
```

## Step 9: Setup Issue Templates

Create `.github/ISSUE_TEMPLATE/`:

### Bug Report Template
`.github/ISSUE_TEMPLATE/bug_report.md`:
```markdown
---
name: Bug report
about: Create a report to help us improve
title: '[BUG] '
labels: bug
assignees: ''
---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Run command '....'
3. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Environment (please complete the following information):**
 - OS: [e.g. Ubuntu 22.04]
 - Python Version: [e.g. 3.9.7]
 - Package Versions: [from pip list]

**Additional context**
Add any other context about the problem here.
```

### Feature Request Template
`.github/ISSUE_TEMPLATE/feature_request.md`:
```markdown
---
name: Feature request
about: Suggest an idea for this project
title: '[FEATURE] '
labels: enhancement
assignees: ''
---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is.

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of alternative solutions.

**Additional context**
Add any other context or screenshots about the feature request here.
```

## Step 10: Add Collaborators (Optional)

If working with others:
1. Go to Settings → Collaborators
2. Click "Add people"
3. Enter GitHub username or email
4. Select role (Read, Write, Admin)
5. Send invitation

## Step 11: Setup Repository Insights

### Configure Insights

1. Go to Insights tab
2. Review:
   - Traffic (views, clones)
   - Commits (activity graph)
   - Community (health check)
   - Contributors

### Community Health Files

Ensure you have:
- [x] README.md
- [x] LICENSE
- [x] CONTRIBUTING.md
- [x] CODE_OF_CONDUCT.md (optional but recommended)
- [x] SECURITY.md (optional)

## Step 12: Social Media Integration

### Announce Repository

**Twitter/X:**
```
🚀 Excited to release the ARC Framework v1.0.0 - evidence-based guidance for 
industrial robotics in STEM education!

📊 Meta-analysis of 52 studies
🤖 5-level technology taxonomy
💰 Optimal cost-effectiveness model
📂 Complete code & data

https://github.com/ClaudioUrrea/ARC-Framework

#RoboticsEducation #STEM #Industry4.0 #EngEducation
```

**LinkedIn:**
```
I'm pleased to announce the public release of the ARC (Automation-Robotics-Control) 
Framework, a comprehensive evidence-based system for integrating industrial robotics 
and adaptive control systems into STEM education.

This systematic review of 52 empirical studies (2019-2025) provides:
• Five-level technology complexity taxonomy
• Competency progression model from novice to expert
• Meta-analysis showing large positive effects (g = 0.783)
• Cost-effectiveness analysis identifying optimal implementation strategies
• Complete code, data, and documentation for full reproducibility

The framework addresses the critical skills gap in Industry 4.0 automation, 
providing educators with evidence-based guidance for technology selection and 
curriculum design.

Repository: https://github.com/ClaudioUrrea/ARC-Framework
Data: https://doi.org/10.6084/m9.figshare.31053583
Paper: Applied Sciences (MDPI), 2026

#EngineeringEducation #IndustrialRobotics #STEM #Industry40 #AdaptiveControl
```

## Maintenance and Updates

### Regular Maintenance
- [ ] Review issues weekly
- [ ] Respond to pull requests within 2 weeks
- [ ] Update dependencies quarterly
- [ ] Check for broken links monthly
- [ ] Update CHANGELOG.md with each release

### Version Updates
When making updates:
```bash
# Make changes to code/documentation
git add .
git commit -m "Update: Description of changes"

# Update version in files:
# - CHANGELOG.md
# - CITATION.cff
# - README.md

# Tag new version
git tag -a v1.0.1 -m "Version 1.0.1: Bug fixes"
git push origin main --tags

# Create GitHub Release (see Step 6)
```

## Troubleshooting

### Push Rejected
```bash
# If push is rejected due to remote changes
git pull --rebase origin main
git push origin main
```

### Large Files
If you have files >100MB:
- Use Git LFS: `git lfs install`
- Or host on FigShare and link in README

### Access Issues
- Verify SSH keys: `ssh -T git@github.com`
- Or use HTTPS: `git remote set-url origin https://github.com/ClaudioUrrea/ARC-Framework.git`

## GitHub Best Practices

1. **Commit Often:** Small, focused commits
2. **Descriptive Messages:** Clear commit messages
3. **Branch Protection:** Protect main branch
4. **Code Review:** Review pull requests thoroughly
5. **Documentation:** Keep README updated
6. **Changelog:** Document all changes
7. **Issues:** Use issue tracker actively
8. **Tags:** Use semantic versioning
9. **Releases:** Create releases for major versions
10. **Community:** Respond to issues and questions

## Support

For GitHub-specific questions:
- **GitHub Docs:** https://docs.github.com
- **GitHub Support:** https://support.github.com
- **Repository Issues:** https://github.com/ClaudioUrrea/ARC-Framework/issues

For framework questions:
- **Email:** claudio.urrea@usach.cl
- **GitHub Issues:** Create new issue

## Verification Checklist

After setup, verify:
- [ ] Repository is public and accessible
- [ ] README displays correctly with all badges
- [ ] All files are present and organized
- [ ] License file is visible
- [ ] Release v1.0.0 is created
- [ ] Topics/tags are added
- [ ] Repository description is accurate
- [ ] FigShare link works
- [ ] Code can be cloned successfully
- [ ] Scripts execute without errors
- [ ] Documentation is readable
- [ ] CITATION.cff is valid
- [ ] GitHub Pages set up (if applicable)
- [ ] Issue templates are available

## Next Steps

1. Monitor repository activity
2. Respond to issues and pull requests
3. Engage with users
4. Share on social media
5. Submit to software registries (e.g., JOSS)
6. Update institutional website
7. Include in CV/portfolio
8. Track citations and usage

---

Last updated: January 13, 2026
