from setuptools import setup, find_packages

setup(
    name='{{cookiecutter.project_name}}',
    version='0.1.0',
    author='{{cookiecutter.project_author}}',
    description='{{cookiecutter.project_description}}',
    python_requires='>=3',
    license='{{cookiecutter.project_license}}',
    packages=find_packages(),
)