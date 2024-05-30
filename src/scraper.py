import requests
from bs4 import BeautifulSoup
import random
import logging
from .proxies import get_proxies
from .data_manager import save_data

# Setup logging
logging.basicConfig(filename='logs/scraper.log', level=logging.INFO)

HEADERS = [
    # List of user agents to simulate real browser requests
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    # Add more user agents here
]

def get_html(url, proxies):
    proxy = random.choice(proxies)
    headers = {'User-Agent': random.choice(HEADERS)}
    response = requests.get(url, headers=headers, proxies={"http": proxy, "https": proxy})
    return response.content

def parse_profile(html):
    soup = BeautifulSoup(html, 'html.parser')
    full_name = soup.find('span', {'class': 'full-name'}).get_text()
    country = soup.find('span', {'class': 'country-name'}).get_text()
    company = soup.find('span', {'class': 'company-name'}).get_text()
    return {
        'full_name': full_name,
        'country': country,
        'company': company
    }

def scrape_profiles(profile_urls):
    proxies = get_proxies()
    for url in profile_urls:
        try:
            html = get_html(url, proxies)
            profile_data = parse_profile(html)
            save_data(profile_data)
            logging.info(f"Successfully scraped: {url}")
        except Exception as e:
            logging.error(f"Failed to scrape: {url} | Error: {str(e)}")

if __name__ == "__main__":
    # Example list of LinkedIn profile URLs
    profile_urls = [
        "https://www.linkedin.com/in/some-profile",
        # Add more URLs
    ]
    scrape_profiles(profile_urls)
