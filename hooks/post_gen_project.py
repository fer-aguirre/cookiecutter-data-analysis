""" Script that runs after the project generation"""
import os

MESSAGE_COLOR = '\033[92m'
RESET_ALL = "\x1b[0m"

# Install pipenv for Linux
os.system("pipx install poetry")

# Install virtual environment and synchronize packages
print(f"{MESSAGE_COLOR}Creating virtual environment...{RESET_ALL}")
os.system("poetry env use python3.8")
os.system("poetry install")

# Initialize git
print(f"{MESSAGE_COLOR}Initializing a git repository...{RESET_ALL}")
os.system("git init && git add . && git commit -m 'Initial commit' && git branch -M main")

# Final message
print(f"{MESSAGE_COLOR}Your template for {{cookiecutter.project_name}} is ready!{RESET_ALL}")