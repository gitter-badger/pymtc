#!/usr/bin/python


from setuptools import setup, find_packages


setup(
    name = "pymtc",
    version = "1.1",
    author = "Vitold Sedyshev",
    author_email = "vit1251@gmail.com",
    description = "Make Test Client",
    keywords = "make test email anonymous temporary temp tmp mailbox inbox",
    package_dir = {'': 'src'},
    packages = find_packages('src'),
    classifiers = [
        "Development Status :: 3 - Alpha",
    ],
)
