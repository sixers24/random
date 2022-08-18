from setuptools import setup, find_packages
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

 

setup(
    name='pyBC',
    version= "1.0.0",
    description=('pyBC'),
    long_description="PyBC",
 
    license='MPL-2.0',
    packages=find_packages(),
 
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'],
    )
