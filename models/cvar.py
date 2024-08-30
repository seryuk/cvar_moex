import datetime as dt
from pydantic import BaseModel, Field

class CvarRequest(BaseModel):
    probability: float
    ticker: str
    cvar_date: dt.date
    cvar_period: int


class CvarResult(BaseModel):
    cvar:float
