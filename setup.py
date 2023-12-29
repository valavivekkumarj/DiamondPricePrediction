from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path):
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    return requirements


setup(
    name="diamondpriceprediction",
    author="vibvek vala",
    author_email="valavivek2019@gmail.com",
    version="0.0.1",
    install_requires=get_requirements("requirement.txt"),
    packages=find_packages(),
)
