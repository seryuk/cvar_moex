import datetime as dt
from pydantic import BaseModel, Field


class CvarRequest(BaseModel):
    probability: float #>=90 =<99,9
    ticker: str # not < 3 not >15
    cvar_date: dt.date # >= 2012/01/01
    cvar_period: int # =>1 <=10


class CvarResult(BaseModel):
    cvar:float #<=0
