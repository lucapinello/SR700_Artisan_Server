#!/bin/sh

python3 -m Pyro4.naming &
sudo python3 SAPDServer.py
