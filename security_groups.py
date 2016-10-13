#!/usr/bin/python3

# A Python script to define and configure an AWS security group called 'httpssh' for AWS

def sec_group():
	import boto
	import boto.ec2
	from time import sleep

	# Establishing conection with AWS
	conn = boto.ec2.connect_to_region('us-west-2')

	while True:
		try:
			secgroup = conn.create_security_group('httpssh', 'Only HTTP and SSH')

			# creating HTTP traffic rules
			secgroup.authorize('tcp', 80, 80, '0.0.0.0/0')
			# creating SSH traffic rules
			secgroup.authorize('tcp', 22, 22, '0.0.0.0/0')
			# the rule ‘0.0.0.0/0’	indicates	authorization	of	traffic	from	any IP	address

			print('\n''  Security group created successfully!')
			print('\n''  Group name: \'httpssh\'')
			sleep(2)
			break

		except boto.exception.EC2ResponseError:
			print('\n''  A security group called \'httpssh\' already exists for this VPC')
			sleep(1)
			break
	print('\n''  Enter this security group name when prompted')
	sleep(1)
	print('\n''  Proceed to next step!''\n')
	sleep(2)

# Defining a main() function
def main():
	sec_group()

# This is the standard boiler plate that calls the main() function
if __name__ == '__main__':
	main()