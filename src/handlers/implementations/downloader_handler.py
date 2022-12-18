from handlers.handler_interface import IHandler
import utils.strings
import requests
import shutil

class DownloadHandler(IHandler):
    def __init__(self, file_url: str, filename: str) -> None:
        self._file_url = file_url
        self.filename = filename
        
    def execute(self, download_dir: str = '.') -> None:
        response =  requests.get(self._file_url, stream=True)

        download_dir = utils.strings.sanitize_path_string(download_dir)

        with open(f"{download_dir}{self.filename}", "wb") as file:
            shutil.copyfileobj(response.raw, file)