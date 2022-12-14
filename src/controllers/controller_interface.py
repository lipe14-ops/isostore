from abc import ABC, abstractmethod

class IController(object):
    @abstractmethod
    def handle(self) -> None:
        """handle the controller responsabilities."""