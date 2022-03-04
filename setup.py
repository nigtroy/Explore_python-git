from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests']) ,
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requirements=['numpy'],
    author='Samuel Gyimah  ',
    author_email='gsamuel171@gmail.com'
)