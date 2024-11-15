import warnings
from PIL import Image, ImageFile
import os

# Suppress DecompressionBombWarning
warnings.filterwarnings("ignore", category=Image.DecompressionBombWarning)

# This handles truncated images gracefully
ImageFile.LOAD_TRUNCATED_IMAGES = True

MAX_IMAGE_SIZE = 900000000  # Set your desired maximum image size

# Function to resize square images in a folder to 512x512 resolution
def resize_images(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):  # Check for image files
            print(f"Processing {filename}")
            image_path = os.path.join(folder_path, filename)
            
            # Check if the file is too large
            if os.path.getsize(image_path) > MAX_IMAGE_SIZE:
                print(f"Skipping {filename} due to excessive size.")
                continue

            try:
                # Open the image file
                with Image.open(image_path) as img:
                    # Check if it's a square image
                    if img.size[0] == img.size[1]:
                        # Resize the image to 512x512 resolution
                        resized_img = img.resize((512, 512))
                        # Save the resized image, overwriting the original file
                        resized_img.save(image_path)
                        print(f"Resized {filename} to 512x512 successfully.")
                    else:
                        print(f"File {filename} is not a square image.")
            except IOError as e:
                print(f"Error opening {filename}: {e}")
            except Exception as e:
                print(f"Error resizing {filename}: {e}")

# Example usage
if __name__ == "__main__":
    folder_path = "output/"  # Change this to the path of your input folder containing square images
    resize_images(folder_path)
