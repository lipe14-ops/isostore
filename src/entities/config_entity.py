import utils.strings
from dataclasses import dataclass
from pathlib import Path

@dataclass
class ConfigEntityDTO:
    download_dir: str
    extraction_dir: str

    def __call__(self) -> None:
        self.download_dir = utils.strings.sanitize_path_string(self.download_dir)
        self.extraction_dir = utils.strings.sanitize_path_string(self.extraction_dir)

    def is_valid(self) -> bool:
        return Path(self.download_dir).is_dir() and Path(self.extraction_dir).is_dir()

    @classmethod
    def from_dict(cls, data: dict[str, str]):
        config_object = cls(**data)
        config_object.download_dir = str(Path(config_object.download_dir).expanduser())
        config_object.extraction_dir = str(Path(config_object.extraction_dir).expanduser())
        return config_object