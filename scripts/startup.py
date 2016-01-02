# Simple script executed at startup
import subprocess
import time
import sys
import os
FNULL = open(os.devnull, 'w')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

server_name = sys.argv[1] if len(sys.argv) > 1 else "Please specify server name" 


print bcolors.BOLD + "Welcome on " +  bcolors.OKBLUE + server_name + bcolors.ENDC + bcolors.BOLD + " server"

print bcolors.UNDERLINE + "Disk usage:" + bcolors.ENDC
print subprocess.check_output(["df", "-h"])

print bcolors.UNDERLINE + "Local date: " + bcolors.ENDC + bcolors.OKBLUE + time.strftime("%c") + bcolors.ENDC + "\n"

# Let's ping servers
servers=[]
for line in open("/etc/startupscript/hosts", 'r'):
	if len(line) > 0 and line[0] == "#":
		continue
	servers.append((line.split(':')[0], line.split(':')[1][:-1]))
print bcolors.UNDERLINE + "Servers state:" + bcolors.ENDC
for server in servers:
	print " *", server[0], "(" + server[1] + ")", "is", (bcolors.OKGREEN + "on" if subprocess.call(["ping", "-c 1", server[1]], stdout=FNULL) == 0 else bcolors.WARNING + "off"), bcolors.ENDC
