from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.routes import router
from app.bootstrap import bootstrap


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("\n" + "=" * 80)
    print("FORCING DOCUMENT REBUILD")
    print("=" * 80)

    await bootstrap()

    yield


app = FastAPI(
    title="OpenDocs AI",
    lifespan=lifespan
)

app.include_router(router)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

templates = Jinja2Templates(
    directory="app/templates"
)


@app.get(
    "/",
    response_class=HTMLResponse
)
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request
        }
    )