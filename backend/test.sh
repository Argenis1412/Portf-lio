#!/bin/bash
# Script to run tests on Linux/Mac using the virtual environment
"./.venv/bin/python" -m pytest "$@"
