import json

def get_choise_astr(file_path:str = "astronomy.json", choise_id:int|None = None) -> list[dict]|dict:
    with open(file_path, 'r', encoding='utf-8') as f:
        choises = json.load(f)
        if not choise_id is None and choise_id < len(choises):
            return choises[choise_id]
        return choises

def get_choise_math(file_path:str = "math.json", choise_id:int|None = None) -> list[dict]|dict:
    with open(file_path, 'r', encoding='utf-8') as f:
        choises = json.load(f)
        if not choise_id is None and choise_id < len(choises):
            return choises[choise_id]
        return choises

def get_choise_python(file_path:str = "python.json", choise_id:int|None = None) -> list[dict]|dict:
    with open(file_path, 'r', encoding='utf-8') as f:
        choises = json.load(f)
        if not choise_id is None and choise_id < len(choises):
            return choises[choise_id]
        return choises