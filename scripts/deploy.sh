#!/bin/bash

git clone --recurse-submodules https://github.com/nomic-ai/gpt4all
cd /app/gpt4all/gpt4all-backend/
mkdir build
cd /app/gpt4all/gpt4all-backend/build
cmake ..
cmake --build . --parallel

cd /app/gpt4all/gpt4all-bindings/python
pip3 install -e .

cd /app
pipenv install

