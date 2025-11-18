from resources.application.create_resource import CreateResource
from resources.domain.models import Resource
from resources.domain.value_objects import ResourceUrl
from resources.application.create_resource import CreateResourceCommand
from resources.domain.exceptions import UrlNotValidException

import pytest as pytest

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
            CreateResourceCommand(resource_url="https://google.com")
        )
        resources = resource_repository.all()
        assert len(resources) == 1
        assert resources[0].get_url() == ResourceUrl(value="https://google.com")
    def test_raise_exception_when_resource_url_is_not_valid (self) -> None:
        resource_repository = FakeResourceRepository()

        with pytest.raises(UrlNotValidException):
            CreateResource(resource_repository).execute(
                CreateResourceCommand(resource_url="resource-url-example-not-valid")
        )
        resources = resource_repository.all()
        assert len(resources) == 0

