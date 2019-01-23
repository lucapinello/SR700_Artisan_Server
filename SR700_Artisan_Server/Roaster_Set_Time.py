#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SR700-Artisan-PDServer, released under GPLv3
# Roaster Set Time
import Pyro4
import sys

def main():
    new_roaster_time = sys.argv[1]

    roast_control = Pyro4.Proxy("PYRONAME:roaster.sr700")
    if int(new_roaster_time) > 0 and int(new_roaster_time) <=1500:
        roast_control.set_time(new_roaster_time)

if __name__ == '__main__':
    main()
