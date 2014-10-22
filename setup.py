#
# setup.py
#

import sys

from setuptools import setup, find_packages

install_requires = ['growler', 'asyncio_mongo']

long_description = """
Growler middleware implementing sesison storage using a MongoDB database backend.

To use, import this module, create your app, connect to a database, and tell the
app to 'use' a MongoSession object created with your settings.

import growler
import GrowlerMongoSession
import asyncio_mongo

db = asyncio_mongo.createConnection(...)

app = growler.App(...)

...

app.use(GrowlerMongoSession(db, session_config))

"""


setup(
  name= "GrowlerMongoSession",
  version= "0.0.1",
  author= "Andrew Kubera",
  license= "Apache v2.0",
  url= "https://github.com/pyGrowler/MongoSession",
  author_email= "andrew.kubera@gmail.com",
  description= "Growler middleware implementing sesison storage using a MongoDB database backend.",
  long_description= long_description,
  classifiers= [
    "Development Status :: 2 - Pre-Alpha",
    # "Framework :: Growler",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Database",
    "Natural Language :: English"
  ],
  install_requires = install_requires,
  packages= find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
)
