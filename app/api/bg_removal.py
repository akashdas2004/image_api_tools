from fastapi import APIRouter, File, UploadFile
from app.services.bg_removal_service import remove_background
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.post("/remove")
async def remove_bg(file: UploadFile = File(...)):
    output_path = await remove_background(file)
    return FileResponse(output_path, media_type="image/png")