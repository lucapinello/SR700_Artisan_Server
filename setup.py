# -*- coding: utf-8 -*-
# Copyright (c) 2018 Luca Pinello
# Made available under the MIT license.


#This is based on: https://github.com/Roastero/freshroastsr700

import os
from setuptools import setup
from setuptools import find_packages
import glob

here = os.path.abspath(os.path.dirname(__file__))

scripts=glob.glob('cmds/*')

setup(
    name='SR700-Artisan-PDServer-Phidget',
    version=0.1,
    description='Extension of the SR700-Artisan-PDServer (https://github.com/infinigrove/SR700-Artisan-PDServer) to use with the Phidget',
    url='https://github.com/lucapinello/freshroastsr700_phidget',
    author='Luca Pinello',
    license='GPLv3',
    packages=find_packages(),
    install_requires=['freshroastsr700_phidget>=0.2','Pyro4','datetime'],
    scripts=scripts,
)
