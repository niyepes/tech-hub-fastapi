from resources.domain.repositories import ResourceRepository
from resources.domain.models import Resource
from resources.domain.value_objects import ResourceUrl

from dataclasses import dataclass

@dataclass
class CreateResourceCommand:
    resource_url : str

class CreateResource:
    def __init__(self, resource_repository: ResourceRepository):
        self._resource_repository = resource_repository

    def execute(self, command: CreateResourceCommand) -> None:
        resource_url = ResourceUrl(value = command.resource_url)
        resource = Resource.create(resource_url = resource_url)
        self._resource_repository.save(resource)