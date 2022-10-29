from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    requirement_list:List[str] = []
    return requirement_list


setup(
    name="sensor",
    version="0.0.1",
    author = "Suraj",
    author_email="suraj@ineuron.ai",
    packages=find_packages(),
    install_requires = []

)