#!bin/bash

poetry shell
poetry export --without-hashes --format=requirements.txt > requirements.txt

cdk deploy