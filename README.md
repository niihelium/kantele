## Running

To run example project first you need to make sure to install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) (or virtualenv manager of your choice).

Create new virtual environment with Python version >= 3.8:
```bash
mkvirtualenv kantele --python=/usr/bin/python3
```
Activate new environment:
```bash
workon kantele
```
Install current package in editable state:
```bash
pip install -e .
```

[//]: # (Just memo)
[//]: # (Python -m pip install --upgrade pip)