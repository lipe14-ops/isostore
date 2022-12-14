from abc import ABC, abstractmethod
from typing import Any

class IService(ABC):
    @abstractmethod
    def run(self) -> Any:
        """run the service."""