import datetime
from enum import Enum
from sqlalchemy import create_engine, Column, Integer, String, DateTime, \
    ForeignKey, Boolean, func
from sqlalchemy.ext.declarative import declarative_base
StatisticsBase = declarative_base()

class IntEnum(int, Enum):
    pass

class ActionTypes(IntEnum):
    GUEST = 0
    REGISTERED = 1
    MODERATOR = 2
    ADMIN = 3
    OWNER = 4

class PlayerAction(StatisticsBase):
    __tablename__ = 'player_actions'

    uuid = Column(String, primary_key=True)
    action_type = Column(Integer, primary_key=True)
    date_time = Column(DateTime, primary_key=True)
    
class ChatLine(StatisticsBase):
    __tablename__ = 'chat_lines'

    uuid = Column(String, primary_key=True)
    date_time = Column(DateTime, primary_key=True)
    line = Column(String)