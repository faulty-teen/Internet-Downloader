import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up headless browser
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the page
url = 'https://samplefocus.com/samples/full-glide-dynamic-piano-haunting-loop'
driver.get(url)

# Find the download button
button = driver.find_element_by_xpath('//button[@class="download-button"]')

# Click the download button
button.click()

# Handle the download (example for an image)
download_url = button.get_attribute('href')
response = requests.get(download_url)

# Save the file
with open('downloaded_file.jpg', 'wb') as file:
    file.write(response.content)

# Clean up
driver.quit()
