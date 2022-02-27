from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from .db_config import Base


class Employee(Base):
    __tablename__ = 'employee'

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    salary = Column("salary", Integer)
    factory = Column("factory", Integer, ForeignKey("factory.id"))

    # factory_table = relationship("Factory", back_populates="employee")

    def __init__(self, emp_id, name, salary, factory):
        self.id = emp_id
        self.name = name
        self.salary = salary
        self.factory = factory
