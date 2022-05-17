# Tools for Python code formatting

The code in the learning resource is validated against the [PEP 8 style guide for Python code](https://peps.python.org/pep-0008/) by executing two automated code style tools—the automated code formatter [Black](https://github.com/psf/black) and the style guide checker [flake8](https://flake8.pycqa.org/en/latest/)—via [nbQA](https://github.com/nbQA-dev/nbQA). nbQA is a tool for notebook code style that allows you to run standard Python code formatters on a Jupyter notebook. 

This notebook installs and runs on all notebooks these code style tools.

# Install code quality tools
!pip install -U nbqa black flake8

# Run black on all notebooks in a folder 
!nbqa black ../notebooks/*.ipynb

# Run flake8 on all notebooks in a folder
!nbqa flake8 ../notebooks/*.ipynb