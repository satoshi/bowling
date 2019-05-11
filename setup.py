from setuptools import setup, find_packages

setup(
    name='bowling',
    version='0.0.3',
    description='bowling score calculator',
    url='https://github.com/satoshi/bowling',
    author='Satoshi Yagi',
    author_email='satoshi.yagi@yahoo.com',
    license='MIT',
    long_description='bowling score calculator with refactoring',
    packages=find_packages(exclude=['tests']),
)
