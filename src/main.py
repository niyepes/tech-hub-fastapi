from fastapi import FastAPI
from shared.infrastructure.api import router as shared_router
app = FastAPI()
app.include_router(shared_router)

@app.get("/")
def read_root():
    return {"Hello":"World"}
