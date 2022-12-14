from dataclasses import dataclass

@dataclass
class GameEntityDTO:
    name: str
    url: str

    @classmethod
    def from_dict(cls, data: dict[str, str]):
        return cls(**data)