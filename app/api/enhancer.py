# app/api/enhancer.py
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
from app.services.enhancer_service import enhance_image
from typing import Annotated

router = APIRouter()

@router.post("/image", responses={
    200: {
        "content": {"image/png": {}},
        "description": "Returns enhanced PNG image"
    }
})
async def enhance(
    file: Annotated[UploadFile, File(description="Image file (JPEG/PNG)")]
):
    """Enhances image quality through multi-stage processing pipeline"""
    output_path = await enhance_image(file)
    return FileResponse(
        output_path, 
        media_type="image/png",
        headers={"X-Enhancement-Method": "v2.1"}
    )
