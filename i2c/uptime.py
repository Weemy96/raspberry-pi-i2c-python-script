import os 
def uptime():
 
     try:
         f = open( "/proc/uptime" )
         contents = f.read().split()
         f.close()
     except:
        return "Cannot open uptime file: /proc/uptime"
 
     total_seconds = float(contents[0])
 
     # Helper vars:
     MINUTE = 60
     HOUR = MINUTE * 60
     DAY = HOUR * 24
 
     # Get the days, hours, etc:
     days=0
     hours=0
     minutes=0
     seconds=0
     days = int( total_seconds / DAY )
     hours = int( ( total_seconds % DAY ) / HOUR )
     minutes = int( ( total_seconds % HOUR ) / MINUTE )
     seconds = int( total_seconds % MINUTE )
 
     # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
     string = ""
     if days >= 0:
         string += str(days) + " " + (days <= 1 and "day" or "days" ) + ", "
	 if minutes <10:
		 string+=str(hours)+":0"+str(minutes)
	 elif minutes>=10:
		 string+=str(hours)+":"+str(minutes)
	 if seconds <10:
		 string+=":0"+str(seconds)
	 elif seconds>=10:
		 string+=":"+str(seconds)
		 
     return string;
#while 1:
#	print uptime()
