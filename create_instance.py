#!/usr/bin/python3

# This script will create and launch a new Amazon EC2 instance
# AWS access keys are required to create the instance
# Securtiy groups need to be defined if none
# AWS credentials need to be defined in .boto file on local machine

def create_instance():
	import sys
	import boto
	import boto.ec2 
	import time
	from time import sleep
		
	while True:
		try:
			# Establishing conection to	a particular	EC2	region on AWS. The	us-west-2 region	is	Oregon.
			conn = boto.ec2.connect_to_region('us-west-2')
			print('\n''  Connection successful to: ' + str(conn))
			sleep(1)
			break
		# AWS connection error handling
		except boto.exception.AWSConnectionError:
			print('\n''  A connection cannot be established at this time')
			sleep(90)
			break

	# creating the Amazon Linux AMI 2016.09.0 (HVM), SSD Volume Type - ami-b04e92d0
	while True:
		try:
			def key():
				key = input('\n''  Please enter the fully qualified path to your AWS key file \'n''  (without any extension): ')
				return key

			sec_group = input('\n''  Please enter your security group name: ')
			reservation = conn.run_instances('ami-b04e92d0', key_name = key, instance_type = 't2.micro', security_groups=[sec_group])
			
			sleep(3)
			instance = reservation.instances[0]
			instance.update()
			sleep(5)

			# Adding a tag name to the newly created instance
			tag = input('\n''  Please enter instance name tag: ')
			#ame = input('\n''  Please enter instance description: ')
			instance.add_tag('Name', tag)

			instance.update()
			sleep(5)
			instate = instance.state
			print('\n''  Instance state: ' + instate)

			def ip():
				ip = instance.ip_address
				return ip
				
			sleep(1)
			print('\n''  Instance IP address: ' + inst_ip)
			print('\n''  Take a note of your instance public IP address!')
			sleep(4)

			choice = 0
			while choice == 0:
				choice = input('\n''  Press any key and hit return to continue... ')
				cmd = 'clear'
				print('\n''  Initializing the instance....')
				sleep(140)
				print('\n''  Returning to the main menu')
				sleep(1)
				break
			break
							
	    # AWS error and exception handling
		except boto.exception.EC2ResponseError:
			print('\n''  No valid credentials entered!')
			break
				
#Defining a main() function
def main():
	create_instance()
	
# This is the standard boiler plate that calls the main() function
if __name__ == '__main__':
	main()