#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SR700-Artisan-PDServer, released under GPLv3
# Get_Roaster_State
import Pyro4

def main():
    roast_control = Pyro4.Proxy("PYRONAME:roaster.sr700")
    et,bt=roast_control.output_temps()
    #Celsius = (Fahrenheit – 32) * 5/9
    et = (et - 32) * 5/9
    bt = (bt - 32) * 5/9
    print ("%d,%d" %(et,bt)) #in manual mode the values are negative.

if __name__ == '__main__':
    main()
