import json

import logging
import boto3
import Environment as env

LAYER_NAME = "secret_manager"

parameters = boto3.client('secretsmanager')
SECRETS_PREFIX = f"{env.ENVIRONMENT}-{env.APP_NAME}"


def get_secret(secret_name: str, use_prefix: bool = True, isJson=False):
    secret_name = f"{SECRETS_PREFIX}-{secret_name}" if use_prefix else secret_name
    try:
        value = parameters.get_secret_value(SecretId=secret_name)
    except Exception as e:
        logging.warning(e)
        raise e
    return value['SecretString'] if not isJson else json.loads(value['SecretString'])
