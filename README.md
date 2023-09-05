# Image Thumbnail Generator

## Overview

The Image Thumbnail Generator is a Python script that automates the process of resizing images in a source directory and saving the resized images as thumbnails in a target directory. This script is useful for quickly generating smaller versions of images for use in web applications, galleries, or other projects.

## Features

- Automatically resizes images to a specified size.
- Supports various image formats, including PNG, JPEG, GIF, and BMP.
- Handles multiple images in a source directory.
- Provides error handling for cases where image processing fails.

## Getting Started

Follow these steps to get started with the Image Thumbnail Generator:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/bayurzx/image-thumbnail-generator.git
   ```

2. **Install Dependencies:**

   Navigate to the project directory and install the required dependencies (Pillow library):

   ```bash
   pip install Pillow
   ```

3. **Usage:**

   Modify the `create_thumbnails` function in the `generate_thumbnails.py` script to specify your source and target directories, as well as the desired thumbnail size.

   ```python
   source_directory = "path/to/source_directory"
   thumbnail_directory = "path/to/thumbnail_directory"
   create_thumbnails(source_directory, thumbnail_directory, size=(128, 128))
   ```

4. **Run the Script:**

   Execute the script to generate thumbnails:

   ```bash
   python run.py
   ```

## Configuration

You can configure the script by modifying the following variables in `generate_thumbnails.py`:

- `source_directory`: The directory containing the source images to be resized.
- `thumbnail_directory`: The directory where resized thumbnails will be saved.
- `size`: The desired size of the thumbnails in pixels (width, height).

## Supported Image Formats

The script supports the following image formats:

- PNG
- JPEG
- GIF
- BMP

## Error Handling

The script includes error handling to handle cases where image processing fails. If an error occurs while processing an image, the script will print an error message and continue processing other images.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Pillow](https://pillow.readthedocs.io/en/stable/): The Python Imaging Library that provides image processing capabilities.

## Author

Adebayo Omolumo
bayurzx@mgmai.com
