from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routes.healthcheck import router

app = FastAPI()
app.include_router(router)


@app.get("/")
def docs():
    return RedirectResponse("/docs")
