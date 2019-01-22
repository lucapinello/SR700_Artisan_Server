# Freshroast SR700 Artisan Server

Server to use the Freshroast SR700 with Artisan (https://artisan-scope.org/). This server simplifies dramatically the setup and the configuration of Artisan (settings are included).

It also allows to fully automate the roasting with users' profiles that can be easily created with another tool (see the end of the document). 

If available the Phidget Temperature Sensor can be used to improve the roasting and to measure the true beans temperature. 

This work was inspired by the SR700-Artisan-PDServer (https://github.com/infinigrove/SR700-Artisan-PDServer) and freshroastsr700(https://github.com/Roastero/freshroastsr700/tree/master/freshroastsr700).

## 0. Requirements

Python >=3.5

You can use the Python installed with your system, but I strongly suggest to install and use the Anaconda Python 3.7 freely available from here:
http://anaconda.com/download

## 1. Phidget setup (OPTIONAL)

If you have a Phidget temperature sensor, install the Phidget driver for your machine: https://www.phidgets.com/docs/Operating_System_Support

## 2. Install this Server with: 

Open a terminal or the Terminal app (osx) and type this command:

`pip install SR700_Artisan_Server`

If you have Python3 you may need this command instead:

`pip3 install SR700_Artisan_Server`

## 3. If you have a Phidget start the server in the Terminal with:

`Start_SR700_Artisan_Server`  

Otherwise with:

`Start_SR700_Artisan_Server no_phidget`

(both the SR700 Roaster and the Phidget must be attached before starting this command )

If the server is running correctly you should see something like this if you have a Phidget:
```
[State:idle] Temp SR700:150 Temp Phidget 52 Target temp: 150 Fan Speed: 1 Time left: 0
[State:idle] Temp SR700:150 Temp Phidget 52 Target temp: 150 Fan Speed: 1 Time left: 0
[State:idle] Temp SR700:150 Temp Phidget 52 Target temp: 150 Fan Speed: 1 Time left: 0
[State:idle] Temp SR700:150 Temp Phidget 52 Target temp: 150 Fan Speed: 1 Time left: 0
```
Or like this without a Phidget:

```
[State:idle] Temp SR700:150  Target temp: 150 Fan Speed: 1 Time left: 0
[State:idle] Temp SR700:150  Target temp: 150 Fan Speed: 1 Time left: 0
[State:idle] Temp SR700:150  Target temp: 150 Fan Speed: 1 Time left: 0
[State:idle] Temp SR700:150  Target temp: 150 Fan Speed: 1 Time left: 0
```

## 4. In Artisan go under Help and select Load Settings…

Download and use this file if you have a Phidget: https://raw.githubusercontent.com/lucapinello/SR700_Artisan_Server/master/SR700_Artisan_Server/settings/artisan-settings.aset

Or this if you don't have a Phidget: https://raw.githubusercontent.com/lucapinello/SR700_Artisan_Server/master/SR700_Artisan_Server/settings/artisan-settings-no-phidget.aset

The roasting profiles are created through alarms, a generic profile is already loaded.

Now you are ready to roast!

Hit Start, and keep in mind that the first 30sec are for preheating the machine. 

## NOTE: You can create custom profiles with this other tool I wrote: https://github.com/lucapinello/create_artisan_alarms_phidget



