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

	end = 1
	while end > 0:
		while True:
			try:
				# Establishing conection to	a particular	EC2	region on AWS. The	us-west-2 region	is	Oregon.
				conn = boto.ec2.connect_to_region('us-west-2')
				print('\n''  Connection successful: ' + str(conn))
				sleep(1)
				break
			except boto.exception.EC2ResponseError:
				print('\n''  A connection cannot be established at this time')
				sleep(1)
				break
				end = 0

		# creating the Amazon Linux AMI 2016.09.0 (HVM), SSD Volume Type - ami-b04e92d0
		while True:
			try:
				key = input('\n''  Please enter your private key file name: ')
				sec_group = ('\n''  Please enter your security group name: ')
				reservation = conn.run_instances('ami-b04e92d0', key_name = key, instance_type = 't2.micro', security_groups=[sec_group])
			
				sleep(3)
				instance = reservation.instances[0]

				# Tag the newly created instance
				tag = input('\n''  Please enter instance name tag: ')
				name = input('\n''  Please enter instance description: ')
				instance.add_tag(tag, name)

				instance.update()
		    	
				instate = instance.state
				inst_ip = instance.ip_address

				print('\n''  Instance state: ' + instate)
				sleep(1)
				print('\n''  Instance IP address: ' + inst_ip)

		    # Error and exception handling
			#except ValueError:
			#	print('\n''  No valid credentials entered!')
			#	break
			#	end = 0
			except boto.exception.EC2ResponseError:
				print('\n''  No valid credentials entered!')
				break
				end = 0

# Defining a main() function
def main():
	create_instance()

# This is the standard boiler plate that calls the main() function
if __name__ == '__main__':
	main()