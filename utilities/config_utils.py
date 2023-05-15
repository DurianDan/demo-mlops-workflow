import __main__
import yaml
from typing import Dict, Any
from pathlib import Path

def absolute_path(path:str) -> str:
    '''Normalize path, based on os platform

    E.g: absolute_path(`path\\to/something/main.py`)
     -> Windows: `D:\\projects\\task\\path\\to\\something\\main.py`
     -> Linux/MacOS: `$HOME/projects/task/path/to/something/main.py`
    '''
    
    result = Path(__main__.__file__)
    # join the parent folder path of 'result' to 'path'
    result = result.parent.joinpath(path) 

    if not result.exists():
        print(f"Warning!!! Path doesn't exist: {result}")
    return str(result)

def load_config(yaml_path:str) -> Dict[str,Any]:
    '''
    Load yaml config file
    '''
    with open(yaml_path, 'r') as f:
        return yaml.load(f, Loader=yaml.FullLoader)

def db_uri(
        type: str,
        username: str,
        password: str,
        host: str,
        name: str, 
        ) -> str:
    return f"{type}://{username}:{password}@{host}/{name}"