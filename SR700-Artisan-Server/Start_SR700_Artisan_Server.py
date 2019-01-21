#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2015-2016 Jeff Stevens
# SR700-Artisan-PDServer, released under GPLv3

#Extended by Luca Pinello @lucapinello

import signal
import sys
import time
import sys
from freshroastsr700_phidget import SR700Phidget
import logging
import Pyro4
import socket
import select
import Pyro4.core
import Pyro4.naming



@Pyro4.expose
class Roaster(object):
    def __init__(self,use_phidget_temp=True,kp=0.4, ki=0.0075, kd=0.9):
        """Creates a freshroastsr700 object passing in methods included in this
        class."""

        self.use_phidget_temp=use_phidget_temp
        self.roaster = SR700Phidget(
	    use_phidget_temp=use_phidget_temp,
            update_data_func=self.update_data,
            state_transition_func=self.next_state,
            thermostat=True,
            kp=kp,
            ki=ki,
            kd=kd)

    def update_data(self):
        """This is a method that will be called every time a packet is opened
        from the roaster."""
        cur_state = self.roaster.get_roaster_state()

        if self.use_phidget_temp:
            print("[State:%s] Temp SR700:%d Temp Phidget %d Target temp: %d Fan Speed: %d Time left: %d"  % \
            ( str(cur_state),
            self.roaster.current_temp,
            self.roaster.current_temp_phidget,
            self.roaster.target_temp,
            self.roaster.fan_speed,
            self.roaster.time_remaining))
        else:
            print("[State:%s] Temp SR700:%d Target temp: %d Fan Speed: %d Time left: %d"  % \
            ( str(cur_state),
            self.roaster.current_temp,
            self.roaster.target_temp,
            self.roaster.fan_speed,
            self.roaster.time_remaining))

    def next_state(self):
        """This is a method that will be called when the time remaining ends.
        The current state can be: roasting, cooling, idle, sleeping, connecting,
        or unkown."""
        if(self.roaster.get_roaster_state() == 'roasting'):
            self.roaster.time_remaining = 20
            self.roaster.cool()
        elif(self.roaster.get_roaster_state() == 'cooling'):
            self.roaster.idle()

    def run_roast(self):
        if(self.roaster.get_roaster_state() == 'idle'):
            self.roaster.roast()

    def run_cooling(self):
        self.roaster.cool()

    def stop(self):
            self.roaster.idle()

    def set_fan_speed(self, speed):
        new_speed = int(speed)
        self.roaster.fan_speed = new_speed

    def set_temperature(self, temperature):
        new_temperature = int(temperature)
        if new_temperature < 120:
            self.roaster.cool()
        else:
            self.roaster.target_temp = new_temperature

    def set_time(self, time):
        new_time = int(time)
        self.roaster.time_remaining = new_time

    def output_current_state(self):
        cur_state = self.roaster.get_roaster_state()
        cur_temp = str(self.roaster.current_temp)
        ret_state = cur_temp + cur_state
        return ret_state

    def output_sr700_and_phidget_temp(self):
        cur_state = self.roaster.get_roaster_state()
        cur_temp = str(self.roaster.current_temp)
        ret_state = cur_temp + cur_state
        return self.roaster.current_temp,self.roaster.current_temp_phidget


if __name__ == '__main__':

    use_phidget_temp=True
    kp=0.4
    ki=0.0075
    kd=0.9


    if len(sys.argv) > 1:
        if sys.argv[1]=='no_phidget':
            use_phidget_temp=False
            kp=0.06
            ki=0.0075
            kd=0.01
        else:
            print('Please use these commands:\n Start_SR700_Artisan_Server.py\nor\n Start_SR700_Artisan_Server.py no_phidget')
            sys.exit(1)



    # Create a roaster object.
    r = Roaster(use_phidget_temp=use_phidget_temp,kp=kp,ki=ki,kd=kd)

    # Set logging
    #logging.basicConfig(filename="RoastControl_debug_log.log",level=logging.DEBUG)

    # Conenct to the roaster.
    r.roaster.auto_connect()

    # Wait for the roaster to be connected.
    while(r.roaster.connected is False):
        print("Please connect your roaster...")
        time.sleep(1)


    
    nameserverUri, nameserverDaemon, broadcastServer = Pyro4.naming.startNS()

    daemon = Pyro4.Daemon()                # make a Pyro daemon
    ns = Pyro4.locateNS()
    uri = daemon.register(r)

    print("Ready. Object uri =", uri)      # print the uri so we can use it in the client later
    ns.register("roaster.sr700", uri)
    daemon.requestLoop()                   # start the event loop of the server to wait for calls
