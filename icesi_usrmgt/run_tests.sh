#!/usr/bin/env bash
set -e 

. ~/.virtualenvs/usermgt/bin/activate

PYTHONPATH=. py.test --junitxml=python_tests.xml
