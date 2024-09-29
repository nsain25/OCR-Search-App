# OCR-Search-App

1. Objective and Initial Setup
The goal was to develop a web application that allows users to upload an image containing both Hindi and English text. The application would extract the text using OCR (Optical Character Recognition) and implement a basic keyword search functionality. The work was conducted using Gradio for the user interface, hosted on Hugging Face Spaces, and initially aimed to use Tesseract as the OCR engine.

2. Implementation Steps
Step 1: Initial Setup (Tesseract-based OCR)
Python Environment Setup:
We began by setting up the environment, including installing necessary libraries like gradio, pytesseract, Pillow, and installing Tesseract via a custom setup.sh script.
The code included setting the Tesseract path in app.py and using Pytesseract to perform the OCR.
Step 2: Creating the Gradio Interface
We created a Gradio interface to allow users to upload an image and display the extracted text.
Gradio was initially configured using gr.inputs.Image, but since this method became deprecated, we updated it to use gr.Image().
Step 3: Deployment on Hugging Face Spaces
After setting up the Gradio interface and implementing the OCR, the web app was deployed on Hugging Face Spaces.
The deployment involved uploading the required files (app.py, setup.sh, and requirements.txt) to Hugging Face.
Step 4: Encountering Issues with Tesseract
Challenge: Tesseract was not installed correctly, or the system could not locate the binary despite multiple attempts using setup.sh to install it. The app produced the error: "/usr/bin/tesseract is not installed or it's not in your PATH."
We tried various installation paths, including /usr/local/bin/tesseract, but the issue persisted.
While the logs indicated that Tesseract was installed, it was still not being recognized by the application.
Step 5: Transition to EasyOCR
Due to persistent challenges with Tesseract, we switched to EasyOCR, a Python-based OCR solution that does not require system-level installations.
Implementation: We integrated EasyOCR into the existing code and adjusted the input to handle PIL Images by converting them to NumPy arrays, which is the format EasyOCR expects.
Libraries: We modified the requirements.txt to include easyocr, torch, gradio, and Pillow.
Step 6: Final Deployment with EasyOCR
The application was redeployed with EasyOCR and successfully handled OCR tasks.
We addressed the issue of input types by ensuring PIL images uploaded through Gradio were converted to NumPy arrays for EasyOCR processing.
The final Gradio interface allowed users to upload an image and see the extracted text.

3. Observations
Tesseract Installation Issues: Despite several installation attempts using a custom setup.sh and checking the system's path, Tesseract was not successfully recognized. This issue could be related to limitations in Hugging Face Spaces when handling system-level installations.
EasyOCR Success: Switching to EasyOCR resolved the issues encountered with Tesseract. EasyOCR successfully extracted text from images containing both Hindi and English text.
Gradio Interface: Gradio provided an easy-to-use interface for image uploads and text extraction, though it required adjustments due to deprecations in the library (gr.inputs replaced with gr.Image()).

4. Challenges Faced
Tesseract Installation: The major challenge was getting Tesseract installed and correctly recognized on Hugging Face Spaces. Even after adjusting paths and trying multiple installation methods, Tesseract remained unavailable.
Library Updates: During the implementation, gr.inputs was deprecated in Gradio, which led to some unexpected errors that were resolved by switching to gr.Image().
Input Type Compatibility: EasyOCR required the image to be in a NumPy array format, but the input provided by Gradio was in PIL Image format. This required a conversion step, which was successfully handled by converting the image before passing it to EasyOCR.

5. Future Work and Enhancements
Search Functionality: Currently, the application performs OCR and displays the extracted text. Future enhancements could include:
Implementing a keyword search within the extracted text.
Highlighting matching keywords in the results for better user experience.
Improved OCR for Multilingual Text:
Model Improvement: Integrating advanced OCR models like those available on Hugging Face (e.g., Vision-Language Models) for better recognition of mixed-language texts, especially for cases involving multiple scripts.
Deployment Improvements:
Switching to Streamlit or other platforms: Hugging Face Spaces had some limitations in terms of installing system-level dependencies. Using a platform that allows for full access to system-level installations or Docker-based deployment could provide more flexibility.
Adding Support for More File Formats:
PDF Support: Extend the application to accept PDFs, perform multi-page OCR, and allow searches across entire documents.
Real-Time OCR:
Allow real-time OCR on video frames or scanned documents as they are uploaded, which would be beneficial for tasks like digitizing books or documents in both English and Hindi.
