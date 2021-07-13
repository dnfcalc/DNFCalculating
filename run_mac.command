#!/bin/bash

proj_path=$(cd $(dirname $BASH_SOURCE) && pwd) || {
    echo "Get program path failed" >&2
    exit 1
}

cd $proj_path && python3.8 main.py

