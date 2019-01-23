#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SR700-Artisan-PDServer, released under GPLv3
# Get_Roaster_State
import Pyro4

def main():
    roast_control = Pyro4.Proxy("PYRONAME:roaster.sr700")
    et,bt=roast_control.output_sr700_and_phidget_temp()
    print ("%d,%d" %(et,bt))

if __name__ == '__main__':
    main()
