from sqlalchemy import INTEGER, Column, DateTime, String, func
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id = Column(INTEGER(), primary_key=True)
    create_at = Column(DateTime(), server_default=func.now())
    update_at = Column(DateTime(), server_default=func.now(), server_onupdate=func.now())

class Url(BaseModel):
    __tablename__ = "urls"
    url = Column(String(length=1024))
    hash = Column(String(length=7), unique=True)
    def to_dict(self):
        return {"url": self.url, "hash": self.hash}
