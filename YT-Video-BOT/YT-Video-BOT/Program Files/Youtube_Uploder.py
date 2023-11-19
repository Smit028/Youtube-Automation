import time
import os
import random
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
dir_path = "Final Video"
count = 0
files = os.listdir(dir_path)
files.sort(key=lambda x: os.path.getmtime(os.path.join(dir_path, x)))
for path in files:
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
print("   ", count, " Videos found in the videos folder, ready to upload...")
time.sleep(6)

for i in range(count):
    bot = webdriver.Chrome(service=service, options=options)

    bot.get("https://studio.youtube.com")
    time.sleep(3)
    upload_button = bot.find_element(By.XPATH, '//*[@id="upload-icon"]')
    upload_button.click()
    time.sleep(1)

    file_input = bot.find_element(By.XPATH, '//*[@id="content"]/input')
    simp_path = os.path.join(dir_path, files[i])
    abs_path = os.path.abspath(simp_path)
    file_input.send_keys(abs_path)

    time.sleep(10)

    # Get video title
    title = "Today's Most Viral Insta Reels: Famous TikTokers Take Over"
    show_more = bot.find_element(By.XPATH, '//*[@id="toggle-button"]')
    show_more.click()

    wait = WebDriverWait(bot, 20)

    # file_input = bot.find_element(
    #     By.CSS_SELECTOR,
    #     "input.style-scope.ytcp-thumbnails-compact-editor-uploader-old",
    # )
    # file_input.send_keys("Thumbnail\Thumbnail.jpg")

    # wait for the upload to complete
    time.sleep(10)
    tags_file = os.path.join("Tags\Tags.txt")
    if os.path.isfile(tags_file):
        with open(
            tags_file, "r", encoding="utf-8"
        ) as f:  # specify the encoding explicitly
            tags = f.read().splitlines()
            # Enter tags
            tag_input = WebDriverWait(bot, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="text-input"]'))
            )
            random.shuffle(tags)
            count = 0

            for tag in tags:
                if count < 10:
                    tag_input.send_keys(tag)
                    tag_input.send_keys("\ue007")  # Press Enter
                    time.sleep(1)
                    count += 1

    # Click next button
    next_button = bot.find_element(By.XPATH, '//*[@id="next-button"]')
    for i in range(3):
        next_button.click()
        time.sleep(5)

    # Click done button
    done_button = bot.find_element(By.XPATH, '//*[@id="done-button"]')
    done_button.click()
    time.sleep(5)
    bot.quit()

print("******************************************")
print("**********final video uploaded************")
print("******************************************")
