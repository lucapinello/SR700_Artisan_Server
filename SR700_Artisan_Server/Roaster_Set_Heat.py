#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SR700-Artisan-PDServer, released under GPLv3
# Roaster Set Temperature

import Pyro4
import sys


def main():
    new_roaster_heat_level = int(sys.argv[1])

    roast_control = Pyro4.Proxy("PYRONAME:roaster.sr700")
    if new_roaster_heat_level > -1 and new_roaster_heat_level <=8:
        roast_control.set_heat_level(new_roaster_heat_level)


if __name__ == '__main__':
    main()
