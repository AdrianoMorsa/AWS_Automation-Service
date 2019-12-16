#Script Stop


import boto3
region = 'us-west-2'
instances = ['i-091e60ababe060baa']

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=instances)
    print 'Desligando a Instancia: ' + str(instances)
   


