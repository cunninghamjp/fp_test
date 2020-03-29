import boto3
import re #imported for use with regex

session = boto3.Session(profile_name='<aws profile name>')
ec2 = session.resource('ec2')

for instance in ec2.instances.all():
    ec2_attributes = [instance.placement,instance.tags]



# Trying to do a if/then to look for AZ or Web Server regex to initiate the reboot but getting errors.
# Spent most of my time trying to debug this issue, would love to see where I went wrong so I don't make same mistake again.

#Tested to see if below actions work, confirmed they do by looking through CloudTrail logs.
for instances in ec2.instances.all():
    instance.reboot()


print(ec2_attributes[1]) # Prints: '[{'Key': 'Name', 'Value': 'web-server-blah'}]' to get name of my EC2
print(ec2_attributes[0]) # Prints: '{'AvailabilityZone': 'us-east-1a', 'GroupName': '', 'Tenancy': 'default'}' to pull AZ


# '^web-server.*' to reboot all instances with web-server leading the name
# 'us-east-[1-3]' to reboot anything in us-east
# '.*' to reboot all instances
