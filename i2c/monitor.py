## loading the class
import lcddriver
import ram_d
#import ip """find local ip address"""
import time
import os
import psutil
import uptime

##Get CPU Temperature
def temperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return float(res[res.index('=') + 1:res.rindex("'")])

##Get Internet Speed in bytes
def speed():
	spe=psutil.net_io_counters().bytes_recv
	return float(spe)

# lcd start
lcd = lcddriver.lcd()

# this command clears the display (captain obvious)
lcd.lcd_clear()

# now we can display some characters (text, line)

##speed starting
spd_c = 0
spd_c_eth = 0

while True:
	##CPU Temperature display
	out_c = temperature()
	outstring ="CPU TEMP: "+str(out_c)+"'C"

	##FREE Ram display
	RAM_stats = ram_d.get()
	RAM_total = int(RAM_stats[0])
	RAM_used = int(RAM_stats[1])
	RAM_free = int(RAM_stats[2])
	if RAM_free >= 100:
		ram_f = "Free RAM: %2d"%RAM_free+"/"+str(RAM_total)+" MB"
	else:
		ram_f = "Free RAM:  %2d"%RAM_free+"/"+str(RAM_total)+" MB"

##IP display
#	ipaddr = ip.s.getsockname()[0]
#	ip_d = "IP: "+str(ipaddr)

## Internet Speed display (Wifi)
	spd = speed()
	c_sp = spd - spd_c
	spd_c = spd
	
	if (c_sp > 1048576):
		rx=c_sp/1048576;
		speed_dsp = "NSpeed: %7.2f"%rx+" MB/s"

	elif (c_sp >= 1024):
		rx=c_sp/1024
		speed_dsp = "NSpeed: %7.2f"%rx+" kB/s"

	else:
		speed_dsp = "NSpeed: %8.2f"%c_sp+" B/s"
		
##get uptime
	get_uptime=uptime.uptime()
##i2c screen display

	lcd.lcd_display_string(outstring, 1)
	lcd.lcd_display_string(ram_f, 2)
	lcd.lcd_display_string(speed_dsp, 3)
	lcd.lcd_display_string(get_uptime, 4)
	
	#maybe 10~30% +-
	time.sleep(0.3)

