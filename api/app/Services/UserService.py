from isiflask_core.app.Services.BaseService import BaseService
from api.app.Data.Models import User


class UserService(BaseService):
    def __init__(self) -> None:
        super().__init__(User)