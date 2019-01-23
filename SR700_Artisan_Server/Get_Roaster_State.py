#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SR700-Artisan-PDServer, released under GPLv3
# Get_Roaster_State

import Pyro4

def main():
    roast_control = Pyro4.Proxy("PYRONAME:roaster.sr700")
    print (roast_control.output_current_state())

if __name__ == '__main__':
    main()
