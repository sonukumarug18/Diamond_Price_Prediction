from setuptools import find_packages, setup # setup used fr versioning and find_packg find all the pacake
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:    #opening requirements.txt file
        requirements = file_obj.readlines()  # read each line and save in variable
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements



setup(
    name='dimond_price_prediction',
    version='0.0.1',
    author= 'Sonu',
    author_email='sonukumarug18@gmail.com',
    install_requires = get_requirements('requirements.txt'),     #['pandas','numpy']
    packages=find_packages()  #inside modules there are submodules,it goes and find that 



)