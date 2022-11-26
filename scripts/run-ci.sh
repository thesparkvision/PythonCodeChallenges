#!/bin/bash

echo "Running Linting Check =>"
./scripts/check-lint.sh

[ $? -ne 0 ] && {
    echo -e ""
    echo "Linting Status: Fail"
    echo "Action to take: Fix linting issues to proceed further"
    exit 1
}

echo "Running Test Coverage Check =>"
./scripts/check-coverage.sh