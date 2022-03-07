from setuptools import setup, find_packages

with open("README.md", "r") as file:
    page_description = file.read()

with open("requirements.txt", "r") as file:
    requirements = file.read().splitlines()

setup(
    name='mypackage',
    version='0.0.1',
    author='José Alberto'
    packages=find_packages(),
    url='https://github.com/dev-JoseAlberto/Image-Processing',
    install_requires=[
        'requests',
        'importlib; python_version == ">=3.8"',
    ],
)