#!/bin/bash
#python -m coverage run -m unittest --verbose
coverage run -m unittest
coverage combine
coverage report -m