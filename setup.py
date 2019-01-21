# -*- coding: utf-8 -*-
# Copyright (c) 2018 Luca Pinello
# Made available under the MIT license.


#This is based on: https://github.com/Roastero/freshroastsr700

import os
from setuptools import setup
from setuptools import find_packages
import glob

here = os.path.abspath(os.path.dirname(__file__))

scripts=glob.glob('SR700-Artisan-PDServer-Phidget/*.py')

setup(
    name='SR700-Artisan-PDServer-Phidget',
    version=0.3,
    packages = ["SR700-Artisan-PDServer-Phidget"],
    package_dir={'SR700-Artisan-PDServer-Phidget': '.'},
    include_package_data = True,
    description='Extension of the SR700-Artisan-PDServer (https://github.com/infinigrove/SR700-Artisan-PDServer) to use with the Phidget',
    url='https://github.com/lucapinello/freshroastsr700_phidget',
    author='Luca Pinello',
    license='GPLv3',
    install_requires=['freshroastsr700_phidget>=0.3','Pyro4','datetime'],
    scripts=scripts,
)
