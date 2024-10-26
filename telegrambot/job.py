from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def search_jobs(location):
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        # Construct the URL for job search
        base_url = "https://www.indeed.co.uk/jobs"
        driver.get(f"{base_url}?q=jobs&l={location}")

        time.sleep(3)  # Wait for the page to load

        job_links = []
        job_cards = driver.find_elements(By.CLASS_NAME, 'jobsearch-SerpJobCard')

        for job_card in job_cards:
            link = job_card.find_element(By.TAG_NAME, 'a')
            job_links.append(link.get_attribute('href'))

        return job_links

    finally:
        driver.quit()

# Example usage
location = 'Plymouth'
job_urls = search_jobs(location)

for url in job_urls:
    print(url)
