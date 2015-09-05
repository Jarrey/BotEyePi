#!/bin/bash
rm bin -f -r
rm *.pyc -f
python build.py
mkdir ./bin

cp setting.py ./bin/
mv *.pyc ./bin/
