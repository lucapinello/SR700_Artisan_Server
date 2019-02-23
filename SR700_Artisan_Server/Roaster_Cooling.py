#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SR700-Artisan-PDServer, released under GPLv3
# Roaster Run Recipe

import Pyro4

def main():
    roast_control = Pyro4.Proxy("PYRONAME:roaster.sr700")
    roast_control.enable_temp_manual_mode()
    roast_control.enable_fan_manual_mode()
    roast_control.set_fan_speed(9)
    roast_control.run_cooling()

if __name__ == '__main__':
    main()
