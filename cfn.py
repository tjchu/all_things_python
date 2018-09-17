#!/usr/local/bin/python3
import boto3
import json



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
		client = boto3.client('cloudformation')

	if not client:
		raise ValueError('Not able to initialize boto3 client with configuration.')
	else:
		logging.info("CloudFormation client created.")
		return client

#setup the model
template_object = get_json(args.templateurl)
params = make_kv_from_args(args.params, "Parameter", False)
tags = make_kv_from_args(args.tags)
response = client.create_stack(
    StackName=args.name,
    TemplateBody=json.dumps(template_object),
    Parameters=params,
    DisableRollback=False,
    TimeoutInMinutes=2,
    NotificationARNs=[args.topicarn],
    Tags=tags
)

