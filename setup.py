from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements mentioned in the requirements.txt file
    """
    requirement_list = []
    try:
        with open ('requirements.txt', 'r') as file:
            lines= file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError as e:
        print(f"requirements.txt file not found: {e}")

    return requirement_list


setup(
    name='Setup Security Mloops Project',
    version='0.0.1',
    author='abdullah',
    author_email='abdullahizaq321@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)