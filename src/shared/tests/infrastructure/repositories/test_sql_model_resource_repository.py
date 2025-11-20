import pytest
from sqlmodel import SQLModel, Session, select
from resources.domain.models import Resource
from resources.domain.value_objects import ResourceUrl
from resources.infrastructure.repositories import SQLModelResourceRepository, engine, ResourceModel


@pytest.fixture(autouse=True)
def create_test_database():
    # Limpia la DB y crea todas las tablas para cada test
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    yield
    # Limpia al final también (opcional)
    SQLModel.metadata.drop_all(engine)

class TestSQLModelResourceRepository:

    def test_save_resource_to_database(self)-> None:
        
        #Arrange/Given
        repo = SQLModelResourceRepository()
        #Act/When
        repo.save(Resource(ResourceUrl(value = "https://google.com")))

        #Assert/Then
        with Session(engine) as session:
            statement = select(ResourceModel)
            resource = session.exec(statement).first()
            resource.url == "https://google.com"

    def test_returns_all_resources(self) -> None:
        
        #Arrange/Given
        with Session(engine) as session:
            session.add(ResourceModel(url="https://google.com"))
            session.commit()

        #Act/When
        resources = SQLModelResourceRepository().all()

        #Assert/Then
        assert len(resources) == 1
        assert resources[0].get_url() == ResourceUrl(value="https://google.com")

