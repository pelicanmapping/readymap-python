import os
from setuptools import setup, find_packages

version = __import__('readymap').__version__

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='readymap-python',
    version=version,
    author='Jason Beverage',
    author_email="jasonbeverage@pelicanmapping.com",
    description=('Python bindings for ReadyMap'),
    long_description=README,
    packages=find_packages(),
    install_requires=['requests>=2.4.1',]
)