from setuptools import setup, find_packages


with open("requirements.txt") as f:
    requires = f.read().splitlines()

setup(
    name='iara',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'iara = src.main:cli',
        ],
    },
)