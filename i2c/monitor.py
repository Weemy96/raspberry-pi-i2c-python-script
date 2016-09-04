## loading the class
import lcddriver
import ram_d
#import ip """find local ip address"""
import time
import os
import uptime

##Get CPU Temperature
def temperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return float(res[res.index('=') + 1:res.rindex("'")])

##Get Internet Speed
#Wifi
def speed():
	##If use cable pls change 'wlan0' to 'eth0'
	spe = os.popen('cat /sys/class/net/wlan0/statistics/rx_bytes')
#	spee = os.popen('cat /sys/class/net/wlan0/statistics/rx_bytes')
	sp = spe.read()
	#sp_w = spee.read()
	sp_st = float(sp)# + float(sp_w)##now auto calulate internet speed not need set-up eth0 or wlan0
	return float(sp_st)

#Eth0
#def eth_speed():
#	spe_eth = os.popen('cat /sys/class/net/eth0/statistics/rx_bytes')
#	sp_eth = spe_eth.read()
#	#sp_w = spee.read()
#	sp_st_eth = float(sp_eth)# + float(sp_w)##now auto calulate internet speed not need set-up eth0 or wlan0
#	return float(sp_st_eth)
	
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
	
	if c_sp < 1024:
		RX_C = c_sp
		speed_dsp = "Wifi: %9.2f"%RX_C+" b/s"

	elif c_sp >= 1024 and c_sp < 1024000:
		RX_C = c_sp/1024
		speed_dsp = "Wifi: %8.2f"%RX_C+" kb/s"

	else:
		RX_C = c_sp/(1024*1024)
		speed_dsp = "Wifi: %8.2f"%RX_C+" MB/s"
		
## Internet Speed display (Eth0)
#	spd_eth = eth_speed()
#	c_sp_eth = spd_eth - spd_c_eth
#	spd_c_eth = spd_eth
#	
#	if c_sp_eth < 1024:
#		RX_C_eth = c_sp_eth
#		speed_dsp_eth = "Eth0: %9.2f"%RX_C_eth+" b/s"
#
#	elif c_sp_eth >= 1024 and c_sp_eth < 1024000:
#		RX_C_eth = c_sp_eth/1024
#		speed_dsp_eth = "Eth0: %8.2f"%RX_C_eth+" kb/s"
#
#	else:
#		RX_C_eth = c_sp_eth/(1024*1024)
#		speed_dsp_eth = "Eth0: %8.2f"%RX_C_eth+" MB/s"

##get uptime
	get_uptime=uptime.uptime()
##i2c screen display

	lcd.lcd_display_string(outstring, 1)
	lcd.lcd_display_string(ram_f, 2)
	lcd.lcd_display_string(speed_dsp, 3)
	lcd.lcd_display_string(get_uptime, 4)
	
	#maybe 10~30% +-
	time.sleep(0.35)

