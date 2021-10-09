from setuptools import setup, find_packages

with open("requirements.txt") as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name='kantele', 
    version='0.1',
    install_requires=REQUIREMENTS,
    python_requires=">=3.8",
    packages=find_packages()
)