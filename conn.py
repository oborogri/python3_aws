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

	conn = boto.ec2.connect_to_region('us-west-2')
	print('\n''  Connection successful: ' + str(conn))
	print(conn)
	sleep(1)

	key = input('\n''  Please enter your key file name (without extension): ')
	sec_group = input('\n''  Please enter your security group name: ')
	reservation = conn.run_instances('ami-b04e92d0', key_name = key, instance_type = 't2.micro', security_groups=[sec_group])
	sleep(3)
	instance = reservation.instances[0]
	instance.update()
	print(instance.id)
	print(instance.state)
	print(instance.ip_address)
	print('bye!')
	sleep(2)

# Defining a main() function
def main():
	create_instance()

# This is the standard boiler plate that calls the main() function
if __name__ == '__main__':
	main()
