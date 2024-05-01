from setuptools import find_packages, setup
from typing import List

hyphen_extra='-e .'
def get_lib(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hyphen_extra in requirements:
            requirements.remove(hyphen_extra)
    return requirements


setup(

name="Guided ML project",
version="0.0.1",
author="Swayam Jha",
author_email="jha.swayam2004@gmail.com",
packages=find_packages(),
install_requires=get_lib('requirements.txt')




)