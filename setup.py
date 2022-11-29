from setuptools import setup
from setuptools import find_packages

setup(
    name='snowflake',
    version='1.0.2',
    packages=find_packages(where="snowflake"),
    package_dir={"": "snowflake"},
    url='https://github.com/flomkns/DSSS_Ex05',
    license='Apache-2.0 license',
    author='Florian Mehrkens',
    author_email='flo.mehrkens@fau.de',
    install_requires=['numpy'],
    description='let it snow (Ex05)'
)
