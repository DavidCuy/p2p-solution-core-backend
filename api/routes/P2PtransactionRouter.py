from flask import Blueprint
from api.app.Controllers.P2PtransactionController import index, find, request_transaction
from api.app.Services.P2PtransactionService import P2PtransactionService

p2ptransaction_router = Blueprint('p2ptransaction', __name__)
p2ptransaction_service = P2PtransactionService()

p2ptransaction_router.route('/', methods=['GET'], defaults={'service': p2ptransaction_service}) (index)
p2ptransaction_router.route('/<id>', methods=['GET'], defaults={'service': p2ptransaction_service}) (find)
p2ptransaction_router.route('/', methods=['POST'], defaults={'service': p2ptransaction_service}) (request_transaction)