import json
import os
from pydantic import BaseModel
from typing import Literal, List, Dict, Any, Optional

DEFAULT_CONFIG_PATH = './hinabot/core/config_default.json'

def load_config(source):
    if isinstance(source, str):
        if not os.path.isfile(source):
            raise FileNotFoundError(f'Config file not found at {source}')
        with open(source, 'r', encoding='utf-8') as f:
            config_data = json.load(f)
    elif isinstance(source, dict):
        config_data = source
    else:
        raise TypeError('Config source must be a file path or a dictionary.')
    return Config(**config_data)

def _load_jason_file(filename: str) -> Dict[str, Any]:
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

class Config(BaseModel):
    release: Literal['development', 'release', 'beta']
    token: str
    prefix: str
    restricted_mode: dict
    blocked_users: List[int]