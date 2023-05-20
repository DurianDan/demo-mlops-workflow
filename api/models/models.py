from sqlalchemy import Column, Integer
from db import Base


class Data(Base):
    """help interact with a table in MySQL server"""

    __tablename__ = "Data"
    id = Column(Integer, primary_key=True, index=True)
    