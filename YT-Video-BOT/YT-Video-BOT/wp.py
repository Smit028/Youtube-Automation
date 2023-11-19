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
    driver.get("https://web.whatsapp.com/")
    time.sleep(10)

# Wait for the user to scan the QR code manually
    name="Kirtan"
    input("Scan the QR code and press Enter after you are logged in...")
    input_field = driver.find_element(By.XPATH, '_2vDPL')
    input_field.send_keys(name)


try:
    while True:
        pass
except KeyboardInterrupt:
    print("You exited the session. Closing the browser...")

# Close the browser window when the user exits the session
driver.quit()
