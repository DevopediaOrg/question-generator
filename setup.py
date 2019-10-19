import os
import versioneer
from setuptools import setup, find_packages
from distutils.sysconfig import get_python_lib

with open('requirements.txt') as f:
    required = f.read().splitlines()


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

setup(
    name="birbal",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url = "https://github.com/DevopediaOrg/question-generator",
    author="Devopedia",
    author_email="djpatra@gmail.com",
    description="Generate questions for Devopedia authors",
    packages=find_packages(exclude=['docs', 'tests*']),
    scripts=[],
    entry_points={
        'console_scripts': ['birbal=birbal.cli:main'],
    },
    install_requires=required,
    test_suite='nose.collector',
    tests_require=['mock~=1.0.1'],
    long_description=read('README.md'),
    extras_require={
        'docs': ['sphinx==1.5.1',
                 'sphinx-rtd-theme==0.1.9']
    }
)


test_suite='nose.collector',
tests_require=['coverage~=4.2', 'mock~=1.0.1'],
