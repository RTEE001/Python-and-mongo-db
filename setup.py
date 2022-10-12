from setuptools import setup, find_packages

setup(name = "src", packages = find_packages(include=['mongo_connection', 'mongo_functions', 'tests']))