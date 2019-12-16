
##Scrip Start with variable

import boto3
region = 'us-west-2'

def lambda_handler(event, context):
    instances = event['instance']
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=[instances])
    print 'stopped your instances: ' + str(instances)
