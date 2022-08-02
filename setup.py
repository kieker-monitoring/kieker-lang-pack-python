# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kieker-monitoring-for-python",
    version="0.0.1",
    author="Serafim Simonov",
    author_email="stu126367@mail.uni-kiel.de",
    description="Implementation of kieker-monitoring for pyhton",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
   
    packages=setuptools.find_packages(
        where='kieker',
       # include =['monitoring', 'tools']
    ),
    package_dir={"": "kieker"}
    #python_requires=">=3.3",
)
