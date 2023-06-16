import logging
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; Trident/5.0)"}


def scrape_page_data(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            logging.info('Request successful')
        elif response.status_code == 403:
            logging.warning(f'Request forbidden with status code {response.status_code}')
            return []
        else:
            logging.warning(f'Too many requests with status code {response.status_code}')
            return []

        content = response.content
        soup = BeautifulSoup(content, 'html.parser')

        data = []
        link_elements = soup.find_all('a', class_='card-link')
        links = [f'https://www.hepsiemlak.com{link["href"]}' for link in link_elements]

        for link in links:
            data.append(url_to_info(link))

        logging.info(f"Scraped data from page: {url}")
        return data
    except Exception as e:
        logging.error(f"Error occurred while scraping page: {url}")
        logging.exception(e)
        return []

def url_to_info(url):
    try:
        response = requests.get(url, headers=headers)
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')

        adress_main = soup.find('ul', class_='short-info-list')
        li_elements = adress_main.find_all('li')
        adress_city = li_elements[0].get_text(strip=True)
        adress_district = li_elements[1].get_text(strip=True)
        adress_neighborhood = li_elements[2].get_text(strip=True)
        price_element = soup.find('p', class_='fz24-text price').get_text(strip=True)

        data = {'City': adress_city, 'District': adress_district, 'Neighborhood': adress_neighborhood}

        gross_m2 = soup.find_all('ul', class_='adv-info-list')
        for ul in gross_m2:
            li_elements = ul.find_all('li', {'class': 'spec-item'})
            for li in li_elements:
                try:
                    txt = li.find('span', {'class': 'txt'}).get_text(strip=True)
                    value = li.find_all('span', {'data-v-60d12482': ''})[1].get_text(strip=True)
                    data[txt] = value
                except:
                    continue

        driver = webdriver.Chrome("chromedriver.exe")
        driver.get(url)
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        distance_elements = driver.find_elements(By.CLASS_NAME, "whats-near-card-item")
        for element in distance_elements:
            html_content = element.get_attribute('innerHTML')
            soup = BeautifulSoup(html_content, 'html.parser')

            description_divs = soup.find_all('div', class_='whats-near-card-item__description')
            distance_divs = soup.find_all('div', class_='whats-near-card-item__distance')

            for description_div, distance_div in zip(description_divs, distance_divs):
                name = description_div.span.get_text(strip=True)
                value_for_name = distance_div.span.get_text(strip=True)
                name_parts = name.split(" - ")
                name = name_parts[0]
                data[name] = value_for_name
        data["Rent"] = price_element


        return data
    

    except Exception as e:
        logging.error(f"Error occurred while scraping data from URL: {url}")
        logging.exception(e)

        return {}
    

total_csv = []

for i in range(0, 1400):

    url = f"https://www.hepsiemlak.com/ankara-satilik?page={i}"
    logging.info(f"Scraping page: {i}")
    page_data = scrape_page_data(url)
    total_csv.extend(page_data)
    total_data = pd.DataFrame(total_csv)
    total_data.to_csv("test", index=False)
    time.sleep(60)

    
logging.info("Scraping completed!")
