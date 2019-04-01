# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

NAME = "groupdocs-classification-cloud"
VERSION = "19.3.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]
TEST_REQUIRES = ["asposestoragecloud >= 1.0.6", "groupdocsclassificationcloud >= 1.0.0"]

setup(
    name=NAME,
    version=VERSION,
    description="GroupDocs.Classification Cloud API References",
    author="GroupDocs Classification",
    url="https://github.com/groupdocs-classification-cloud/groupdocs-classification-cloud-python",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Office Suites',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=["groupdocs", "python", "groupdocs cloud", "classification", "documents classification", "iab2", "taxonomy"],
    install_requires=REQUIRES,
    tests_require=TEST_REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""
    This repository contains GroupDocs.Classification Cloud SDK for Python source code. This SDK allows you to classify raw text and documents with IAB-2 and Documents taxonomies in your Python applications quickly and easily, with zero initial cost.
    """
)
