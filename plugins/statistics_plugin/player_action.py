import datetime
from enum import Enum
from sqlalchemy import create_engine, Column, Integer, String, DateTime, \
    ForeignKey, Boolean, func

from sqlalchemy.ext.declarative import declarative_base
StatisticsBase = declarative_base()

class IntEnum(int, Enum):
    pass

class ActionTypes(IntEnum):
    CONNECTED = 0
    DISCONNECTED = 1

class PlayerAction(StatisticsBase):
    __tablename__ = 'player_actions'

    uuid = Column(String, primary_key=True)
    action_type = Column(Integer, primary_key=True)
    date_time = Column(DateTime, primary_key=True)
    
class PlayerChatLine(StatisticsBase):
    __tablename__ = 'player_chat_lines'

    uuid = Column(String, primary_key=True)
    date_time = Column(DateTime, primary_key=True)
    line = Column(String)

class PlayerWarps(StatisticsBase):
    __tablename__ = 'player_warps'

    uuid = Column(String, primary_key=True)
    date_time = Column(DateTime, primary_key=True)
    warp_type = Column(Integer)
    warp_target = Column(String)