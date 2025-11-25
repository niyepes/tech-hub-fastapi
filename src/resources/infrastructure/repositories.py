from sqlmodel import SQLModel, Field, create_engine, Session, select

from src.resources.domain.models import Resource
from src.resources.domain.repositories import ResourceRepository
from src.resources.domain.value_objects import ResourceUrl

class ResourceModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    url: str

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

class SQLModelResourceRepository(ResourceRepository):
    def all(self) -> list[Resource]:
        with Session(engine) as session:
            resource_models = session.exec(select(ResourceModel)).all()
            return [Resource(ResourceUrl(value=resource_model.url)) for resource_model in resource_models]

    def save(self, resource: Resource) -> None:
        resource_model = ResourceModel(url=resource.get_url().value)
        with Session(engine) as session:
            session.add(resource_model)
            session.commit()