from PIL import Image
import os

def resize_image(image_path, max_width=10240):
    # Open the image
    with Image.open(image_path) as img:
        # Check if the image width is greater than max_width
        if img.width > max_width:
            # Calculate the new height while preserving the aspect ratio
            new_height = int((max_width / img.width) * img.height)
            # Resize the image
            img = img.resize((max_width, new_height), Image.ANTIALIAS)
            # Save the resized image
            img.save(image_path)
            print(f"[INFO] Image '{image_path}' resized to {max_width}px wide.")
        else:
            print(f"[INFO] Image '{image_path}' is already smaller than {max_width}px wide.")

def process_images_in_directory(directory):
    # Loop through all files in the specified directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Only process image files (you can expand this list if needed)
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            print(f"[INFO] Processing image: {file_path}")
            resize_image(file_path)

if __name__ == "__main__":
    # Provide the directory containing images to process
    directory = "imgs/tmp/"  # Change this to your directory path
    print(f"[INFO] Starting to process images in directory: {directory}")
    process_images_in_directory(directory)
    print("[INFO] Image processing completed.")
