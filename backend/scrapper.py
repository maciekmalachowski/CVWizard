from bs4 import BeautifulSoup
import requests
import re

def get_data(link):
    try:
        # Get response and init BeautifulSoup
        response = requests.get(link)
        response.raise_for_status()  # Ensure we handle HTTP errors
        soup = BeautifulSoup(response.text, "html.parser")

        # Scrape title (handle missing elements)
        title_div = soup.find('div', class_='css-s52zl1')
        title = title_div.find('h1').get_text(strip=True) if title_div else "No title found"

        # Scrape skills (use select() for flexibility)
        skills = [skill.get_text(strip=True) for skill in soup.select("h4.css-b849nv")]

        # Scrape description (handle missing elements)
        desc_section = soup.find("div", class_='css-tbycqp')
        description = []
        if desc_section:
            for element in desc_section.find_all(['p', 'ul']):
                if element.name == 'p' and element.get_text(strip=True):
                    description.append(element.get_text(strip=True))
                elif element.name == 'ul':
                    for li in element.find_all('li'):
                        description.append(li.get_text(strip=True))

        # Clean up text
        def normalize_space(text):
            return re.sub(r'\s+', ' ', text).strip()  # Replace multiple spaces with single space

        cleaned_description = " ".join(normalize_space(desc) for desc in description)

        return {"title": title, "skills": skills, "description": cleaned_description}
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}
