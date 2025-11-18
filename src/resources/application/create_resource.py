from resources.domain.repositories import ResourceRepository
from resources.domain.models import Resource
from dataclasses import dataclass

@dataclass
class CreateResourceCommand:
    resource_url : str

class CreateResource:
    def __init__(self, resource_repository: ResourceRepository):
        self._resource_repository = resource_repository

    def execute(self, command: CreateResourceCommand) -> None:
        self._resource_repository.save(Resource())