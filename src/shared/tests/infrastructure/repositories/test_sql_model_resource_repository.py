import pytest
from sqlmodel import SQLModel, Session, select
from resources.domain.models import Resource
from resources.domain.value_objects import ResourceUrl
from resources.infrastructure.repositories import SQLModelResourceRepository, engine, ResourceModel

class TestSQLModelResourceRepository:

    @pytest.fixture(autouse=True)
    def clean_up_database(self):
        yield
        SQLModel.metadata.drop_all(engine)

    
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
        assert resources[0] == Resource(ResourceUrl(value="https://google.com"))

