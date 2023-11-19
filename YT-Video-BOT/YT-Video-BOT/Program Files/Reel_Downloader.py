import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

download_dir = os.path.join(os.getcwd(), "Video-Clips")

files = os.listdir(download_dir)

# Iterate over the files and remove each one
for file in files:
    file_path = os.path.join(download_dir, file)
    if os.path.isfile(file_path):
        os.remove(file_path)
        
# Initialize Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
options.add_argument(
    "user-data-dir=C:\\Users\\sbtan\\AppData\\Local\\Google\\Chrome Beta\\User Data\\"
)
options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"

service = Service(executable_path="Driver\chromedriver.exe")

options.add_experimental_option(
    "prefs",
    {
        "download.default_directory": download_dir,  # Set the default download directory
        "download.prompt_for_download": False,  # Disable prompting for download
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    },
)

try:
    # Try initializing Chrome WebDriver
    driver = webdriver.Chrome(service=service, options=options)
except Exception as e:
    if "This version of ChromeDriver only supports Chrome version" in str(e):
        # Handle version mismatch error
        print("Version mismatch error. Downloading compatible ChromeDriver...")
        ChromeDriverManager().install()  # Download and install compatible ChromeDriver
        # Retry initializing Chrome WebDriver
        driver = webdriver.Chrome(service=service, options=options)
    else:
        # Handle other exceptions
        print("An error occurred:", e)


# Path to the links file
links_file = "links.txt"
# Output directory for downloaded videos
output_dir = "Video-Clips"

# Read links from the links file
with open(links_file, "r") as file:
    links = file.readlines()

# Initialize a variable to store the expected number of .mp4 files
expected_file_count = 0


# Function to count .mp4 files in a directory
def count_mp4_files(directory):
    return len([f for f in os.listdir(directory) if f.endswith(".mp4")])


# Iterate through the links and download videos
for link in links:
    link = link.strip()  # Remove leading/trailing whitespace
    if not link:
        continue  # Skip empty lines

    try:
        # Open the InstaVideoSave website
        driver.get("https://fastdl.app/")
        time.sleep(3)

        # Find the input field and submit button
        input_field = driver.find_element(By.XPATH, '//*[@name="url"]')
        submit_button = driver.find_element(By.XPATH, '//*[@type="submit"]')

        # Enter the link and click the download button
        input_field.send_keys(link)
        time.sleep(3)
        submit_button.click()

        # Wait for the download to complete (adjust the sleep time as needed)
        time.sleep(10)
        driver.execute_script("window.scrollBy(0,700);")
        time.sleep(3)

        # Locate the download button and click it
        download_button = driver.find_element(
            By.XPATH,
            '//*[contains(@id,"download-btn") ]',
        )
        href_link = download_button.get_attribute("href")
        driver.get(href_link)
        # Wait for the download to complete (adjust the sleep time as needed)
        time.sleep(10)

        # Move the downloaded video to the output directory
        print(f"Downloaded and saved: {link}")

        # Increment the expected file count
        expected_file_count += 1

    except Exception as e:
        print(f"Error while processing link: {link}\n{e}")

# Check if all expected files are downloaded before closing the WebDriver
while True:
    current_file_count = count_mp4_files(output_dir)
    if current_file_count == expected_file_count:
        break
    time.sleep(1)  # Sleep for 1 second and check again

# Close the WebDriver
driver.quit()
print("*****************************************")
print("**********Reels downloaded***************")
print("*****************************************")
