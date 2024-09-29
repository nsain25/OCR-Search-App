import gradio as gr
from PIL import Image
import easyocr
import numpy as np

# Initialize EasyOCR reader (for English and Hindi)
reader = easyocr.Reader(['en', 'hi'])

# OCR function using EasyOCR
def ocr_with_gradio(image):
    if image is None:
        return "Error: No image uploaded."
    
    try:
        # Convert the PIL image to a NumPy array (which EasyOCR expects)
        image_np = np.array(image)
        
        # Perform OCR using EasyOCR
        extracted_text = reader.readtext(image_np, detail=0, paragraph=True)
        return '\n'.join(extracted_text) if extracted_text else "No text found in the image."
    
    except Exception as e:
        return f"Error during OCR: {str(e)}"

# Gradio Interface
interface = gr.Interface(
    fn=ocr_with_gradio, 
    inputs=gr.Image(type="pil"), 
    outputs="text", 
    title="OCR for Hindi and English Text",
    description="Upload an image containing both Hindi and English text, and the OCR will extract the text."
)

# Launch the Gradio interface
interface.launch()
