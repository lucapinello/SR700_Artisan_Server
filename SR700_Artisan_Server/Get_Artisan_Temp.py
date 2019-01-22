#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SR700-Artisan-PDServer, released under GPLv3
# Get_Roaster_State

import Pyro4

def main():
    roast_control = Pyro4.Proxy("PYRONAME:roaster.sr700")
    print (roast_control.output_current_state()[0:3])

if __name__ == '__main__':
    main()
