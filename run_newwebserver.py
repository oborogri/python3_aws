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
from create_instance import *

# User is presented with an action menu

end = 1
while end > 0: 

	print('\n''  ####################################################################')
	print('  #   This script will create and launch a new Amazon EC2 instance   #')
	print('  #   You must have an AWS account and relevant access credentials   #')
	print('  ####################################################################')
	print('  #                                                                  #')
	print('  #     Please enter one of the following options to proceed:        #')
	print('  #                                                                  #')
	print('  ####################################################################')
	print('  #                                                                  #')
	print('  #    1. Create and define AWS security groups (if none avaialble)  #')
	print('  #                                                                  #')
	print('  #    2. Create and launch  a new Amazon EC2 instance               #')
	print('  #                                                                  #')
	print('  #    3. Copy Python3 script check_server.py to the AWS instance    #')
	print('  #                                                                  #')
	print('  #    4. Run check_server.py script on AWS instance                 #')
	print('  #                                                                  #')
	print('  #    5. Exit the program                                           #')
	print('  #                                                                  #')
	print('  ####################################################################')
	choice = int(input('\n''  Please enter a number: '))
	if choice == 1:
		print('\n''  you choose option 1:')
		subprocess.call(['python3', 'security_groups.py'])
		subprocess.call(['clear'])
	elif choice == 2:
		print('\n''  you choose option 2:')
		subprocess.call(['python3', 'create_instance.py'])
		subprocess.call(['clear'])
	elif choice == 3:
		print('\n''  you choose option 3:')
		subprocess.call(['python3', 'instance_server.py'])
		subprocess.call(['clear'])		
	elif choice == 4:
		subprocess.call(['run_checkserver.py'])
		subprocess.call(['clear'])	
		break
	else:
		print('\n''  Invalid option! Exiting the program!')
		subprocess.call(['clear'])	
		subprocess.call(['exit'])	
		break
end = 0	 