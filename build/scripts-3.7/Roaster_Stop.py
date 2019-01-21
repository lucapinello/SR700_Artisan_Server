#!python
# -*- coding: utf-8 -*-
# SR700-Artisan-PDServer, released under GPLv3
# Roaster Run Recipe

import Pyro4

roast_control = Pyro4.Proxy("PYRONAME:roaster.sr700")
roast_control.stop()
