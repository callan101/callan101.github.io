from PIL import Image
import os

# Function to resize images in a folder
def resize_images(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):  # Check for image files
            image_path = os.path.join(folder_path, filename)
            try:
                # Open the image file
                with Image.open(image_path) as img:
                    # Check if it's a square image
                    if img.size[0] == img.size[1]:
                        # Resize the image to half the resolution
                        resized_img = img.resize((img.size[0] // 2, img.size[1] // 2))
                        # Save the resized image, overwriting the original file
                        print(img.size[0])
                        resized_img.save(image_path)
                        print(f"Resized {filename} successfully.")
                        print(img.size[0])
                    else:
                        print(f"File {filename} is not a square.")
            except Exception as e:
                print(f"Error resizing {filename}: {e}")

# Example usage
if __name__ == "__main__":
    folder_path = "output"
    resize_images(folder_path)
