import os
import random
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the path to the directory containing .mp4 files
video_path = r"Video-Clips"

# Get a list of .mp4 files in the directory
mp4_files = [
    filename for filename in os.listdir(video_path) if filename.endswith(".mp4")
]

# Load tags from .env file as a list
tags = os.getenv("tags")
print(tags)
if tags:
    tags = tags.strip("[]").replace('"', "").split(",")

# Shuffle the list of tags
random.shuffle(tags)

# Ensure that there are enough tags for the .mp4 files
if len(mp4_files) > len(tags):
    raise ValueError("Not enough tags in the .env file.")

# Loop over each .mp4 file and assign a random tag
for mp4_file in mp4_files:
    try:
        # Get a random tag from the list
        random_tag = tags.pop()
        print(random_tag)
        # Rename the .mp4 file with the new filename (using the random tag)
        new_filename = f"{random_tag}.mp4"
        os.rename(
            os.path.join(video_path, mp4_file),
            os.path.join(video_path, new_filename),
        )

        print(f"Renamed {mp4_file} to {new_filename}")
    except Exception as e:
        print(f"An error occurred while renaming {mp4_file}: {str(e)}")

print("*****************************************")
print("**********Reels renamed************")
print("*****************************************")
