#!/usr/bin/python3

# A Pyton3 script to check if nginx webserver is running
# if not running - it installs and starts nginx

def check_server():

	import sys
	import subprocess
	from time import sleep

	#installing nginx server
	print('\n''  Installing nginx...')
	cmd = 'sudo yum -y install nginx' 
	sleep(40)

	# Checking in nginx is installed runnig
	cmd1 = 'ps -A | grep nginx | grep -v grep'
	(status, output) = subprocess.getstatusoutput(cmd)

	if status > 0:
		while status > 0:
			print('\n''  Nginx Server IS NOT running')		

			# Starting nginx
			print('\n''  Starting  nginx...')
			cmd3 = 'sudo service -y nginx start'
			sleep(6)
	else:
		print('\n''  Nginx Server IS running')

# Define a main() function.
def main():
    check_server()
      
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()