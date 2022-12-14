from services.service_interface import IService
from entities import ConfigEntityDTO
import json


class ConfigLoadService(IService):
    def __init__(self, config_file: str) -> None:
        self._file_path = config_file
    
    def run(self) -> ConfigEntityDTO:
        with open(self._file_path, 'r') as file:
            json_file = json.load(file)
        return ConfigEntityDTO.from_dict(json_file)