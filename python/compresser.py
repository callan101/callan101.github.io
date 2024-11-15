import os
from PIL import Image

def compress_image(image_path, output_path, quality=85):
    """Compress an image by converting it to RGB, removing metadata, and saving in JPEG or WebP format."""
    try:
        with Image.open(image_path) as img:
            # Convert image to RGB (required for saving as JPEG or WebP)
            img = img.convert("RGB")

            # Check if we should save in WebP format for better compression
            if image_path.lower().endswith(('png', 'bmp', 'gif')):  # Only use WebP for non-JPEG images
                img.save(output_path, "WEBP", quality=quality, method=6)
            else:
                # Save as JPEG with the given quality and optimization
                img.save(output_path, "JPEG", quality=quality, optimize=True)

            print(f"Compressed image saved to: {output_path}")

    except Exception as e:
        print(f"Error compressing image {image_path}: {e}")

def process_folder(root_folder, quality=60):
    """Process all the images in the folder and subfolders."""
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            
            # Check if the file is an image (expandable for more formats)
            if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                print(f"Processing image: {file_path}")

                # Define the output file path (overwrite original or save as a new file)
                output_path = file_path

                # Compress and save the image
                compress_image(file_path, output_path, quality=quality)

if __name__ == "__main__":
    # The parent folder containing all the subfolders and images
    root_folder = "imgs/tmp/"

    # Compress images in the folder with a quality threshold
    process_folder(root_folder, quality=30)
