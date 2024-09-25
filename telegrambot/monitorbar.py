from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
import re

# Set up Edge options
edge_options = Options()
edge_options.add_experimental_option("detach", True)

# Initialize the Edge driver
# Make sure this path points to the actual location of msedgedriver.exe
service = Service('C:/WebDriver/msedgedriver.exe')
driver = webdriver.Edge(service=service, options=edge_options)

# Function to extract search query from URL
def extract_search_query(url):
    search_match = re.search(r'[\?&]q=([^&]*)', url)
    if search_match:
        return search_match.group(1)
    return None

# Function to monitor browser activity
def monitor_browser():
    while True:
        current_url = driver.current_url
        print(f"Visited URL: {current_url}")
        
        # Check for Google search queries
        if "google.com/search" in current_url:
            query = extract_search_query(current_url)
            if query:
                print(f"Search query: {query}")

        # Wait for a short period before checking again
        time.sleep(2)

# Open a new tab and start monitoring
driver.get("https://www.google.com")

# Wait for the user to navigate and interact
try:
    monitor_browser()
except KeyboardInterrupt:
    print("Monitoring stopped by user")
finally:
    driver.quit()
