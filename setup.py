from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here,"README.md"),encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='tinyperceptron',
    version='1.0.0',
    author='zidea',
    author_email='zidea2015@163.com',
    description='perceptron agent ',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="perceptron of agent",
    url="https://github.com/zideajang/tinyperceptron",
    # install_requires=requirements,
    packages=find_packages(exclude=["examples","docs"]),
    python_requires=">=3.9"
)