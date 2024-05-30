import requests
from bs4 import BeautifulSoup

def get_proxies():
    response = requests.get('https://www.sslproxies.org/')
    soup = BeautifulSoup(response.content, 'html.parser')
    proxies = []
    for row in soup.find_all('tr')[1:11]:  # Getting top 10 proxies
        tds = row.find_all('td')
        proxies.append(f"{tds[0].text}:{tds[1].text}")
    return proxies
