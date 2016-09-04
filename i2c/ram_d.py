import os

def get():
	p = os.popen('free -m')
	i = 0
	while 1:
		i = i + 1
		line = p.readline()
		if i==2:
			return(line.split()[1:4])
