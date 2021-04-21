#!/usr/bin/env python
from setuptools import setup  # type: ignore


setup(
    name="winsum",
    version="0.1",
    description="NTLM checksums from the command line",
    author="Clin",
    author_email="yoloClin@github.com",
    scripts=["bin/ntlm"],
    url="",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    license="LICENSE.txt",
)
