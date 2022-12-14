from repositories.repository_interface import IRepository
from services import IService, CsvLoadService
from entities import GameEntityDTO

class GameDataRepository(IRepository):
    def __init__(self, repository_path: str, reader: IService = CsvLoadService) -> None:
        self._repository_path = repository_path
        self._state: list[GameEntityDTO] = []
        self.__setup_data()

    def __setup_data(self, reader: IService = CsvLoadService) -> list[GameEntityDTO]:
        csv_reader = reader(self._repository_path)
        for data in csv_reader.run():
            self.add(data)

    def add(self, data: dict[str, str]) -> None:
        game = GameEntityDTO.from_dict(data)
        self._state.append(game)
    
    def list_all(self) -> list[GameEntityDTO]:
        return self._state