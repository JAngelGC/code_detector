#!/bin/sh

# Resolve the directory of the script
PROJECTPATH=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

PYTHONPATH=$PROJECTPATH

echo "The current directory of the script is: $PROJECTPATH"

export PYTHONPATH
python3 -Wignore:"Python 3.6 is no longer supported":UserWarning "$@"