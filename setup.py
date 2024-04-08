from setuptools import setup, find_packages

NAME = "easydebugger"
VERSION = '1.0.1'
DESCRIPTION = 'A clean Python debugging tool'
LONG_DESCRIPTION = 'A clean Python debugging tool. Documentation at https://github.com/Blob2763/easydebugger'

# Setting up
setup(
    name=NAME,
    version=VERSION,
    author="blob2763",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(include=["easydebugger"]),
    install_requires=[],
    keywords=['python', 'debugger']
)