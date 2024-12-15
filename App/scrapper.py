from bs4 import BeautifulSoup
import requests
from deep_translator import ChatGptTranslator


def get_data(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    # scrappe skills
    skills =  [i.text for i in soup.find_all("h4", attrs={'class': 'css-b849nv'})]

    # scrape description
    full_desc = soup.find("div", attrs={'class': 'css-tbycqp'})
    sections = full_desc.find_all(['p', 'ul'])
    desc = {}
    current_key = None
    for element in sections:
        if element.name == 'p':
            if element.get_text(strip=True):
                current_key = element.get_text(strip=True)
                desc[current_key] = []
        elif element.name == 'ul' and current_key:
            desc[current_key].extend([li.get_text(strip=True) for li in element.find_all('li')])

    result = {"skills":skills} | desc
    print(result)
    # return result

get_data("https://justjoin.it/job-offer/nomachine-poland-c-c-porting-engineer-wroclaw-c")