#!/bin/bash
#python -m coverage run -m unittest --verbose
coverage run unittest
coverage combine
coverage report -m