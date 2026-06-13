import io

import core
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import StreamingResponse

router = APIRouter(prefix="/MFR", tags=["MFR"])


@router.get("/files/search")
def MFR_search_files(feature_name: str = Query(..., description="MFR feature name to search for.")):
    try:
        return core.search_MFR_files(feature_name)
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@router.get("/labels/description")
def MFR_labels_description():
    try:
        return {"labels_description": core._json_safe(core.get_MFR_labels_description())}
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@router.get("/dataset/table-of-contents")
def MFR_table_of_contents():
    try:
        return core.get_MFR_table_of_contents()
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@router.get("/files/{file_id}/thumbnail")
def MFR_file_thumbnail(file_id: int):
    try:
        png_bytes = core.get_MFR_file_thumbnail(file_id)
        return StreamingResponse(io.BytesIO(png_bytes), media_type="image/png")
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


