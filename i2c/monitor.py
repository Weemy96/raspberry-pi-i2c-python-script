## loading the class
import lcddriver
import ram_d
import ip
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
	row_1 ="CPU TEMP: "+str(out_c)+"'C"

	##FREE Ram display
	RAM_stats = ram_d.get()
	RAM_total = int(RAM_stats[0])
	RAM_used = int(RAM_stats[1])
	RAM_free = int(RAM_stats[2])
	if RAM_free >= 100:
		row_2 = "Free RAM: %2d"%RAM_free+"/"+str(RAM_total)+" MB"
	else:
		row_2 = "Free RAM:  %2d"%RAM_free+"/"+str(RAM_total)+" MB"

##IP display
	space=""
	ipaddr = ip.get_ip()
	if(ipaddr == "Not Connection"):
		row_4 = "IP: %2s"%space+str(ipaddr)
	else:
		row_4 = "IP: %2s"%space+str(ipaddr)+"%3s"%space

## Internet Speed display (Wifi)
	spd = speed()
	c_sp = spd - spd_c
	spd_c = spd
	
	if (c_sp > 1048576):
		rx=c_sp/1048576;
		row_3 = "NSpeed: %7.2f"%rx+" MB/s"

	elif (c_sp >= 1024):
		rx=c_sp/1024
		row_3 = "NSpeed: %7.2f"%rx+" kB/s"

	else:
		row_3 = "NSpeed: %8.2f"%c_sp+" B/s"
		
##get uptime
	#row_4=uptime.uptime()
##i2c screen display

	lcd.lcd_display_string(row_1, 1)
	lcd.lcd_display_string(row_2, 2)
	lcd.lcd_display_string(row_3, 3)
	lcd.lcd_display_string(row_4, 4)

	#maybe 10~30% +-
	time.sleep(0.3)

