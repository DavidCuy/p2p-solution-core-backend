from isiflask_core.app.Controllers.BaseController import index, find

import json
from flask import request
import logging
from isiflask_core.app.Data.Enum.http_status_code import HTTPStatusCode

from isiflask_core.app.Exceptions.APIException import APIException
from isiflask_core.app.Validators.RequestValidator import RequestValidator

from isiflask_core.database.DBConnection import AlchemyEncoder, get_session
from isiflask_core.utils.http_utils import build_response

from ..Data.Models import P2Ptransaction
from ..Services import P2PtransactionService

from api.utils.aws.ssm import get_parameter
from api.utils.aws.sqs import send_message_to_queue

QUEUE_NAME = get_parameter(ssm_name='p2p/transaction-queue')

def request_transaction(service: P2PtransactionService):
    session = get_session()
    
    RequestValidator(session, service.get_rules_for_store()).validate()
    input_params = request.get_json()

    try:
        body = service.insert_register(session, input_params)
        response = json.dumps(body, cls=AlchemyEncoder)
        send_message_to_queue(QUEUE_NAME, response)
        status_code = HTTPStatusCode.OK.value
    except APIException as e:
        logging.exception("APIException occurred")
        response = json.dumps(e.to_dict())
        status_code = e.status_code
    except Exception:
        logging.exception("No se pudo realizar la consulta")
        body = dict(message="No se pudo realizar la consulta")
        response = json.dumps(body)
        status_code=HTTPStatusCode.UNPROCESABLE_ENTITY.value
    finally:
        session.close()
    
    return build_response(status_code, response, is_body_str=True)
    pass