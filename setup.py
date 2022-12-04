from distutils.core import setup
from setuptools import find_packages

setup(
    name='snowflake',
    version='1.0.2',
    author='Florian Mehrkens',
    author_email='flo.mehrkens@fau.de',
    packages=find_packages(),
    install_requires=['numpy', 'turtles'],
)
