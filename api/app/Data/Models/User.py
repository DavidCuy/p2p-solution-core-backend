from typing import Any, Dict, List
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from isiflask_core.app.Data.BaseModel import BaseModel
import Environment as env

class User(BaseModel):
    """ Table Users Database model

    Args:
        BaseModel (ORMClass): Parent class

    Returns:
        User: Instance of model
    """
    __tablename__ = 'users'
    __table_args__ = {"schema": env.DB_SCHEMA}
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    unique_id = Column("unique_id", String)
    created_at = Column("created_at", DateTime, default=func.now())
    
    model_path_name = "user"

    filter_columns = [
        "id",
        "unique_id"
    ]
    relationship_names = []
    search_columns = [
        "name"
    ]
    
    @classmethod
    def property_map(self) -> Dict:
        return { }
    
    @classmethod
    def display_members(cls_) -> List[str]:
        return [
            "id",
            "name",
            "unique_id",
            "created_at"
        ]
    
    @classmethod
    def rules_for_store(cls_) -> Dict[str, List[Any]]:
        return {
            
        }