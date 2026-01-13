# Changelog

All notable changes to the ARC Framework project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-13

### Added
- Initial public release of ARC Framework
- Complete systematic review analysis of 52 studies (2019-2025)
- Five-level technology complexity taxonomy
- Competency progression model (Novice → Expert)
- Meta-analysis with Hedges' g = 0.783 (95% CI: 0.719-0.847)
- Eight publication-quality figures (300 DPI):
  - Figure 1: PRISMA 2020 flow diagram
  - Figure 2: Technology complexity taxonomy pyramid
  - Figure 3: Cost-effectiveness analysis
  - Figure 4: HRC performance metrics (4-panel visualization)
  - Figure 5: Sensitivity analysis
  - Figure 6: Competency progression model
  - Figure 7: Meta-analysis forest plot
  - Figure 8: ARC Framework implementation pathway
- Python code for Figures 2-6 generation
- R code for Figure 7 forest plot
- Experimental datasets:
  - HRC_Aggregated_Fanuc.csv (1000 episodes)
  - Sensitivity_Results_Fanuc_Shaded.csv (12 configurations)
- Comprehensive documentation:
  - README.md (main documentation)
  - INSTALL.md (installation guide)
  - REPRODUCE.md (reproduction instructions)
  - README_DATA.md (data documentation)
  - CONTRIBUTING.md (contribution guidelines)
  - LICENSE (CC BY 4.0)
  - CITATION.cff (standardized citation)
- Automation scripts:
  - generate_all_figures.sh (Bash)
  - generate_all_figures.ps1 (PowerShell)
- Dependency specifications:
  - requirements.txt (pip)
  - environment.yml (conda)
- FigShare repository: https://doi.org/10.6084/m9.figshare.31053583
- GitHub repository: https://github.com/ClaudioUrrea/ARC-Framework
- Complete paper PDF (Applied Sciences, MDPI, 2026)

### Documentation
- Detailed installation instructions for Windows, macOS, and Linux
- Step-by-step reproduction guide for all figures
- Comprehensive data documentation with statistical summaries
- Technology selection decision-support tools
- Pedagogical strategy recommendations by competency level
- Cost-effectiveness analysis methodology

### Research Contributions
- First comprehensive framework for industrial robotics education
- Evidence-based technology progression pathways
- Quantification of technology complexity effects (26% improvement industrial vs. educational)
- Optimal cost-effectiveness model identified (remote labs: $45/student)
- Integration of competency development with technology selection
- Systematic review following PRISMA 2020 guidelines
- Random-effects meta-analysis with heterogeneity assessment
- Validation with Fanuc M-20iA industrial manipulator data

## [Unreleased]

### Planned for v1.1.0
- Additional supplementary materials:
  - Assessment rubrics (XLSX format)
  - Technology selection decision tool (interactive)
  - Implementation checklist templates
- Extended examples:
  - Curriculum integration case studies
  - Course syllabi examples
  - Laboratory exercise templates
- Video tutorials:
  - Installation walkthrough
  - Figure generation demonstration
  - Framework application examples
- Interactive visualizations:
  - Web-based technology selector
  - Cost calculator tool
  - Competency self-assessment
- Multilingual support:
  - Spanish translation (README, documentation)
  - Portuguese translation (selected materials)

### Under Consideration
- Jupyter notebooks with interactive analyses
- Additional datasets from different robot platforms
- Extension to Industry 5.0 technologies
- Integration with learning management systems
- Automated report generation tools
- Machine learning model for technology recommendation
- Collaboration network visualization
- Citation tracking and impact metrics dashboard

## Version History

### How Versions Are Numbered

Given a version number MAJOR.MINOR.PATCH:
- **MAJOR**: Incompatible changes to framework structure
- **MINOR**: Backward-compatible functionality additions
- **PATCH**: Backward-compatible bug fixes

### Release Schedule

- Major versions: Annually (January)
- Minor versions: Quarterly as needed
- Patch versions: As needed for bug fixes

### Support Policy

- **Current version (1.0.x)**: Full support
- **Previous major version**: Security updates only for 1 year
- **Older versions**: No support (upgrade recommended)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Reporting bugs
- Suggesting features
- Submitting pull requests
- Development workflow

## Acknowledgments

### Version 1.0.0 Contributors
- **Claudio Urrea** (University of Santiago of Chile) - Principal Investigator
  - Conceptualization, methodology, formal analysis, investigation, writing
  - Software development, data curation, visualization
  - Project administration, funding acquisition

### Institutional Support
- Faculty of Engineering, University of Santiago of Chile

### Acknowledgments
- Anonymous peer reviewers for Applied Sciences
- Research participants in human-robot collaboration studies
- Open-source software communities (Python, R, matplotlib, metafor)

## Citation

If you use ARC Framework in your research, please cite:

```bibtex
@article{urrea2026arc,
  title={Industrial Robotics and Adaptive Control Systems in STEM Education: 
         Systematic Review of Technology Transfer from Industry to Classroom 
         and Competency Development Framework},
  author={Urrea, Claudio},
  journal={Applied Sciences},
  year={2026},
  volume={16},
  number={2},
  doi={10.3390/appXXXXXXXX},
  publisher={MDPI}
}
```

## License

This project is licensed under CC BY 4.0 - see [LICENSE](LICENSE) file.

## Contact

**Maintainer:** Claudio Urrea  
**Email:** claudio.urrea@usach.cl  
**Institution:** University of Santiago of Chile  
**GitHub:** https://github.com/ClaudioUrrea/ARC-Framework  
**ORCID:** 00000-0001-7197-8928

---

For complete version history and detailed changes, see:
- [GitHub Releases](https://github.com/ClaudioUrrea/ARC-Framework/releases)
- [GitHub Commits](https://github.com/ClaudioUrrea/ARC-Framework/commits)
