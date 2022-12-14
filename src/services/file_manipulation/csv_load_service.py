from services.service_interface import IService
from entities import GameEntityDTO
import csv

class CsvLoadService(IService):
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path

    def run(self) -> list[dict]: 
        with open(self._file_path, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            return [data for data in csv_reader]