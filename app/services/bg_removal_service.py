from rembg import remove
from PIL import Image
import io
import os

async def remove_background(file):
    input_data = await file.read()
    output_data = remove(input_data)
    output_path = f"app/static/removed_{file.filename}"
    with open(output_path, "wb") as f:
        f.write(output_data)
    return output_path