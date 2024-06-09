import pytesseract
from PIL import Image
import os

# Set the path to the folder containing images
image_folder = './source'

# Set the path to the output text file
output_file = 'output.txt'

# Open the output file in append mode
with open(output_file, 'a') as file:
    # Loop through each image in the folder
    for image_name in os.listdir(image_folder):
        # Construct the full path to the image
        image_path = os.path.join(image_folder, image_name)
        # Open the image file
        with Image.open(image_path) as img:
            # Perform OCR on the image
            text = pytesseract.image_to_string(img)
            # Write the extracted text to the output file
            file.write(f'{image_name}: {text}\n')
