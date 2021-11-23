# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test-kieker",
    version="0.0.1",
    author="ME",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #package_dir={"": "monitoring", "tools": "tools"},
    packages=setuptools.find_packages(include=["monitoring", "monitoring.", "tools", "tools."]),
    python_requires=">=3.6",
)
