from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

from .db_config import Base


class Factory(Base):
    __tablename__ = 'factory'

    factory_id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    code_bonus = Column("code_bonus", Integer)

    employee_table = relationship("Employee")

    def __init__(self, factory_id, name, code_bonus):
        self.factory_id = factory_id
        self.name = name
        self.code_bonus = code_bonus
