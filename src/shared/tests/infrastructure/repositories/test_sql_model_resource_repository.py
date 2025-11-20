from sqlmodel import Session, select
from resources.domain.models import Resource
from resources.domain.value_objects import ResourceUrl
from resources.infrastructure.repositories import SQLModelResourceRepository, engine, ResourceModel

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
