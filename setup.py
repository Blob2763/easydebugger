from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'A clean Python debugging tool'
LONG_DESCRIPTION = 'A clean Python debugging tool. Documentation coming soon...'

# Setting up
setup(
    name="easydebugger",
    version=VERSION,
    author="blob2763",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(include=["easydebugger"]),
    install_requires=[],
    keywords=['python', 'debugger']
)