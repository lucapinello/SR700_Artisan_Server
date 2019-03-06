#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SR700-Artisan-PDServer, released under GPLv3
# Roaster Run Recipe

import Pyro4
import time

def main():
    roast_control = Pyro4.Proxy("PYRONAME:roaster.sr700")
    roast_control.enable_temp_manual_mode()
    roast_control.enable_fan_manual_mode()
    roast_control.set_fan_speed(9)
    roast_control.run_cooling()

    # if the Artisan alarms trigger before detecting manual fan mode, then 
    # they will reset the fan to a (likely) lower speed.  So, keep 
    # keep setting fan to recover from race condition.
    time.sleep(2)
    roast_control.set_fan_speed(9)
    time.sleep(2)
    roast_control.set_fan_speed(9)
    time.sleep(2)
    roast_control.set_fan_speed(9)

if __name__ == '__main__':
    main()
