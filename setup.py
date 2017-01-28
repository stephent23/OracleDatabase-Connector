from setuptools import setup
import re

version = ''

with open('OracleDatabase/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Unable to find version information.')

print 'VER:', version

with open('README.md') as f:
    readme = f.read()

packages = ['OracleDatabase']

setup(
    name='OracleDatabase',
    version=version,
    long_description=readme,
    packages=packages,
    url='',
    license='',
    author='Stephen Tate',
    author_email='stephen@sjtate.co.uk',
    description='Python Oracle Database Connector'
)