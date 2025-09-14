from abc import ABC, abstractmethod

class ResourceRepository(ABC):
    @abstractmethod
    def get(self)-> Resource:
        pass