#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# We use calendar versioning
version = "2022.07.10"

with open("README.rst") as readme_file:
    long_description = readme_file.read()

setup(
    name="cookiecutter-django",
    version=version,
    description=(
        "A Cookiecutter template for creating production-ready "
        "Django projects quickly. Deployable to OpenShift 4 using Helm Charts."
    ),
    long_description=long_description,
    author="Krishna Madhavan",
    author_email="madhavank@who.int",
    url="https://github.com/krishnamadhavan/cookiecutter-django-helm-openshift4",
    packages=[],
    license="BSD",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Django :: 3.2",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
    ],
    keywords=(
        "cookiecutter, Python, projects, project templates, django, "
        "skeleton, scaffolding, project directory, setup.py, "
        "helm, kubernetes, openshift"
    ),
)
