from handlers.handler_interface import IHandler
import requests

class DownloadHandler(IHandler):
    def __init__(self, file_url: str, filename: str) -> None:
        self._file_url = file_url
        self.filename = filename
        
    def execute(self, download_dir: str = '.') -> None:
        response =  requests.get(self._file_url)

        if not download_dir.endswith("/"):
            download_dir += '/'

        with open(f"{download_dir}{self.filename}", "wb") as file:
            file.write(response.content)
            