#!/bin/bash
#python -m coverage run -m unittest --verbose
python -m coverage combine
python -m coverage report -m