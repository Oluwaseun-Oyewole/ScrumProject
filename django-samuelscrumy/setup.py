from setuptools import setup, find_packages
from os import path
from io import open

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

version = '3.2.1'

setup(
    name='django-samuelscrumy',
    version=version,
    packages=find_packages(),
    license='BSD License,',
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    zip_safe=False,
    author='Samuel Oyewole',
    author_email='findseunoyewole@gmail.com',
    description='Django-samuelscrumy helps you create goals and goal status with web based authentication and authorization',
    url='http://54.90.243.31:8000/samuelscrumy',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython"
    ]
)