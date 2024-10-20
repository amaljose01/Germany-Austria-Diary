import os
from PIL import Image
import pyheif

def convert_heic_to_jpg(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.heic', '.heif')):
            heic_file_path = os.path.join(directory, filename)
            jpg_file_path = os.path.join(directory, filename.rsplit('.', 1)[0] + '.jpg')

            # Read HEIC file
            heif_file = pyheif.read(heic_file_path)

            # Convert to Image object
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
                heif_file.mode,
                heif_file.stride
            )

            # Save as JPG
            image.save(jpg_file_path, "JPEG")
            print(f"Converted: {filename} to {jpg_file_path}")

# Use the current working directory
current_directory = os.getcwd()
convert_heic_to_jpg(current_directory)

