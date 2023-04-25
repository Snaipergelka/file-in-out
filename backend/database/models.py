from sqlalchemy import Column, Integer, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PhotoInfo(Base):
    __tablename__ = "photo_info"

    id = Column("Photo id", Integer, primary_key=True)
    size = Column("Photo size", Integer)
    created_at = Column("Created at", TIMESTAMP, server_default=func.now())

    def __str__(self):
        return self.id
