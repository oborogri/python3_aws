#!/usr/bin/python3

# A Python3 script that establish SSH connection to the new instance on AWS
# It will copy check_server script from local machine and will check if nginx webserver is runnig on that instance
# If nginx not runnig - it will install and start the webserver
# The user is presented with info messasges about state of nginx webserver on the instance

def instance_server():
	import sys
	import time
	import subprocess
	from time import sleep
	
	while True:
		try:
			#Obtaining the key file name
			key = input('\n''  Please enter your AWS access key file name \n''  (without any extension): ')
			ip = input('\n''  Please enter the Public IP of your AWS instance: \n''')
			
			# Updating packages on the instance
			print('\n''  Updating packages on the instance...')
			cmd1 = 'ssh -t -o StrictHostKeyChecking=no -i ' + key + '.pem ec2-user@' + ip + ' sudo yum -y update'
			(status, output) = subprocess.getstatusoutput(cmd1)

			if status == 0:
				print('\n''  Packages updated!')
				cmd = 'clear'
			else:
				print('\n''  Packages not updated!')
			sleep(10)

			#Installing Python3 on the instance

			print('\n''  Installing Python3 on the instance...')
			#cmd2 = 'ssh -t -o StrictHostKeyChecking=no -i ' + key + '.pem ec2-user@' + ip + ' sudo yum -y install python35'
			cmd2 = 'ssh -t -i ' + key + '.pem ec2-user@' + ip + ' sudo yum -y install python35'
			(status, output) = subprocess.getstatusoutput(cmd2)
			if status == 0:
				sleep(30)
				print('\n''  Python3 installed!')
			else:
				print('\n''  Python3 not installed!')
			
			# copying check_server.py script ot the instance
			print('\n''  Copying check_server.py script to the instance...')
			cmd4 = 'scp -i ' + key + '.pem ~/devops/assignments/check_server.py ec2-user@' + ip + ':~'
			(status, output) = subprocess.getstatusoutput(cmd4)

			if status == 0:
				print('\n''  File copied successfully ')
			else:
				print('\n''  File not copied!')

			cmd5 = 'ssh -i ' + key + '.pem ec2-user@' + ip + ' chmod +x check_server.py'
			(status, output) = subprocess.getstatusoutput(cmd5)

			if status == 0:
				print('\n''  Check_server.py changed to executable')
				break
			else:
				print('\n''  Operation failed!')
				break
		#AWS error and exception handling
		except ValueError:
			print('\n''  No valid credentials entered!')
			break

#Defining a main() function
def main():
	instance_server()
# This is the standard boiler plate that calls the main() function
if __name__ == '__main__':
	main()