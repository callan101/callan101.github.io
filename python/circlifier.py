from PIL import Image, ImageDraw
import os

# Specify input and output directories
input_directory = "output/"
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
    print("Width : " + str(width))
    print("Height : " + str(height))
    result.paste(img, mask=mask)
    result.save(output_path, "PNG")

# Batch convert JPG/PNG to PNG and crop into circles
for filename in os.listdir(input_directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Include PNG files
        img_path = os.path.join(input_directory, filename)
        output_filename = os.path.splitext(filename)[0] + ".png"
        output_path = os.path.join(output_directory, output_filename)
        convert_and_crop_to_circle(img_path, output_path)
        print(f"Converted and cropped: {filename}")


print("Conversion and cropping completed.")
