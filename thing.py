from PIL import Image, ImageDraw
import os
"""
# Specify input and output directories
input_directory = "imgs/360planets"
output_directory = "output/"

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Function to convert and crop images into circles
def convert_and_crop_to_circle(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    mask = Image.new("L", (width, height), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((0, 0, width, height), fill=255)
    result = Image.new("RGBA", (width, height))
    result.paste(img, mask=mask)
    result.save(output_path, "PNG")

# Batch convert JPG to PNG and crop into circles
for filename in os.listdir(input_directory):
    if filename.endswith(".jpg"):
        jpg_path = os.path.join(input_directory, filename)
        png_filename = os.path.splitext(filename)[0] + ".png"
        png_path = os.path.join(output_directory, png_filename)
        convert_and_crop_to_circle(jpg_path, png_path)
        print(f"Converted and cropped: {filename}")

print("Conversion and cropping completed.")
"""

# Function to resize images in a folder
def resize_images(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
            image_path = os.path.join(folder_path, filename)
            try:
                # Open the image file
                with Image.open(image_path) as img:
                    # Resize the image if its dimensions are 4096x4096
                    if img.size == (4096, 4096):
                        resized_img = img.resize((2048, 2048))
                        # Save the resized image, overwriting the original file
                        resized_img.save(image_path)
                        print(f"Resized {filename} successfully.")
            except Exception as e:
                print(f"Error resizing {filename}: {e}")

# Example usage
if __name__ == "__main__":
    folder_path = "output/"
    resize_images(folder_path)