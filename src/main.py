from fastapi import FastAPI
from src.shared.infrastructure.api import router as shared_router
from src.resources.infrastructure.api import router as resources_router

app = FastAPI()
app.include_router(shared_router)
app.include_router(resources_router)

@app.get("/")
def read_root():
    return {"Hello":"World"}
