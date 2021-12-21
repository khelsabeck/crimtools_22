from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup (
    name='criminal_records_nc',
    version='0.0.1',
    description='Tools for running NC criminal records (for attys).',
    py_modules=[ 
        "defendant", "crime", "charge", "convictiondate",
    ],
    package_dir={'':'src'}, 
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/khelsabeck/crimtools_22.git",
    download_url="",
    author="Keith Helsabeck",
    author_email="admin@mylawdb.com",
)
