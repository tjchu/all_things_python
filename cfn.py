#!/usr/local/bin/python3
import boto3
import json
import argparse
import logging

#Parameters to pass into this script
parser = argparse.ArgumentParser(description="Inputs needed to run the Release Notes Generator")
parser.add_argument('--template', '-t', action='store', dest='templatepath' ,help='File path to CloudFormation JSON temple')
parser.add_argument('--name', '-n', action='store', dest='name' ,help='Stack name')
parser.add_argument('--params', '-p', action='store', dest='params' ,help='Parameters')
parser.add_argument('--region', '-r', action='store', dest='region' ,help='Region')
args = parser.parse_args()

def make_cloudformation_client(config=None):
	"""
	this method will attempt to make a boto3 client
	it manages the choice for a custom config
	"""
	#load the app config
	client = None
	if config != None:
		logging.info("Using custom config.")
		config = load_config(args.config)
		client = boto3.client('cloudformation',
		config["AWS_REGION_NAME"],
		aws_access_key_id=config["AWS_ACCESS_KEY_ID"],
		aws_secret_access_key=config["AWS_SECRET_ACCESS_KEY"])
	else:
		# we dont have a configuration, lets use the
		# standard configuration fallback
		logging.info("using default config.")
		client = boto3.client('cloudformation', args.region)

	if not client:
		raise ValueError('Not able to initialize boto3 client with configuration.')
	else:
		logging.info("CloudFormation client created.")
		return client

#setup the model
with open(args.templatepath) as json_data:
	template_object = json.load(json_data)
#params = make_kv_from_args(args.params, "Parameter", False)
#tags = make_kv_from_args(args.tags)
new_client = make_cloudformation_client()
response = new_client.create_stack(
    StackName=args.name,
    TemplateBody=json.dumps(template_object),
    DisableRollback=False,
    TimeoutInMinutes=2,
)

