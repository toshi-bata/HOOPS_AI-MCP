from contextlib import asynccontextmanager
import mimetypes
import pathlib

mimetypes.init()
mimetypes.add_type("application/javascript", ".mjs")

import core
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import brep, cad, files, mfr, similarity


@asynccontextmanager
async def lifespan(app: FastAPI):
    import shutil
    for folder in (core.CAD_UPLOAD_DIR, core.CAD_VIEWER_OUTPUT_DIR):
        if folder.exists():
            shutil.rmtree(folder)
        folder.mkdir(parents=True, exist_ok=True)
    core.init_hoops_license()
    yield
    if core.MFR_dataset_explorer is not None and hasattr(core.MFR_dataset_explorer, "close"):
        core.MFR_dataset_explorer.close()
    core.CAD_viewers.clear()


app = FastAPI(
    title="HOOPS AI File Search API",
    lifespan=lifespan,
)

app.include_router(files.router)
app.include_router(mfr.router)
app.include_router(cad.router)
app.include_router(brep.router)
app.include_router(similarity.router)

core.CAD_VIEWER_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
app.mount("/out", StaticFiles(directory=str(core.CAD_VIEWER_OUTPUT_DIR)), name="out")

_static_dir = pathlib.Path(__file__).parent / "static"
_static_dir.mkdir(exist_ok=True)
app.mount("/static", StaticFiles(directory=str(_static_dir)), name="static")

