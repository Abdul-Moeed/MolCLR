from setuptools import setup, find_packages

setup(
    name='molclr',
    version='0.1',
    description='MolClr',
    packages=find_packages(include=['molclr', 'molclr.*']),
    setup_requires=['pytest-runner', 'flake8'],
    tests_require=['pytest']
)
