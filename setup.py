#!/usr/bin/env python
# flake8: noqa

from setuptools import setup, find_packages

setup(
    name = "bit-notify",
    version = "0.1.2",
    packages = find_packages(),

    author = "Hunter Thompson",
    author_email = "thompson.grey.hunter@gmail.com",
    description = "Bittrex SMS Notifier",
    license = "MIT",
    keywords = "sms bittrex",
    url = "https://github.com/hthompson6/bit-notifier",

    long_description = open('README.md').read(),
    classifiers = [
      'Programming Language :: Python',
      'Programming Language :: Python :: 2.7',
      'Operating System :: OS Independent',
      'License :: OSI Approved :: MIT License',
      'Development Status :: 3 - Alpha',
    ],
    install_requires=['twilio>=6.4.2','bit-bind>=0.1.0']
)
