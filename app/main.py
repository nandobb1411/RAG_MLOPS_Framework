"""Main module."""

from fastapi import FastAPI
import uvicorn
from api.routers import router

app = FastAPI(title=r'Bertoncellos Chocolate Factory', version="1.0.0")

@app.get("/")
def read_root():
    """Hello World"""
    return {"Hello": "World"}


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)