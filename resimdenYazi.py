from PIL import Image
import pytesseract


image_path = "C:/Users/tunahan/Pictures/Screenshots/Ekran görüntüsü 2025-12-29 075959.png"  # Görüntü dosyanızın yolu
image = Image.open(image_path)

extracted_text = pytesseract.image_to_string(image)


print(extracted_text)
