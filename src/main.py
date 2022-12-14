from controllers import GameInstallerController
from handlers import GameSearcherHandler
from services import ConfigLoadService
from pathlib import Path

MIRROR_LIST_PATH = Path("/opt/isostore/res/games-mirror-list.csv")
CONFIG_FILE_PATH = Path('~/.config/isostore/config.json').expanduser()


def main() -> None:
    config_loader = ConfigLoadService(CONFIG_FILE_PATH)
    user_config = config_loader.run()

    if not CONFIG_FILE_PATH.is_file():
        print("you must have a config file.")
        exit(1)

    if not user_config.is_valid():
        print("your config file must have valid directories.")
        exit(1)

    installer=GameInstallerController(user_config.download_dir, user_config.extraction_dir)
    searcher=GameSearcherHandler(MIRROR_LIST_PATH)

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
