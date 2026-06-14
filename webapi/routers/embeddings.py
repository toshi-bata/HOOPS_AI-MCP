import core
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/Embeddings", tags=["Embeddings"])


@router.post("/compute")
def compute_embeddings():
    """Load the embeddings model and compute shape embeddings for all CAD files
    in the configured directory (notebooks/../packages/cadfiles/fabwave).

    Returns embedding vectors (ids + values matrix), model name, and counts.
    """
    try:
        core.get_embeddings_model()
        return core.embeddings_result
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Embedding computation failed: {exc}") from exc
