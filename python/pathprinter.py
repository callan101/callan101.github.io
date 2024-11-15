import os

def generate_img_tags(input_folder):
    # Define supported image extensions (you can add more if needed)
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')

    # Check if the input folder exists
    if not os.path.isdir(input_folder):
        print(f"Error: The folder '{input_folder}' does not exist.")
        return
    
    # Loop through the directory to find image files
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            # Check if the file is an image based on its extension
            if file.lower().endswith(image_extensions):
                # Get the relative path of the image
                relative_path = os.path.relpath(os.path.join(root, file), input_folder)
                # Print the <img> tag with the relative path
                print(f'<img class="img-responsive" src="../imgs/a6000/2024-08-19_ParkButteLookout/{relative_path}" onclick="openFullscreen(this)" />')

# Provide the path to the folder you want to scan
input_folder = 'imgs/a6000/2024-08-19_ParkButteLookout/'  # Change this to your folder's path
generate_img_tags(input_folder)

