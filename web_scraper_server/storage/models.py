from sqlalchemy import BigInteger, Column, String

from .database import Base


class Apartment(Base):
    __tablename__ = "apartments"

    id = Column(BigInteger, primary_key=True, index=True)
    title = Column(String)
    image = Column(String)
