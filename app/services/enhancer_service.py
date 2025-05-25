# app/services/enhancer_service.py
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import io

async def enhance_image(file):
    # Load image and ensure RGB mode
    image = Image.open(io.BytesIO(await file.read())).convert('RGB')
    
    # 1. Light noise reduction
    image = image.filter(ImageFilter.MedianFilter(size=3))
    
    # 2. GENTLE sharpening using unsharp mask
    image = image.filter(ImageFilter.UnsharpMask(
        radius=1.5,   # Reduced from 2.5
        percent=120,  # Reduced from 180
        threshold=3
    ))
    
    # 3. Mild contrast enhancement
    image = ImageOps.autocontrast(image, cutoff=2.0)  # Increased cutoff
    
    # 4. SUBTLE color enhancement
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(1.15)  # Much gentler than HSV manipulation
    
    # 5. REMOVE EDGE_ENHANCE_MORE - it's causing posterization
    # image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)  # ← COMMENTED OUT
    
    # 6. Gentle brightness adjustment
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1.05)  # Reduced from 1.08
    
    output_path = f"app/static/enhanced_{file.filename}"
    image.save(output_path, 'PNG', optimize=True, quality=95)  # Higher quality
    return output_path
