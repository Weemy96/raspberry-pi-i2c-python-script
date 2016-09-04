# Raspberry-pi-i2c-4x20-monitor-script
Raspi i2c 4x20 monitor python script
</br>
</br>
<h3>How to use?</h3>
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
3. Auto startup this code? Just type <b>"sudo nano /etc/rc.local"</b> insert the command <b>"sudo python &lt;you script location&gt;"</b> before <b>"exit 0"</b>.
</br>
</br><b>ip.py</b> = Get local network IP. (Modem local IP)&lt;Class file&gt;
</br><b>uptime.py</b> = Get uptime. &lt;Class file&gt;
</br><b>ram_d.py</b> = Get Ram information. &lt;Class file&gt;
</br><b>monitor.py</b> =Main script

#Disclaimer
All the code copy on raspberry pi forums, stackoverflow and github. Some code I modify for my self.
If any copyright infringement, please inform me. I will delete the code in 48 Hours. Thank You.
