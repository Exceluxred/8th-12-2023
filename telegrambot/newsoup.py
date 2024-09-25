import requests
from bs4 import BeautifulSoup

def get_all_links(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Send a GET request to the URL with headers
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all 'a' tags (which typically contain links)
        links = soup.find_all('a')
        
        # Extract and print the URLs
        for link in links:
            href = link.get('href')
            if href:
                print(href)
                
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
url = 'https://www.jumia.com.ng/'  # Replace with your desired URL
get_all_links(url)
