#!/bin/bash

# go to the home directory of the api project
cd $(dirname $(readlink -f $0))

source venv/bin/activate

uvicorn src.hello_world_api:app --reload
