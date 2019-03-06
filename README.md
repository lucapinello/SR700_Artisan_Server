# Freshroast SR700 Artisan Server

Server to use the Freshroast SR700 with Artisan (https://artisan-scope.org/). This server simplifies dramatically the setup and the configuration of Artisan (settings are included).

It also allows to fully automate the roasting with users' profiles that can be easily created with another tool (see the end of the document).

If available the Phidget Temperature Sensor can be used to improve the roasting and to measure the true beans temperature.

This work was inspired by the SR700-Artisan-PDServer (https://github.com/infinigrove/SR700-Artisan-PDServer) and freshroastsr700(https://github.com/Roastero/freshroastsr700/tree/master/freshroastsr700).

## 0. Requirements

Python >=2.7

You can use the Python installed with your system, but I strongly suggest to install and use the Anaconda Python 3.7 freely available from here:

http://anaconda.com/download

On Windows machine unfortunately you have to use speficially Python 3.5 If you have Anaconda install you can do this with:

`conda install python=3.5`

## 1. Phidget setup (OPTIONAL)

If you have a Phidget temperature sensor, install the Phidget driver for your machine: https://www.phidgets.com/docs/Operating_System_Support

## 2. Install this Server with:

Open a terminal or the Terminal app (osx) and type this command:

`pip install SR700_Artisan_Server`

To update from an old version type:

`pip install SR700_Artisan_Server==1.5`

*Important* Please download again and reload the setting file!

## 3. Start the server in the Terminal with:

`Start_SR700_Artisan_Server`  

If you a a Phidget without an hub, start the server with:

`Start_SR700_Artisan_Server --enable_extension phidget_simple`

If you a a Phidget with the hub, start the server with:

`Start_SR700_Artisan_Server --enable_extension phidget_hub`

Depending on your hub setup you may need to change hub port and channel adding these two flags:

  ```
  --phidget_hub_port PHIDGET_HUB_PORT
  --phidget_hub_channel PHIDGET_HUB_CHANNEL
  ```

For example, to use the hub port 0 and the channel 1:

`Start_SR700_Artisan_Server --enable_extension phidget_hub --phidget_hub_port 0  --phidget_hub_channel 1`

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
If you use a MAX31865, then start the server with:
`Start_SR700_Artisan_Server --enable_extension max31865`

You should see something like this with the MAX31865:
```
[ [State:idle](Temp SR700:150)(Temp max31865 119)(Target temp: 449)(Fan Speed: 9)(Time left: 649) ]
```

If you need to, you can also specify the GPIO pins used by the MAX31865, e.g.
`Start_SR700_Artisan_Server --enable_extension max31865 --max_31865_gpio_cs=8 --max_31865_gpio_miso=9 --max_31865_gpio_mosi=10 --max_31865_gpio_clk=11`

See documentation for `freshroastsr700_phidget` for more info.

## 4. Start Artisan

**Important** if you are on a Mac start Artisan **from the Terminal app** with this command:

`/Applications/Artisan.app/Contents/MacOS/Artisan`

## 5. In Artisan go under Help and select Load Settings…

Download and use this file: https://raw.githubusercontent.com/lucapinello/SR700_Artisan_Server/master/SR700_Artisan_Server/settings/artisan-settings.aset

The roasting profiles are created through alarms, a generic profile is already loaded.

Now you are ready to roast!

Hit Start, and keep in mind that the first 30sec are for preheating the machine.

## NOTE: You can create custom profiles with this other tool I wrote: https://github.com/lucapinello/SR700_Artisan_Profile_Builder

You can also disable the automatic changes in temperature and fan using the buttons: Temp Manual and Fan Manual. The buttons Temp Alarm and Fan Alarm enable instead the alarm mode.
