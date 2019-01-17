import os

COMMAND = "vcgencmd measure_temp"

def get_temp():
	out = os.popen(COMMAND).readline()
	temp = out.replace('temp=', '').replace("'C", '').strip()
	temp = float(temp)
	return temp

if __name__ == '__main__':
	print(get_temp())
