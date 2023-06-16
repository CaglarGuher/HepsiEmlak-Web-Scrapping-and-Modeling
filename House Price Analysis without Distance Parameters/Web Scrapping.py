import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import logging



logging.basicConfig(filename='scraping.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


def get_property_info(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f'Request successful for URL: {url}')
        elif response.status_code == 403:
            logging.warning(f'Request forbidden for URL: {url}')
            return None
        else:
            logging.warning(f'Too many requests for URL: {url}')
            return None

        time.sleep(25)  

        soup = BeautifulSoup(response.content, 'lxml')
        address_elements = soup.find('ul', class_='short-info-list').find_all('li')
        address_city = address_elements[0].get_text(strip=True)
        address_district = address_elements[1].get_text(strip=True)
        address_neighborhood = address_elements[2].get_text(strip=True)
        price = soup.find('p', class_='fz24-text price').get_text(strip=True)

        property_info = {'City': address_city, 'District': address_district, 'Neighborhood': address_neighborhood, 'Rent': price}
        gross_m2 = soup.find_all('ul', class_='adv-info-list')
        
        for ul in gross_m2:
            li_elements = ul.find_all('li', {'class': 'spec-item'})
            for li in li_elements:
                try:
                    txt = li.find('span', {'class': 'txt'}).get_text(strip=True)
                    value = li.find_all('span', {'data-v-60d12482': ''})[1].get_text(strip=True)
                    property_info[txt] = value
                except:
                    continue

        return property_info

    except Exception as e:
        logging.error(f'An error occurred while processing URL: {url}. Error message: {str(e)}')
        return None


total_data = []

for i in range(0, 1400):
    url = f"https://www.hepsiemlak.com/ankara-satilik?page={i}"
    logging.info(f"Scraping page {i+1} - URL: {url}")
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'lxml')
    link_elements = soup.find_all("div", class_="links")

    for value in link_elements:
        links = [f'https://www.hepsiemlak.com{link_element["href"]}' for link_element in value('a', class_='card-link')]
        for link in links:
            data = get_property_info(link)
            if data:
                total_data.append(data)

    logging.info(f"Scraped page {i+1}")

total_data = pd.DataFrame(total_data)
total_data.to_csv("house_prices_without_distances.csv", index=False)
logging.info("Data saved to 'house_prices.csv'")

