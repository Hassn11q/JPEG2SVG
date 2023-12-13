# JPEG2SVG

This Python script enables the conversion of images from JPEG format to SVG format.

## Requirements

Before running the code, ensure you have the following Python packages installed:

- **cv2**: OpenCV library for image processing.
- pip install opencv-python



- **glob**: File path expansion matching library.
- pip install glob2


- **svgwrite**: Library to create SVG files.
- pip install svgwrite


- **base64**: Library for encoding and decoding base64 files.
- pip install pybase64


## Usage

1. Clone or download the repository.

2. Install the required packages using the commands mentioned above.

3. Run the `jpeg_to_svg.py` script, providing the necessary parameters or editing the script to suit your requirements.

Example usage:
```bash
python jpeg_to_svg.py --input <input_directory_path> --output <output_directory_path>

Replace <input_directory_path> with the directory containing your JPEG images and <output_directory_path> with the directory where you want to save the converted SVG files.

Check the specified output directory for the generated SVG files.
How it works
The script uses OpenCV (cv2) to read JPEG images, processes them, and then converts them into SVG format using svgwrite. It iterates through the specified input directory, converts each JPEG image to SVG, and saves the resulting SVG files to the specified output directory.

License
This project is licensed under the MIT License.


Feel free to adjust any additional information or instructions based on the specifics of your code or any preferences you might have. This enhanced README file provides clearer instructions on how to install the necessary dependencies and how to use your JPEG to SVG conversion script.

