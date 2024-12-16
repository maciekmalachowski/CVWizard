from bs4 import BeautifulSoup
import requests

def get_data(link):
    # Get response and init the BeautifulSoup
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")

    # Scrappe skills
    skills =  [i.text for i in soup.find_all("h4", attrs={'class': 'css-b849nv'})]

    # Scrape description
    full_desc = soup.find("div", attrs={'class': 'css-tbycqp'})
    sections = full_desc.find_all(['p', 'ul'])
    desc = []
    for element in sections:
        if element.name == 'p':
            if element.get_text(strip=True):
                desc.append(element.get_text(strip=True))
        elif element.name == 'ul':
            for li in element.find_all('li'):
                desc.append(li.get_text(strip=True))

    result = {"skills":skills} | {"description": " ".join(desc)}
    return result
