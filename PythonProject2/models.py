from pydantic import BaseModel
from aiogram.fsm.state import State, StatesGroup

class ChoiseStates(StatesGroup):
    search_thema = State()
    search_thema_2 = State()
    filter_astronomy = State()
    random_astronomy = State()
    random_math = State()
    random_python = State()

class Choise(BaseModel):
    name : str
    type : str
    poster : str
    description : str
