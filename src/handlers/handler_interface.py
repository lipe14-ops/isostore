from abc import ABC, abstractmethod
from typing import Any

class IHandler(ABC):
    @abstractmethod
    def execute(self) -> Any:
        """handle the child class propouse"""
