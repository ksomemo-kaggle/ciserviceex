import re
from setuptools import (
    setup,
    find_packages
)

PACKAGES_ROOT = '.'

def find_version():
    with open('ciserviceex/version.py') as f:
        version_regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
        version_match = re.search(version_regex, f.read(), re.M)
        if version_match:
            version = version_match.group(1)
        else:
            raise RuntimeError("Unable to find version string.")
    return version


def long_description():
    with open('README.rst') as f:
        return f.read()

setup(
    name='ciserviceex',
    description='continuous integration service exercise',
    long_description=long_description(),
    author='ksomemo',
    url='https://github.com/ksomemo/ciserviceex',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='package example',
    license='MIT',
    version=find_version(),
    packages=find_packages(PACKAGES_ROOT)
)

