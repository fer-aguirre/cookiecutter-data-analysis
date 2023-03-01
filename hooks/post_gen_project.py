""" Script that runs after the project generation"""
import os

MESSAGE_COLOR = '\033[92m'
RESET_ALL = "\x1b[0m"

# Install pipenv for Linux
os.system("pip install pipenv")

# Install virtual environment and synchronize packages
print(f"{MESSAGE_COLOR}Creating virtual environment...{RESET_ALL}")
os.system("pipenv install")
os.system("pipenv sync")
os.system("pipenv update setuptools")
os.system("python3 setup.py install")
os.system("pipenv install -e .")

# Initialize git
print(f"{MESSAGE_COLOR}Initializing a git repository...{RESET_ALL}")
os.system("git init && git add . && git commit -m 'Initial commit' && git branch -M main")

# Final message
print(f"{MESSAGE_COLOR}Your template for {{cookiecutter.project_name}} is ready!{RESET_ALL}")