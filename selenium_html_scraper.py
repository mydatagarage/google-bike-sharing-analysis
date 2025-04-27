import os, time, requests, zipfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Configuration variables
url = "https://divvy-tripdata.s3.amazonaws.com/index.html"  # Source data URL
TARGET_YEAR = 2024  # Only download files from this year
RAW_DIR = "./dataset/raw_data/"      # Directory to store ZIP files
EXTRACT_DIR = "./dataset/extracted_data/"  # Directory for extracted CSVs

# Create necessary directories if they don't exist
os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(EXTRACT_DIR, exist_ok=True)

# Set up headless Firefox browser
options = Options()
options.headless = True  # Run browser in background
driver = webdriver.Firefox(options=options)
driver.get(url)  # Open the data index page
time.sleep(1.5)  # Wait for page to fully load

# Extract all links containing the target year
# This finds <a> elements and filters for those with href containing our year
links = [a.get_attribute('href') for a in driver.find_elements(By.CSS_SELECTOR, "a") 
         if str(TARGET_YEAR) in a.get_attribute('href')]
driver.close()  # Close browser when done

# Download each file if it doesn't already exist locally
for link in links:
    # Example of url: "https://divvy-tripdata.s3.amazonaws.com/202006-divvy-tripdata.zip"
    filename = link.split('/')[-1]  # Extract filename from URL
    filepath = os.path.join(RAW_DIR, filename)
    
    if not os.path.exists(filepath):  # Skip if already downloaded
        print(f"Downloading: {filename}")
        # Get file content and save to disk
        with open(filepath, "wb") as f:
            f.write(requests.get(link).content)
        time.sleep(1)  # Brief pause between downloads to be gentle on server
    else:
        print(f"Already exists: {filename}")

# Extract all ZIP files to the extraction directory
for file in [f for f in os.listdir(RAW_DIR) if f.endswith('.zip')]:
    print(f"Extracting: {file}")
    # Extract all contents directly to extraction directory
    zipfile.ZipFile(os.path.join(RAW_DIR, file)).extractall(EXTRACT_DIR)

print("Download and extraction complete!")
