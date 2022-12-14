from handlers.handler_interface import IHandler
from repositories import IRepository, GameDataRepository
from entities import GameEntityDTO

class GameSearcherHandler(IHandler):
    def __init__(self, repository_path: str, repository: IRepository = GameDataRepository) -> None:
        self._repository_path = repository_path
        self._repository = repository(self._repository_path)

    def execute(self, game_seach_name: str) -> list[GameDataRepository]:
        output_game_list = []
        games_list = self._repository.list_all()

        for game in games_list:
            if game_seach_name.lower() in game.name.lower():
                output_game_list.append(game)
                continue

            splited_game_name = game_seach_name.split(" ")
            for name_particle in splited_game_name:
                if name_particle.lower() in game.name.lower():
                    output_game_list.append(game)
                    break
            
        return output_game_list

