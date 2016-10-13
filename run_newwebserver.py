#!/usr/bin/python3

# A	Python	script	to	create and launch a new launch a new Amazon EC2 instance. 
# Boto API library must be used to launch from a free tier Amazon Linux AMI. 
# Amazon credentials must be provided in a .boto file (not in the Python code).
# The public IP address of the instance must be used to connect it. 
# This script should install the nginx webserver using the appropriate ssh command line options. 
# The script should then copy the check_webserver.py script from local machine to the new instance using scp and 
# then execute this script to check if the nginx process is running. 
# If it is not running, it should start the nginx webserver process (using ssh remote command execution, for example). 
# Both scripts should perform appropriate error handling and output meaningful error messages to the user. 

# This script requires boto installed and AWS access credentials included in a .boto file on local machine. 
# If working on a virtual machine, system date/time have to be updated

import sys
import subprocess
from time import sleep

# User is presented with an action menu

end = 1
while end < 0: 

	print('  #################################################################')
	print('  #  This script will create and launch a new Amazon EC2 instance #')
	print('  #     You must have an AWS account and access credentials       #')
	print('  #################################################################')
	print('  #                                                               #')
	print('  #      Please choose one of the following to proceed:           #')
	print('  #                                                               #')
	print('  #################################################################')
	print('  #                                                               #')
	print('  # 1. ')
	# Creating the AWS instance requires security own groups to be defined   