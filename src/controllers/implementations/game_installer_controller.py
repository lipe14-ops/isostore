from controllers.controller_interface import IController
from entities import GameEntityDTO
import utils.strings
from handlers import DownloadHandler, FileExtractorHandler

class GameInstallerController(IController):
    def __init__(self, download_dir: str = '.', extraction_dir: str = '.') -> None:
        self._download_dir = utils.strings.sanitize_path_string(download_dir)
        self._extraction_dir = utils.strings.sanitize_path_string(extraction_dir)
    
    def handle(self, game: GameEntityDTO) -> None:
        game_filename = utils.strings.sanitize_zipped_filename(game.name, '.7z')

        download_handler = DownloadHandler(
            file_url=game.url, 
            filename=game_filename
        )
        file_extractor =  FileExtractorHandler(
            file_path=f'{self._download_dir}{game_filename}', 
            out_dir=self._extraction_dir
        )

        download_handler.execute(download_dir=self._download_dir)
        file_extractor.execute()
