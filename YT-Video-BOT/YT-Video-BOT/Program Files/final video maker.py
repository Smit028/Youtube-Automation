import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Set the directory containing the videos
video_dir = "Video-Clips"
final_video_dir = "Final Video"
files = os.listdir(final_video_dir)

# Iterate over the files and remove each one
for file in files:
    file_path = os.path.join(final_video_dir, file)
    if os.path.isfile(file_path):
        os.remove(file_path)
# Get a list of all the video files in the directory
video_files = [f for f in os.listdir(video_dir) if f.endswith(".mp4")]

# Create a list of resized video clips
video_clips = []
for file in video_files:
    clip = VideoFileClip(os.path.join(video_dir, file)).resize(height=1920)
    video_clips.append(clip)

# Sort the clips by duration, from shortest to longest
video_clips = sorted(video_clips, key=lambda x: x.duration)

# Concatenate the clips into one video
final_clip = concatenate_videoclips(video_clips)

# Set the title of the final video
final_clip.title = "Today's Most Viral Insta Reels: Famous TikTokers Take Over"

# Create a directory to save the final video
output_dir = "Final Video"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the final video
final_clip.write_videofile(
    os.path.join(output_dir, "Final Video.mp4"), codec="libx264", fps=30
)

# Set the original filename
original_filename = "Final Video.mp4"

# Set the new filename with the provided title
new_filename = "Today's Most Viral Insta Reels - Famous TikTokers Take Over.mp4"

# Rename the final video
os.rename(
    os.path.join(output_dir, original_filename), os.path.join(output_dir, new_filename)
)

print("*****************************************")
print("**********final video created************")
print("*****************************************")
