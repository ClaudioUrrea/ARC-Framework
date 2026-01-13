# Contributing to ARC Framework

Thank you for your interest in contributing to the ARC Framework! This document provides guidelines for contributing to this repository.

## Types of Contributions

We welcome several types of contributions:

### 1. Bug Reports
If you find a bug in the code or documentation:
- Check existing issues to avoid duplicates
- Create a new issue with:
  - Clear description of the problem
  - Steps to reproduce
  - Expected vs. actual behavior
  - Your environment (OS, Python version, package versions)
  - Error messages or screenshots

### 2. Feature Requests
To suggest new features:
- Describe the feature and its benefits
- Explain use cases
- Consider implementation complexity
- Discuss alternatives you've considered

### 3. Code Contributions
For code improvements:
- Fork the repository
- Create a feature branch
- Make your changes
- Test thoroughly
- Submit a pull request

### 4. Documentation Improvements
Documentation contributions are valuable:
- Fix typos or unclear explanations
- Add missing documentation
- Improve code comments
- Create tutorials or examples

### 5. Data Contributions
If you have conducted related research:
- Additional experimental data
- Validation studies
- Replications in different contexts
- Extension to new technology platforms

## Development Setup

1. **Fork and Clone**
```bash
git clone https://github.com/YOUR-USERNAME/ARC-Framework.git
cd ARC-Framework
```

2. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
pip install pytest pytest-cov black flake8  # Development dependencies
```

4. **Create Feature Branch**
```bash
git checkout -b feature/your-feature-name
```

## Coding Standards

### Python Code
- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and modular
- Maximum line length: 88 characters (Black default)

**Example:**
```python
def calculate_effect_size(mean1: float, mean2: float, sd_pooled: float) -> float:
    """
    Calculate Cohen's d effect size.
    
    Args:
        mean1: Mean of group 1
        mean2: Mean of group 2
        sd_pooled: Pooled standard deviation
        
    Returns:
        Effect size (Cohen's d)
    """
    return (mean1 - mean2) / sd_pooled
```

### R Code
- Use snake_case for variable names
- Add comments for complex operations
- Follow tidyverse style guide
- Use meaningful variable names

### Documentation
- Use Markdown for all documentation
- Keep lines under 100 characters for readability
- Include code examples where appropriate
- Link to related resources

## Testing

### Running Tests
```bash
# Python tests (when implemented)
pytest tests/

# With coverage
pytest --cov=code tests/
```

### Adding Tests
Create tests for new features:
```python
def test_effect_size_calculation():
    """Test effect size calculation with known values."""
    result = calculate_effect_size(10, 8, 2)
    assert abs(result - 1.0) < 0.001
```

## Pull Request Process

1. **Update Documentation**
   - Update README if needed
   - Add docstrings/comments
   - Update CHANGELOG.md

2. **Test Your Changes**
   - Run all tests
   - Generate all figures to ensure no breaking changes
   - Test in clean environment

3. **Commit Messages**
   - Use clear, descriptive messages
   - Start with verb in present tense
   - Reference issue numbers if applicable

**Good commit messages:**
```
Add sensitivity analysis for learning rate parameter
Fix bug in Figure 4 colorbar scaling
Update installation instructions for Windows
Refactor data loading to handle missing files
```

4. **Submit Pull Request**
   - Provide clear description
   - Reference related issues
   - Explain changes made
   - Include screenshots if relevant

## Code Review Process

All submissions require review:
1. Automated checks must pass
2. Code reviewed by maintainer
3. Documentation reviewed
4. Tests verified
5. Changes approved and merged

## Reporting Security Issues

**Do not create public issues for security vulnerabilities.**

Instead, email the maintainer directly:
- Email: claudio.urrea@usach.cl
- Subject: "ARC Framework Security Issue"
- Provide detailed description

We'll respond within 48 hours to acknowledge receipt.

## Communication

### Preferred Channels
- **GitHub Issues:** Bug reports, feature requests
- **Pull Requests:** Code contributions
- **Email:** Security issues, collaboration inquiries

### Response Times
- Issues acknowledged within 1 week
- Pull requests reviewed within 2 weeks
- Security issues addressed within 48 hours

## Attribution

Contributors will be acknowledged in:
- README.md (Contributors section)
- CHANGELOG.md (version notes)
- Academic papers citing significant contributions

## License

By contributing, you agree that your contributions will be licensed under the CC BY 4.0 license.

## Questions?

If you have questions about contributing:
- Create a GitHub issue with "Question" label
- Email: claudio.urrea@usach.cl

## Acknowledgments

Thank you for contributing to advancing engineering education research!

---

**First-time contributors are especially welcome.** Don't hesitate to ask questions or request help.
