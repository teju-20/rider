import cv2
import numpy as np
import os
from tqdm import tqdm  # Progress bar

# Folder paths
input_folder = r"C:\Users\Smart\.vscode\.vscode\AI_Image super resolution\low_quality"  # Update this with your actual folder path
output_folder = r"C:\Users\Smart\.vscode\.vscode\AI_Image super resolution\model 1"  # Folder to save processed images

# Create output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

def process_images(input_folder, output_folder, output_size=(256, 256), max_images=10000):
    """Process and save only a limited number of images with correct color handling."""
    
    # Get all image files
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]
    
    # Limit to first 10,000 images
    image_files = image_files[:max_images]

    for image_file in tqdm(image_files, desc="Processing Images"):
        image_path = os.path.join(input_folder, image_file)
        
        # Read image in BGR format
        image = cv2.imread(image_path)
        if image is None:
            print(f"Skipping {image_file} (could not load)")
            continue

        # Convert BGR to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Resize to 256x256 using bicubic interpolation (better for super-resolution)
        resized_image = cv2.resize(image_rgb, output_size, interpolation=cv2.INTER_CUBIC)

        # Normalize pixel values (0 to 1 for CNN training)
        normalized_image = resized_image / 255.0

        # Convert back to BGR (since OpenCV saves in BGR format)
        processed_image = (normalized_image * 255).astype(np.uint8)  # Convert back to 0-255 range
        processed_image = cv2.cvtColor(processed_image, cv2.COLOR_RGB2BGR)  

        # Save preprocessed image
        save_path = os.path.join(output_folder, image_file)
        cv2.imwrite(save_path, processed_image)
    
    print(f"✅ {len(image_files)} images processed and saved in '{output_folder}'.")

# Run the batch processing for 10,000 images
process_images(input_folder, output_folder, max_images=10000)
