import boto3

session = boto3.Session(profile_name='Jim')
ec2 = session.resource('ec2', region_name='us-east-1')

def instance_rebooter():

  # Regex in boto3 seems to be limited based on documentation I could find. '?' is a placeholder for any single character
  # while '*' takes care of anything afterwards. Created an instance in my own AWS account named "Web-Server-blah" and the script worked.
  # confirmed by CloudTrail
    filters= [{'Name':'tag:Name','Values':['?eb-Server*']}] 

    instances = ec2.instances.filter(Filters=filters)

    for instance in instances:
        for tags in instance.tags:
            if tags["Key"] == 'Name':
                name = tags["Value"]
                instance.reboot()


instance_rebooter()


# # '^web-server.*' to reboot all instances with web-server leading the name
# # 'us-east-[1-3]' to reboot anything in us-east
# # '.*' to reboot all instances
