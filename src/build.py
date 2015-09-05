#!/usr/bin/python
import py_compile as c
import os

files = ['run.py', 'bar.py', 'capturer.py', 'logger.py', 'power_monitor.py']

for f in files:
	c.compile(f)
