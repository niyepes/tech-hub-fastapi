from fastapi import APIRouter, FastAPI, Request
from pydantic import BaseModel
from resources.application.create_resource import CreateResource, CreateResourceCommand
from resources.domain.models import Resource
from resources.infrastructure.repositories import SQLModelResourceRepository

router = APIRouter()

class Payload(BaseModel):
    url: str   

class Response(BaseModel):
    url: str

    @classmethod
    def  from_domain (cls, resource: Resource) -> "Response":
        return cls(url = resource.get_url().value)

@router.post("/resources/")
def create_resource(payload: Payload)-> Response:
    resource = CreateResource(SQLModelResourceRepository()).execute(
        CreateResourceCommand(resource_url=payload.url)
    )
    return Response.from_domain(resource)
