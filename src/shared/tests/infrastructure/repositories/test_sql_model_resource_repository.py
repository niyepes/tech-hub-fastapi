from resources.domain.models import Resource
from resources.domain.value_objects import ResourceUrl

class TestSQLModelResourceRepository:
    
    def test_save_resource_to_database(self)-> None:
        
        #Arrange/Given
        repo = SQLModelResourceRepository()
        #Act/When
        repo.save(Resource(ResourceUrl("https://google.com")))

        #Assert/Then
        with Session(engine) as session:
            statement = select(ResourceModel)
            resource = session.exec(statement)
            esource.url == "https://google.com"
