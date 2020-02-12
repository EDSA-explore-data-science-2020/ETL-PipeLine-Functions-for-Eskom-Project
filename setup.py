from setuptools import setup, find_packages

setup(
    name='analysefunctions',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA analysefunctions python package',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas'],
    url='https://github.com/EDSA-explore-data-science-2020/Eskom-Analyse-Functions-',
    author='EDSA Team 10',
    author_email='nuri@gmail.com'
)
