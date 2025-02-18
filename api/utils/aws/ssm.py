# -*- coding: utf-8 -*-
from typing import Any, Union, Dict

import logging
import boto3
import Environment as env

__all__ = ["get_parameter"]

LAYER_NAME = "ssm"

parameters = boto3.client('ssm')
PARAMETERS_PREFIX = f"/{env.ENVIRONMENT}/{env.APP_NAME}"


def get_parameter(ssm_name, *,
                  use_prefix: bool = True) -> Union[Dict[str, Any], str]:
    """
    Get a parameter from SSM service on aws.

    Parameters
    ----------
    use_prefix
    ssm_name : str
        The name of the parameter to get.
    default : str
        The default value to return if the parameter is not found.
    transform : bool
        If the parameter value is a json string you can pass this laike true and get the value like dict object.

    Returns
    -------
    str
        The value of the parameter.

    Raises
    ------
    ValueError
        If the parameter is not found and no default value is provided.

    Examples
    --------
    >>> from core_aws.ssm import get_parameter
    >>> get_parameter("/my/parameter")

    """
    ssm_name = f"{PARAMETERS_PREFIX}/{ssm_name}" if use_prefix else ssm_name
    try:
        value = parameters.get_parameter(Name=ssm_name)
    except Exception as e:
        logging.warning(e)
        raise e
    logging.debug(f"Value for {ssm_name}: {value['Parameter']['Value']}")

    return value['Parameter']['Value']
