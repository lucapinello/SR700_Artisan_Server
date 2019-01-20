# SR700-Artisan-PDServer-Phidget

Extension of the SR700-Artisan-PDServer (https://github.com/infinigrove/SR700-Artisan-PDServer) to use with the Phidget Temperature Sensor (if available) and to simplify the setup and the configuration with Artisan (https://artisan-scope.org/).

1. Phidget setup (OPTIONAL)

Install the Phidget driver for your machine: https://www.phidgets.com/docs/Operating_System_Support

Download and install the Python module from here:https://www.phidgets.com/docs/Language_-_Python

2. Install this Server with: 

pip install SR700-Artisan-PDServer-Phidget

3. If you have a Phidget Start the server with:

Start_SR700_Artisan_Server.py  

Otherwise with:

Start_SR700_Artisan_Server.py no_phidget

(both the SR700 Roaster and the Phidget must be attached before starting this command )

If the server is running correctly you should see something like this if you have a Phidget:

[State:idle] Temp SR700:150 Temp Phidget 52 Target temp: 150 Fan Speed: 1 Time left: 0
[State:idle] Temp SR700:150 Temp Phidget 52 Target temp: 150 Fan Speed: 1 Time left: 0
[State:idle] Temp SR700:150 Temp Phidget 52 Target temp: 150 Fan Speed: 1 Time left: 0
[State:idle] Temp SR700:150 Temp Phidget 52 Target temp: 150 Fan Speed: 1 Time left: 0

Or like this without a Phidget:

[State:idle] Temp SR700:150  Target temp: 150 Fan Speed: 1 Time left: 0
[State:idle] Temp SR700:150  Target temp: 150 Fan Speed: 1 Time left: 0
[State:idle] Temp SR700:150  Target temp: 150 Fan Speed: 1 Time left: 0
[State:idle] Temp SR700:150  Target temp: 150 Fan Speed: 1 Time left: 0

4. In Artisan go under help and select Load Settings…

Use this file if you have a Phidget: https://raw.githubusercontent.com/lucapinello/SR700-Artisan-PDServer-Phidget/master/settings/artisan-settings.aset

Or this if you don't have a Phidget: https://raw.githubusercontent.com/lucapinello/SR700-Artisan-PDServer-Phidget/master/settings/artisan-settings-no-phidget.aset

The roasting profiles are created through alarms, a generic profile is already loaded.

Now you are ready to roast!

Hit Start, and keep in mind that the first 30sec are for preheating the machine. 

NOTE: You can create custom profiles with this other tool I wrote: https://github.com/lucapinello/create_artisan_alarms_phidget



