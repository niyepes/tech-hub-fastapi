from resources.application.create_resource import CreateResource
from resources.domain.models import Resource
from resources.application.create_resource import CreateResourceCommand

class FakeResourceRepository:
    def __init__(self) -> None:
        self._resources = []

    def save(self, resource) -> None:
        self._resources.append(resource)

    def all(self) -> list[Resource]:
        return list(self._resources)

class TestCreateResource:
    def test_create_resource(self) -> None:
        resource_repository = FakeResourceRepository()
        CreateResource(resource_repository).execute(
            CreateResourceCommand(resource_url="resource-url-example")
        )
        resources = resource_repository.all()
        assert len(resources) == 1
        assert resources[0].url == "resource-url-example"

