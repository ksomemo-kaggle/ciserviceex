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

setup(
    version=find_version(),
    packages=find_packages(PACKAGES_ROOT)
)

