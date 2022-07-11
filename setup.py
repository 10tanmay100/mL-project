from setuptools import setup
from typing import List


def get_requirements_list()->List[str]:
    '''
    This function will going to return a list of strings which will contain name for all the libraries specified with requirements.txt
    '''
    with open("requirements.txt","r") as f:
        return f.readlines()

setup(
name="housing-predictor",
version="0.0.1",
author="Tanmay",
description="This is house price prdiction setup file",
packages=["housing"],
install_requires=get_requirements_list()
)




