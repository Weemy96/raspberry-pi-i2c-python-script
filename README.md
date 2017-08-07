# Raspberry-pi-i2c-4x20-monitor-script
Raspi i2c 4x20 monitor python script
</br>
</br>
### How to use?
</br>
0. i2c screen connect to gpio like image below:
</br>
<img src="https://github.com/Weemy96/raspberry-pi-i2c-python-script/raw/master/rpi-i2c-pins.png"/>
</br>
**Image resource from http://www.robot-electronics.co.uk/
</br>
</br>
1. On raspberry pi terminal or ssh connect to raspberry pi type <b>sudo raspi-config</b> > Advanced Options > I2C > Enable
<h5>Note: I use raspbian OS for my code, other OS I haven't try.</h5>
</br>
2. The Setup you can visit this 2 page 
   </br>https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c#installing-kernel-support-manually
   </br>http://hardware-libre.fr/2014/03/en-raspberry-pi-using-a-4x20-characters-display/
</br>

3. Request <code>psutil</code>
```sh
sudo apt install gcc python-dev python-pip
pip install psutil
```
4. Auto startup this code? Just type copy or move the startup script "<b>i2c_monitor</b>" to <b>/etc/init.d/</b>
</br> after give the execute codemission.</br>
```sh
sudo chmod 755 /etc/init.d/i2c_monitor
```
</br>
### Run</br>

```sh
sudo /etc/init.d/i2c_monitor start
```

### Stop
```sh
sudo /etc/init.d/i2c_monitor stop
```

</br><b>ip.py</b> = Get local network IP. (Modem local IP)&lt;Class file&gt;
</br><b>uptime.py</b> = Get uptime. &lt;Class file&gt;
</br><b>ram_d.py</b> = Get Ram information. &lt;Class file&gt;
</br><b>monitor.py</b> =Main script


Copyright © 2017 Weemy96
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See http://www.wtfpl.net/ for more details.