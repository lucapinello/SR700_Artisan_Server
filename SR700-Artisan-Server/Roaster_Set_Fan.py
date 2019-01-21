#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SR700-Artisan-PDServer, released under GPLv3
# Roaster Set Fan Speed
import Pyro4
import sys

new_roaster_speed = sys.argv[1]

roast_control = Pyro4.Proxy("PYRONAME:roaster.sr700")
if int(new_roaster_speed) < 1:
    new_roaster_speed = 1
if int(new_roaster_speed) > 9:
    new_roaster_speed = 9
if int(new_roaster_speed) > 0 and int(new_roaster_speed) <10:
    roast_control.set_fan_speed(new_roaster_speed)
