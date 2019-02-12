#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SR700-Artisan-PDServer, released under GPLv3
# Roaster Set Fan Speed
import Pyro4
import sys

def main():

    roast_control = Pyro4.Proxy("PYRONAME:roaster.sr700")
    roast_control.disable_temp_manual_mode()


if __name__ == '__main__':
    main()
