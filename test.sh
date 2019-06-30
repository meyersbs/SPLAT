#!/bin/sh

PYTHONPATH=./splat/ coverage run --source=splat -m unittest discover -s test/
coverage report -m --omit=splat/logger.py


