from abc import ABC, abstractmethod
from typing import Any

class IRepository(ABC):

    @abstractmethod
    def add(self, data: Any) -> Any:
        """add new data to respository"""
    
    @abstractmethod
    def list_all(self) -> Any:
        """list all content from source."""