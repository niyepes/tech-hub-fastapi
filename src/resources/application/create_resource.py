from resources.domain.repositories import ResourceRepository

class CreateResource:
    def __init__(self, resource_repository: ResourceRepository):
        self._resource_repository = resource_repository
    def execute(self) -> None:
        # Logic to create a new resource
        pass