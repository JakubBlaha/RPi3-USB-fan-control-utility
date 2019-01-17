import time
import os
import psutil
from get_temp import get_temp
from tabulate import tabulate

DEFAULT_CONFIG = {'max_temp': 60, 'temp_check_interval': 1, 'cool_by': 0}
STATE_COMMAND = "sudo hub-ctrl -h 0 -P 2 -p %i"
THROTTLING = True # USB power is on by default
INIT_STATE = True # TODO, check, restore at the end
THROTTLED = False # TODO dirty fix for state
COOL_TO = 40


# Load config
with open('config') as f:
	data = f.readlines()

data = {line.split('=')[0].strip(): line.split('=')[1].strip() for line in data}
config = DEFAULT_CONFIG

for key, value in data.items():
	config[key] = float(value) if value.replace('.', '').isdigit() else value
print('Loaded config: ', config)

COOL_TO = config['max_temp'] - config['cool_by']

def throttle(state):
	global THROTTLING, THROTTLED
	if state != THROTTLING or not THROTTLED:
		ret = os.system(STATE_COMMAND % state)
		if not ret:
			THROTTLING = state
			THROTTLED = True
		return ret

# Warn user
print('Warning: This can turn off all the USB ports!')
time.sleep(2)

try:
	while True:
		# Check, throttle
		tmp = get_temp()
		if tmp > COOL_TO:
			throttle(1)
			COOL_TO = config['max_temp'] - config['cool_by']
		else:
			throttle(0)
			COOL_TO = config['max_temp']

		# Output
		os.system('clear')
		cpu = psutil.cpu_freq()
		load = psutil.cpu_percent()
		mem = psutil.virtual_memory().percent
		table = tabulate([[
				   cpu.min, cpu.max, cpu.current, load, mem, tmp, THROTTLING]],
				   headers=['Min', 'Max', 'Curr', 'Load %', 'Mem %', "Temp 'C", 'Fan'])
		print(table)

		# Wait
		time.sleep(config['temp_check_interval'])
except:
	# Restore USBs
	print('Restored power: ', not throttle(INIT_STATE))
	raise
