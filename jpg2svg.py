import cv2
import glob
import os
import svgwrite
import base64

# Paths to the image folder
image_folder = # Replace with the actual path
base_folder =  # Replace with the actual path

# Create output folder
output_folder = os.path.join(base_folder, 'Images')
os.makedirs(output_folder, exist_ok=True)

# Iterate through each image
for image_file in glob.glob(os.path.join(image_folder, "*.jpg")):
    base_name = os.path.basename(image_file)

    # Read the image
    image = cv2.imread(image_file)

    # Create SVG file for each image
    output_svg = os.path.join(output_folder, f"{base_name.replace('.jpg', '.svg')}")
    dwg = svgwrite.Drawing(output_svg, profile='tiny', size=(image.shape[1], image.shape[0]))

    # Encode the image data in base64
    _, image_data = cv2.imencode('.jpg', image)
    image_data_base64 = base64.b64encode(image_data).decode('utf-8')

    # Embed the image data in the SVG file
    image_data_uri = f"data:image/jpeg;base64,{image_data_base64}"
    dwg.add(dwg.image(href=image_data_uri, insert=(0, 0), size=(image.shape[1], image.shape[0])))

    # Save the SVG file
    dwg.save()
