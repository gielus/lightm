#!/usr/bin/env python
import os
from datetime import datetime

def availableLights ( retval = 'ALL' ):
	conffile = "/etc/lightm/lights.conf"
	if os.path.isfile(conffile):
		fh = open(conffile,"r")
		conf = fh.readlines()
		fh.close()

		config = {}

		for i in conf:
			c = i.strip().split("\t")

			name = c[0]
			type = c[1]
			freq = c[2]
			swit = c[3]
			file = c[4]

			if not config.has_key(name):
				config[name] = {}

			config[name]['name'] = name
			config[name]['type'] = type
			config[name]['freq'] = freq
			config[name]['swit'] = swit
			config[name]['file'] = file

	else:
		print "Config file not found"

	if retval == 'ALL':
		return config
	else:
		return config[retval]

def setState ( light , state = 'off' ):
	path = light['file']+light['name']

	fh = open(path,"w")
	fh.write(state)
	fh.close()

def getState ( light ):
        path = light['file']+light['name']

        fh = open(path,"r")
        state = fh.read()
        fh.close()

	return state


def switch ( light, action = 'off' ):
	setState( light, action )
	
	cmd = []
	cmd.append("sudo /usr/local/bin/lights/"+light['type'])
	cmd.append(light['freq'])
	cmd.append(light['swit'])
	cmd.append(action)
	cmd = " ".join(cmd)

	log ( light['name'], action, cmd )

	os.system(cmd)
	
	return light['name']+","+action

def toggle ( light ):
	light = availableLights( light )

	state = getState( light )

	if state == "off":
		return switch (light,'on')
	elif state == "on":
		return switch (light,'off')
	
def log ( light , action, cmd):
	logfile = "/var/log/lightm/lightm"

	string = []
	string.append(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
	string.append(light)
	string.append(action)
	string.append(cmd)

	string = ",".join(string)

	fh = open(logfile,"a")
	fh.write(string + "\n")
	fh.close()
