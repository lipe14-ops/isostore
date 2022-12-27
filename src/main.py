from controllers import GameInstallerController
from handlers import GameSearcherHandler
from constants.mirrors_files import MirrorsFilesConstant
from services import ConfigLoadService
from pathlib import Path
import platform
import sys

LINUX_MIRRORS_DIR = Path('/opt/isostore/res/mirrors')
LINUX_CONFIG_FILE_PATH = Path('~/.config/isostore/config.json').expanduser()

WINDOWS_MIRRORS_DIR = Path('./res/mirrors')
WINDOWS_CONFIG_FILE_PATH = Path('./config.json')


def get_console_mirror(mirror_dir_path: str) -> str | None:
        print("[0] - playstation 1\n[1] - playstation 2\n[2] - portable playstation")
        console_mirror_code =  int(input("console code: "))

        mirrors_files = [
            MirrorsFilesConstant.PS1,
            MirrorsFilesConstant.PS2,
            MirrorsFilesConstant.PSP,
        ]

        if  0 < console_mirror_code > len(mirrors_files) - 1:
            return
        
        return Path(f"{mirror_dir_path}/{mirrors_files[console_mirror_code]}")


def main() -> None:
    config_file_path = LINUX_CONFIG_FILE_PATH if platform.system() == 'Linux' else WINDOWS_CONFIG_FILE_PATH 
    mirror_dir_path = LINUX_MIRRORS_DIR if platform.system() == 'Linux' else WINDOWS_MIRRORS_DIR  

    if not config_file_path.is_file():
        print("you must have a config file.")
        sys.exit(1)

    config_loader = ConfigLoadService(config_file=config_file_path)
    user_config = config_loader.run()

    if not user_config.is_valid():
        print("your config file must have valid directories.")
        sys.exit(1)

    installer = GameInstallerController(config=user_config)

    print("[0] - search\n[1] - download\n[2] - quit")
    while True:
        command_code = input("command code: ( h for help. ) ")

        if command_code in ["q", "2"]:
            print("goodbye!!!")
            sys.exit()

        elif command_code in ["help", "h"]:
            print("[0] - search\n[1] - download\n[2] - quit")
            
        elif command_code == "0":
            mirror_file_path = get_console_mirror(mirror_dir_path)

            if not mirror_file_path:
                print("console code not valid.")
                continue

            searcher = GameSearcherHandler(repository_path=mirror_file_path)
            game_name = input("search game: ")
            games_list = searcher.execute(game_name)

            if not games_list:
                print("games not found.")
                continue

            for game in games_list:
                print(f"> {game.name} <")

        elif command_code == "1":
            mirror_file_path = get_console_mirror(mirror_dir_path)

            if not mirror_file_path:
                print("console code not valid.")
                continue

            searcher = GameSearcherHandler(repository_path=mirror_file_path)
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
