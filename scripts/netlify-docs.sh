#!/usr/bin/env bash

# install pipenv
pip install poetry
# install all dev dependencies (including mkdocs)
poetry install
# build mkdocs site
mkdocs build
