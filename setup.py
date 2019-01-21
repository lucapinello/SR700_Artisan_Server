# -*- coding: utf-8 -*-
# Copyright (c) 2018 Luca Pinello
# Made available under the MIT license.


#This is based on: https://github.com/Roastero/freshroastsr700

import os
from setuptools import setup
from setuptools import find_packages
import glob

here = os.path.abspath(os.path.dirname(__file__))

scripts=glob.glob('SR700-Artisan-Server/*.py')

setup(
    name='SR700-Artisan-Server',
    version=0.1,
    packages = ["SR700-Artisan-Server"],
    package_dir={'SR700-Artisan-Server': '.'},
    include_package_data = True,
    description='Extension of the SR700-Artisan-PDServer (https://github.com/infinigrove/SR700-Artisan-PDServer) to use with the Phidget',
    url='https://github.com/lucapinello/SR700-Artisan-Server',
    author='Luca Pinello',
    license='GPLv3',
    install_requires=['freshroastsr700_phidget>=0.3','Pyro4','datetime'],
    scripts=scripts,
)
