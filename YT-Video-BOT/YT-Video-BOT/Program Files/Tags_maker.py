import os
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
options.add_argument(
    "user-data-dir=C:\\Users\\sbtan\\AppData\\Local\\Google\\Chrome Beta\\User Data\\"
)
options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"
service = Service(executable_path="Driver\chromedriver.exe")
folder_path = "Tags"
files = os.listdir(folder_path)

# Iterate over the files and remove each one
for file in files:
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        os.remove(file_path)

output_file_path = os.path.join(folder_path, "tags.txt")
if os.path.exists(output_file_path):
    os.remove(output_file_path)
# Create 'Tags' folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Create or open the output file 'tags.txt' in append mode
output_file_path = os.path.join(folder_path, "tags.txt")
output_file = open(output_file_path, "a", encoding="utf-8")


# Remove any emoji from the filename
def remove_emoji(text):
    non_text_pattern = re.compile(r"[^\w\s\.]+")
    return non_text_pattern.sub("", text)


def find_and_write_tags(video_title):
    # set the path of the webdriver
    driver = webdriver.Chrome(service=service, options=options)

    # open the url
    driver.get("https://rapidtags.io/generator")

    # find the input box and enter the video title
    input_box = driver.find_element(By.XPATH, '//*[@id="searchInput"]')
    input_box.send_keys(video_title)

    # find the search button and click it
    search_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    search_button.click()

    # wait for the search results to load
    time.sleep(5)

    # find the tagbox and get the text of each span tag
    tagbox = driver.find_element(By.XPATH, '//div[@class="tagbox"]')
    tags = [remove_emoji(tag.text) for tag in tagbox.find_elements(By.TAG_NAME, "span")]

    # close the browser
    driver.quit()

    # Append tags to 'tags.txt' file
    for tag in tags:
        output_file.write(tag + "\n")


# Get a list of all files in the 'videos' folder
video_files = os.listdir("Video-Clips")

# Loop through each video file and call the 'find_and_write_tags()' function
for video_file in video_files:
    if video_file.endswith(".mp4"):
        # Extract the video title from the file name
        video_title = os.path.splitext(video_file)[0].title()
        find_and_write_tags(remove_emoji(video_title))

# Close the output file
output_file.close()

print("*****************************************")
print("************Tags Created*****************")
print("*****************************************")
