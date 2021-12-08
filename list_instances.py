import boto3
import sys
import json


client = boto3.client('ecs')

def list_containers(cluster_name):
    # list all container instances id 
    response = client.list_container_instances(
        cluster=cluster_name
    )
    return response['containerInstanceArns']

def describe_container():
    # get terraform query json and assign it to a dict
    query=sys.stdin.readlines()
    respone=json.loads(query[0])
    cluster_name=respone['cluster_name']

    # get the container instances
    response = client.describe_container_instances(
    cluster=cluster_name,
        containerInstances=list_containers(cluster_name)
    )

    # get the instance id's and assign to a variable
    instances=list(map(lambda x:x['ec2InstanceId'],response['containerInstances']))
    # assign them to our original query json (dict)
    respone['instances_id\'s']=instances

    # return as stdout
    output = json.dumps({str(key): str(value) for key, value in respone.items()})
    sys.stdout.write(output)


if __name__ == '__main__':
    describe_container()