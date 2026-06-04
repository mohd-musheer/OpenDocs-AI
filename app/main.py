from pathlib import Path
import asyncio

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.routes import router

# =====================================================
# Auto bootstrap
# =====================================================

PAGEINDEX_DIR = Path("data/pageindex")

needs_bootstrap = (
    not PAGEINDEX_DIR.exists()
    or
    len(list(PAGEINDEX_DIR.glob("*.json"))) == 0
)

if needs_bootstrap:

    print("\n" + "=" * 80)
    print("NO PAGEINDEX FOUND")
    print("RUNNING BOOTSTRAP")
    print("=" * 80)

    from app.bootstrap import bootstrap

    asyncio.run(
        bootstrap()
    )

# =====================================================
# FastAPI App
# =====================================================

app = FastAPI(
    title="OpenDocs AI"
)

app.include_router(router)

app.mount(
    "/static",
    StaticFiles(
        directory="app/static"
    ),
    name="static"
)

templates = Jinja2Templates(
    directory="app/templates"
)

# =====================================================
# Routes
# =====================================================

@app.get(
    "/",
    response_class=HTMLResponse
)
def home(
    request: Request
):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )