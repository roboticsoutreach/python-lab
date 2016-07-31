# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='simulator',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0',

    description='SR Simulator',

    # The project's main homepage.
    url='https://github.com/srobo-southampton/python-lab',

    # Author details
    author='Student Robotics',
    author_email='abarrett-sprot@studentrobotics.org',

    # Choose your license
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    install_requires=[
    ],

    package_data={'': ['*.png','*.yaml']},
    include_package_data=True,

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

)