from sqlmodel import SQLModel, Field, create_engine, Session
from resources.domain.models import Resource
from resources.domain.repositories import ResourceRepository

class ResourceModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    url: str

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

class SQLModelResourceRepository(ResourceRepository):
    def all():
        pass

    def save(self, resource: Resource) -> None:
        resource_model = ResourceModel(url=resource.get_url().value)
        with Session(engine) as session:
            session.add(resource_model)
            session.commit()