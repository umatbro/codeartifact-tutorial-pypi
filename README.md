# CodeArtifact with pypi tutorial

This tutorial explains how to create a Python package using [Poetry](https://python-poetry.org/) and how to publish it to the repository
created in [AWS CodeArtifact](https://aws.amazon.com/codeartifact/).

## Setup

Clone the repository:
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

## Create CodeArtifact repository

This part of the tutorial assumes that you already have [created your AWS account](https://aws.amazon.com/free).

Login to your account and navigate to [CodeArtifact](console.aws.amazon.com/codesuite/codeartifact/start).

Click **Create repository** button and fill in the form. In this example we will use `hello-repo` as a repository name.

![Create repository](img/create-repository.png)


<!-- TODO check this -->
Note that you should select `pypi-store` in **Public upstream repositories** if you also want to use
public packages for pypi.
By default it is not enabled and only packages uploaded manually will be available.
<!-- ENDTODO -->

Click **Next** and select **This AWS account** and type in a new domain name, in this tutorial we go with `hello`.

![Select domain](img/select-domain.png)

In the last step confirm your setup by clicking **Create repository**.

## Config poetry to use `hello` repository
