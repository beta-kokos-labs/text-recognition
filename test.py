from PIL import Image
import pytesseract

# Path to the Tesseract executable
# Adjust this path if necessary, especially if you're on Windows.
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'  # Change this if needed

def recognize_text(image_path):
    # Open the image file
    try:
        with Image.open(image_path) as img:
            # Use pytesseract to do OCR on the image
            text = pytesseract.image_to_string(img)
            return text
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Path to the image file
    image_path = 'path_to_your_image.png'  # Replace this with your image file path
    text = recognize_text(image_path)
    print("Recognized Text:")
    print(text)
