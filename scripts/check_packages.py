#!/usr/bin/env python3

import importlib

requirements = [
    "jupyter",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn"
]

errors = []
for requirement in requirements:
    try:
        importlib.import_module(requirement)
    except ImportError as e:
        errors.append(requirement)

if len(errors) > 0:
    print("Could not import the required package(s):")
    print("-", "\n- ".join(errors))
    print("Please ask one of our helpers to show you how to install them")
else:
    print("All of the packages are installed!")
    print("You're good to go")
