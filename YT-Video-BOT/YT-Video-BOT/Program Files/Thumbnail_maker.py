import os
import random
from PIL import Image

# Set path to directory containing images
image_dir = r"D:\\Edit Pack\\youtube-autoupload-bot-master\\youtube-autoupload-bot-master\\YT-Video-BOT\\Video Clips"

# Get a list of all image files in the directory
image_files = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]

# Randomly select 3 images from the list
selected_files = random.sample(image_files, 3)

# Resize each image to have width 640 and calculate height based on aspect ratio
images = []
for image_file in selected_files:
    image_path = os.path.join(image_dir, image_file)
    image = Image.open(image_path)
    width, height = image.size
    new_height = int((640 / width) * height)
    resized_image = image.resize((640, new_height))

    # Crop image from the center to have a height of 1080
    left = 0
    top = (new_height - 1080) / 2
    right = 640
    bottom = (new_height + 1080) / 2
    cropped_image = resized_image.crop((left, top, right, bottom))

    images.append(cropped_image)

# Concatenate images side-by-side
total_width = sum([im.size[0] for im in images])
max_height = max([im.size[1] for im in images])
new_im = Image.new("RGB", (total_width, max_height))

# Add resized images to collage
x_offset = 0
for im in images:
    new_im.paste(im, (x_offset, 0))
    x_offset += im.size[0]

# Specify the path to the logo image
logo_path = r"D:\Edit Pack\youtube-autoupload-bot-master\youtube-autoupload-bot-master\YT-Video-BOT\Logo\insta_logo.png"

# Check if the logo file exists before attempting to open it
if os.path.isfile(logo_path):
    # Open and process the logo image
    logo = Image.open(logo_path).convert("RGBA")  # Convert to RGBA with transparency
    logo_width = 200
    logo_height = int(logo.size[1] * (logo_width / logo.size[0]))
    logo = logo.resize((logo_width, logo_height))
    new_im.paste(logo, (20, 20), logo)

# Resize final image to have height 1080 and width 1920
new_width = 1920
new_height = 1080
scale = min(new_width / new_im.width, new_height / new_im.height)
new_size = (int(new_im.width * scale), int(new_im.height * scale))
new_im = new_im.resize(new_size)

# Save final image
save_path = r"Thumbnail\Thumbnail.jpg"
new_im.save(save_path)
