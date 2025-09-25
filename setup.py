from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as req_obj:
        req=req_obj.readlines()
        requirements=[i.replace("\n","") for i in req]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements

setup(
    name='End to end ML project',
    version='0.0.1',
    author='Kunal S',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)