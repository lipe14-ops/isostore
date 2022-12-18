from controllers import GameInstallerController
from handlers import GameSearcherHandler
from services import ConfigLoadService
from pathlib import Path
import platform

LINUX_MIRROR_LIST_PATH = Path('/opt/isostore/res/games-mirror-list.csv')
LINUX_CONFIG_FILE_PATH = Path('~/.config/isostore/config.json').expanduser()

WINDOWS_MIRROR_LIST_PATH = Path('./res/games-mirror-list.csv')
WINDOWS_CONFIG_FILE_PATH = Path('./config.json')


def main() -> None:
    config_file_path = LINUX_CONFIG_FILE_PATH if platform.system() == 'Linux' else WINDOWS_CONFIG_FILE_PATH 
    mirror_file_path = LINUX_MIRROR_LIST_PATH if platform.system() == 'Linux' else WINDOWS_MIRROR_FILE_PATH  

    config_loader = ConfigLoadService(config_file=config_file_path)
    user_config = config_loader.run()

    if not config_file_path.is_file():
        print("you must have a config file.")
        exit(1)

    if not user_config.is_valid():
        print("your config file must have valid directories.")
        exit(1)

    installer=GameInstallerController(config=user_config)
    searcher=GameSearcherHandler(repository_path=mirror_file_path)

    print("[0] - search\n[1] - download\n[2] - quit")
    while True:
        command_code = input("command code: ( h for help. ) ")
        if command_code in ["q", "2"]:
            print("goodbye!!!")
            exit()

        elif command_code in ["help", "h"]:
            print("[0] - search\n[1] - download\n[2] - quit")
            
        elif command_code == "0":
            game_name = input("search game: ")
            games_list = searcher.execute(game_name)

            if not games_list:
                print("games not found.")
                continue

            for game in games_list:
                print(f"> {game.name} <")

        elif command_code == "1":
            game_name = input("search game: ")
            games_list = searcher.execute(game_name)

            if not games_list:
                print("games not found.")
                continue
            
            for index, game in enumerate(games_list):
                print(f"[{index}] - {game.name}")
            
            game_index = int(input("enter the game code: "))
            if 0 < game_index > len(games_list) - 1:
                print("game code is not valid.")
                continue

            selected_game = games_list[game_index]
            print(f"Downloading \"{selected_game.name}\"... It will take a while to get done.")
            installer.handle(selected_game)
            print("game installed. Have fun!!!")
        else:
            print(f"command code \"{command_code}\" is not valid. use the command \"help\".")
    
if __name__ == "__main__":
    main()
