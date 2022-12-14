from services.service_interface import IService
import py7zr

class SevenzipFileExtractionService(IService):
    def __init__(self, file_path: str, out_dir: str) -> None:
        self._file_path = file_path
        self._out_dir = out_dir

    def run(self) -> None:
        with py7zr.SevenZipFile(self._file_path, mode='r') as file:
            file.extractall(self._out_dir)
