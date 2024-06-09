from PIL import Image
import os

# Set the path to the folder containing images
image_folder = './source'

# Create a new PDF file
pdf_file = 'output.pdf'

# Open the PDF file in write mode
with open(pdf_file, 'wb') as f:
    # Loop through each image in the folder
    for image_name in os.listdir(image_folder):
        # Construct the full path to the image
        image_path = os.path.join(image_folder, image_name)
        # Open the image file
        with Image.open(image_path) as img:
            # Save the image to the PDF file
            img.save(f, 'PDF', resolution=100.0)
