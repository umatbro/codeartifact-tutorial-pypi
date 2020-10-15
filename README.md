# CodeArtifact with pypi tutorial

This tutorial explains how to create a Python package using Poetry and how to publish it to the repository 
created in AWS CodeArtifact.

## Setup

Clone repository:
```
git clone git@github.com:umatbro/codeartifact-tutorial-pypi.git
cd codeartifact-tutorial-pypi
```

Setup virtualenv

```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $
```

Install poetry and project dependencies
```
pip install poetry
poetry install
```
