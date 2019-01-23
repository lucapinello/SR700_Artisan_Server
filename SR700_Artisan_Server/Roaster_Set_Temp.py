#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SR700-Artisan-PDServer, released under GPLv3
# Roaster Set Temperature

import Pyro4
import sys


def main():
    new_roaster_temperature = sys.argv[1]

    roast_control = Pyro4.Proxy("PYRONAME:roaster.sr700")
    if int(new_roaster_temperature) > -1 and int(new_roaster_temperature) <551:
        roast_control.set_temperature(new_roaster_temperature)


if __name__ == '__main__':
    main()
