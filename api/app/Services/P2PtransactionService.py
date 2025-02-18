from isiflask_core.app.Services.BaseService import BaseService
from api.app.Data.Models import P2Ptransaction


class P2PtransactionService(BaseService):
    def __init__(self) -> None:
        super().__init__(P2Ptransaction)