import sys
import os
import time

def getVersionString():
	return getImageVersionString()

def getImageVersionString():
	try:
		if os.path.isfile('/var/lib/opkg/status'):
			st = os.stat('/var/lib/opkg/status')
		else:
			st = os.stat('/usr/lib/ipkg/status')
		tm = time.localtime(st.st_mtime)
		if tm.tm_year >= 2011:
			return time.strftime("%Y-%m-%d %H:%M:%S", tm)	
	except:
		pass
	return _("unavailable")

def getEnigmaVersionString():
	import enigma
	list = []
	enigma_version = enigma.getEnigmaVersionString()
	if '-(no branch)' in enigma_version:
		enigma_version = enigma_version [:-12]
#iq [
		list = enigma_version.split("-")
	return list[1] + "-" + list[2] + "-" + list[0]
#iq ]

def getKernelVersionString():
	try:
		return open("/proc/version","r").read().split(' ', 4)[2].split('-',2)[0]
	except:
		return _("unknown")

def getHardwareTypeString():
	try:
		if os.path.isfile("/proc/stb/info/boxtype"):
			return open("/proc/stb/info/boxtype").read().strip().upper() + " (" + open("/proc/stb/info/board_revision").read().strip() + "-" + open("/proc/stb/info/version").read().strip() + ")"
		if os.path.isfile("/proc/stb/info/hwmodel"):
			return open("/proc/stb/info/hwmodel").read().strip().upper().replace('TM', 'TM-').replace('OE', '-OE').replace('MEDIABOX', 'Mediabox HD LX-1').replace('SUPER', '-SUPER').replace('NANO2T','NANO-2T')
#			return "VU+" + open("/proc/stb/info/vumodel").read().strip().upper() + "(" + open("/proc/stb/info/version").read().strip().upper() + ")" 
#		if os.path.isfile("/proc/stb/info/model"):
#			return open("/proc/stb/info/model").read().strip().upper()
	except:
		pass
	return _("unavailable")

def getImageTypeString():
	try:
		return open("/etc/issue").readlines()[-2].capitalize().strip()[:-6]
	except:
		pass
	return _("undefined")

# iq[
def getMicomVersionString():
	try:
		import fcntl, array
		f = array.array('h', [0])
		fp = open('/dev/dbox/fp0', 'w')
		fcntl.ioctl(fp.fileno(), 0x428, f, 1)
		return '%s' % f.tolist()[0]
	except:
		return _("unknown")

# ]

# For modules that do "from About import about"
about = sys.modules[__name__]
