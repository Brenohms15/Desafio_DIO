from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Fmath",
    version="0.0.1",
    author="Breno Henrique",
    author_email="brenohms99@gmail.com",
    description="Fullstack Developer",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Brenohms15/Desafio_DIO.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)