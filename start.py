#Scrip Start

import boto3
region = 'us-west-2'
instances = ['i-091e60ababe060baa']

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)
    print 'Ligando a Instancia: ' + str(instances)
