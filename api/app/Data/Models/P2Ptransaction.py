from typing import Any, Dict, List
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from isiflask_core.app.Data.BaseModel import BaseModel
import Environment as env

class P2Ptransaction(BaseModel):
    """ Table P2Ptransactions Database model

    Args:
        BaseModel (ORMClass): Parent class

    Returns:
        P2Ptransaction: Instance of model
    """
    __tablename__ = 'p2p_transaction'
    __table_args__ = {"schema": env.DB_SCHEMA}
    id = Column("id", Integer, primary_key=True)
    source_id = Column("source_id", Integer)
    dest_id = Column("dest_id", Integer)
    amount = Column("amount", Float)
    status = Column("status", String, default="created")
    created_at = Column("created_at", DateTime, default=func.now())
    
    model_path_name = "p2ptransaction"

    filter_columns = [
        "id",
        "source_id",
        "status"
    ]
    relationship_names = []
    search_columns = [
        "amount",
        "created_at"
    ]
    
    @classmethod
    def property_map(self) -> Dict:
        return { }
    
    @classmethod
    def display_members(cls_) -> List[str]:
        return [
            "id",
            "source_id",
            "dest_id",
            "amount",
            "status",
            "created_at"
        ]
    
    @classmethod
    def rules_for_store(cls_) -> Dict[str, List[Any]]:
        return {
            "source_id": ["required", "numeric"],
            "dest_id": ["required", "numeric"],
            "amount": ["required", "numeric"]
        }