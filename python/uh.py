from PIL import Image
import os
import warnings

warnings.filterwarnings("ignore", category=Image.DecompressionBombWarning)


# Set the folder path (change this to your folder path)
folder_path = 'imgs/tmp'


# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a .jpg file
    if filename.lower().endswith('.jpg'):
        # Get the full file path
        file_path = os.path.join(folder_path, filename)
        
        try:
            # Open the image using Pillow
            with Image.open(file_path) as img:
                # Get the dimensions of the image
                width, height = img.size
                # Print the filename and its dimensions
                print(f'{width}x{height} : {filename}')
        except Exception as e:
            print(f"Error opening {filename}: {e}")
