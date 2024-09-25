import requests
from bs4 import BeautifulSoup
import random
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

def get_all_links(url):
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
        # Add more user agents here
    ]

    proxies = [
        'http://13.80.134.180:8080',
        'http://102.214.104.56:8080',
        'http://131.196.212.172:8080',
        # Add more proxies here
    ]
    
    headers = {
        'User-Agent': random.choice(user_agents)
    }

    # Method 1: Simple requests with user-agent rotation
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')
        
        print("Method 1: Simple requests with user-agent rotation")
        for link in links:
            href = link.get('href')
            if href:
                print(href)
        return
    except requests.exceptions.RequestException as e:
        print(f"Method 1 failed: {e}")
    
    # Method 2: Requests with user-agent rotation and proxies
    for proxy in proxies:
        try:
            response = requests.get(url, headers=headers, proxies={'http': proxy, 'https': proxy})
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a')
            
            print("Method 2: Requests with user-agent rotation and proxies")
            for link in links:
                href = link.get('href')
                if href:
                    print(href)
            return
        except requests.exceptions.RequestException as e:
            print(f"Method 2 failed with proxy {proxy}: {e}")
    
    # Method 3: Selenium with undetected-chromedriver for headless browsing
    try:
        options = uc.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        driver = uc.Chrome(options=options)
        
        driver.get(url)
        elements = driver.find_elements(By.TAG_NAME, 'a')
        
        print("Method 3: Selenium with undetected-chromedriver for headless browsing")
        for elem in elements:
            href = elem.get_attribute('href')
            if href:
                print(href)
                
        driver.quit()
    except Exception as e:
        print(f"Method 3 failed: {e}")

# Example usage
url = 'https://www.jumia.com.ng/'  # Replace with your desired URL
get_all_links(url)
