from handlers.handler_interface import IHandler
from services import IService
from services.extraction_methods.sevenzip_file_extractor import SevenzipFileExtractionService

class FileExtractorHandler(IHandler):
    def __init__(self, file_path: str, out_dir: str, extraction_method: IService = SevenzipFileExtractionService) -> None:
        self._file_path = file_path
        self._out_dir = out_dir
        self._extraction_method = extraction_method(self._file_path, self._out_dir)
    
    def execute(self) -> None:
        self._extraction_method.run()
