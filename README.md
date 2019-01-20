# SR700-Artisan-PDServer
Python Pyro PID Daemon server for Fresh Roast SR700 for use with Artisan roasting software.

This allows for connection of Fresh Roast SR700 coffee roaster with Artisan roasting software.

# Drivers

USB Drivers are automatically installed for Linux.  For Windows please refer to OpenRoast Software and Driver installation page (https://github.com/Roastero/Openroast/blob/master/docs/wiki/users_installing_windows.md) to ensure you have the appropriate USB drivers installed.

# Setting Up A Development Environment

Requirements are Python3 and [Artisan](https://github.com/artisan-roaster-scope/artisan/releases) (tested with v1.5.0)

**Ubuntu Linux**

    sudo apt-get install git python3 python3-pip
    git clone https://github.com/infinigrove/SR700-Artisan-PDServer.git
    cd SR700-Artisan-PDServer
    pip3 install -r requirements.txt
    sudo ./Install.linux.sh
    
The Install.linux.sh will install the commands in the Artisan directory /usr/share/artisan/SR700/  if your commands are not installed there then alter your Artisan configuration accordingly.

Make sure the Fresh Roast SR700 roaster is connected before starting the server.

    ./StartSAPDServer.linux.sh
    
Start Artisan. Click Help -> Load Settings... select the sr700-artisan-Linux-settings.aset file from the SR700-Artisan-PDServer/settings dir.
    
**Windows**

    git clone https://github.com/infinigrove/SR700-Artisan-PDServer.git
    cd SR700-Artisan-PDServer
    pip install -r requirements.txt
    ./Install.windows.cmd
    
The Install.windows.cmd will need to be run as Administrator and will install the commands in the Artisan directory C:\Program Files\Artisan\SR700 .

Make sure the Fresh Roast SR700 roaster is connected before starting the server.

    ./StartSAPDServer.windows.cmd
    
Start Artisan. Click Help -> Load Settings... select the sr700-artisan-Windows-settings.aset file from the SR700-Artisan-PDServer/settings dir.

Detailed Windows instruction video - [Fresh Roast SR700 controlled by Artisan on Windows10](https://youtu.be/3Usqqbwv3i8)

# Manually Configure Artisan BT bean temperature

Start Artisan, click Config->Device from the drop-down menu.  In the Device Assignment dialog box select "Program" and replace "test.py" with "/usr/share/artisan/SR700/Get_Artisan_Temp.py" for Linux or "python "C:\Program Files\Artisan\SR700\Get_Artisan_Temp.py"" for Windows then click "OK"

# Manually Configure Artisan Sliders

Click Config->Events from the drop-down menu.  In the "Event Types" row change the following

    1 "Air" to "Timer"
    2 "Drum" to "Fan"
    4 "Burner" to "Temp"
    
Click the "Sliders" tab and check the box for "Timer", "Fan",  and "Temp" and select an Action of "Call Program" for each.  Then set them up as follows:

**Linux**

    Timer Command = "/usr/share/artisan/SR700/Roaster_Set_Time.py {}", Offset = 1, Factor = 6.00, Min = 0, Max = 100
    Fan Command = "/usr/share/artisan/SR700/Roaster_Set_Fan.py {}", Offset = 0, Factor = 1.00, Min = 1, Max = 9
    Temp Command = "/usr/share/artisan/SR700/Roaster_Set_Temp.py {}", Offset = 0, Factor = 1.00, Min = 120, Max = 550
    
**Windows**

    Timer Command = "sr700\set_time.cmd {}", Offset = 1, Factor = 6.00, Min = 0, Max = 100
    Fan Command = "sr700\set_fan.cmd {}", Offset = 0, Factor = 1.00, Min = 1, Max = 9
    Temp Command = "sr700\set_temp.cmd {}", Offset = 0, Factor = 1.00, Min = 120, Max = 550
    
**Note:** Setting the temp below/lower than 150 will cause the roaster to go into cooling cycle.

# Configue Artisan Alarms

(see samples in alarms dir)

To use the included Alarm sets:

    Click "ON" to display sliders and temperature
    Click "START" to send inital time, temperature, and fan speed
    Wait 10+ seconds to make sure initial settings are sent to the roaster (May take 30+ seconds for Windows)
    Click "CHARGE" to start roasting

Command to start roaster

    Linux = "/usr/share/artisan/SR700/Roaster_charge.py"
    Windows = "sr700\start_roast.cmd"
    
[More on configuring Artisan alarms](https://artisan-roasterscope.blogspot.com/2013/03/alarms.html)