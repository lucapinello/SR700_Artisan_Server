# -*- coding: utf-8 -*-
# Copyright (c) 2015-2016 Jeff Stevens
# Made available under the MIT license.

import time
import freshroastsr700
import logging


class Roaster(object):
    def __init__(self):
        """Creates a freshroastsr700 object passing in methods included in this
        class."""
        self.roaster = freshroastsr700.freshroastsr700(
            self.update_data, self.next_state, thermostat=True)

    def update_data(self):
        """This is a method that will be called every time a packet is opened
        from the roaster."""
        cur_state = self.roaster.get_roaster_state()
        print("Current Temperature:", self.roaster.current_temp, cur_state)

    def next_state(self):
        """This is a method that will be called when the time remaining ends.
        The current state can be: roasting, cooling, idle, sleeping, connecting,
        or unkown."""
        if(self.roaster.get_roaster_state() == 'roasting'):
            self.roaster.time_remaining = 20
            self.roaster.cool()
        elif(self.roaster.get_roaster_state() == 'cooling'):
            self.roaster.idle()

    def start_test(self):
        self.roaster.auto_connect()
        # Wait for the roaster to be connected.
        while(self.roaster.connected is False):
            print("Please connect your roaster...")
            time.sleep(1)

        # Set variables.
        self.roaster.target_temp = 200
        self.roaster.fan_speed = 9
        self.roaster.time_remaining = 10

        time.sleep(10)

        # Disconnect from the roaster.
        self.roaster.disconnect()


if __name__ == '__main__':
    # Create a roaster object.
    r = Roaster()
    r.start_test()
