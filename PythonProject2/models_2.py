from pydantic import BaseModel
from aiogram.fsm.state import State, StatesGroup

class Choise_2(BaseModel):
    name : str
    poster : str
    description : str
    link : str
