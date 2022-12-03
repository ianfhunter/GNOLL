import sys

from setuptools import setup

sys.argv.extend(["--plat-name", "manylinux2014"])
setup()
