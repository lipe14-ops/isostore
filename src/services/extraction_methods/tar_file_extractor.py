from services.service_interface import IService
import tarfile

class TarFileExtractionService(IService):
    def __init__(self, file_path: str, out_dir: str) -> None:
        self._file_path = file_path
        self._out_dir = out_dir

    def run(self) -> None:
        with tarfile.open(self._file_path) as sevenzip_file:
            sevenzip_file.extractall(self._out_dir)