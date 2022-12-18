from controllers.controller_interface import IController
from entities import GameEntityDTO, ConfigEntityDTO
import utils.strings
from handlers import DownloadHandler, FileExtractorHandler

class GameInstallerController(IController):
    def __init__(self, config: ConfigEntityDTO) -> None:
        self._config = config
        self._config.download_dir = utils.strings.sanitize_path_string(self._config.download_dir)
        self._config.extraction_dir = utils.strings.sanitize_path_string(self._config.extraction_dir)
    
    def handle(self, game: GameEntityDTO) -> None:
        game_filename = utils.strings.sanitize_zipped_filename(game.name, '.7z')

        download_handler = DownloadHandler(
            file_url=game.url, 
            filename=game_filename
        )
        file_extractor =  FileExtractorHandler(
            file_path=f'{self._config.download_dir}{game_filename}', 
            out_dir=self._config.extraction_dir
        )

        download_handler.execute(download_dir=self._config.download_dir)
        file_extractor.execute()
