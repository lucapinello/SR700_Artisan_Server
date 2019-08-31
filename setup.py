# -*- coding: utf-8 -*-
# Copyright (c) 2018 Luca Pinello
# Made available under the MIT license.


#This is based on: https://github.com/Roastero/freshroastsr700

import os
from setuptools import setup
from setuptools import find_packages
import glob

here = os.path.abspath(os.path.dirname(__file__))

script_names=list(map(os.path.basename,glob.glob('SR700_Artisan_Server/*.py')))
entry_points_list=['{0}={1}.{0}:main'.format(name.split('.')[0],'SR700_Artisan_Server') for name in script_names]

setup(
    name='SR700_Artisan_Server',
    version=1.7,
    packages = ["SR700_Artisan_Server"],
    package_dir={'SR700_Artisan_Server': 'SR700_Artisan_Server'},
    include_package_data = True,
    description='Extension of the SR700-Artisan-PDServer (https://github.com/infinigrove/SR700-Artisan-PDServer) to use with the Phidget',
    url='https://github.com/lucapinello/SR700-Artisan-Server',
    author='Luca Pinello',
    license='GPLv3',
    install_requires=['freshroastsr700_phidget>=1.1','Pyro4','datetime'],
    entry_points = {"console_scripts": entry_points_list},
)
