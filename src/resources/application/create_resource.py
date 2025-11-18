from resources.domain.repositories import ResourceRepository
from resources.domain.models import Resource

class CreateResource:
    def __init__(self, resource_repository: ResourceRepository):
        self._resource_repository = resource_repository

    def execute(self) -> None:
        self._resource_repository.save(Resource())