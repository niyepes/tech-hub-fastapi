from abc import ABC, abstractmethod
from src.resources.domain.models import Resource

class ResourceRepository(ABC):
    @abstractmethod
    def all(self) -> list[Resource]:
        pass

    @abstractmethod
    def save(self, resource: Resource) -> None:
        pass