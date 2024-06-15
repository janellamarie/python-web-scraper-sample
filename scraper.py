import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def ScrapeMercariUS(url):
  options = Options()
  options.add_argument("--headless")

  browser = webdriver.Chrome(options=options)
  print("Navigating to", url)
  browser.get(url)
  page = browser.page_source

  print("Parsing information...")
  soup = BeautifulSoup(page, "lxml")
  print(soup)
  
  name = soup.find('h1', attrs={'data-testid': 'ItemName'}).text
  price = soup.find('p', attrs={'data-testid': 'ItemPrice'}).text.rsplit('$')[1]
  if soup.find('div', attrs={'data-testid': 'ItemDetailsRibbon'}) != None:
    status = soup.find('div', attrs={'data-testid': 'ItemDetailsRibbon'}).text
    if status.find("SOLD") != -1:
      status = 'unavailable'
  else:
    status = 'available'
  img_link = soup.select('img[class*="Image__ThumbnailImage-"]')[0].get('src').split('?')[0]

  print("Quitting browser...")
  browser.quit()

  return {'name': name,'price': price, 'status': status, 'img_link': img_link}

def ScrapeMercariJP(url):
  options = Options()
  options.add_argument("--headless")

  browser = webdriver.Chrome(options=options)
  print("Navigating to", url)
  browser.get(url)
  page = browser.page_source

  time.sleep(5)

  print("Parsing information...")
  content = browser.page_source.encode('utf-8').strip()
  soup = BeautifulSoup(content, "html.parser")

  name = soup.find('title').text.split(' by')[0]
  price = soup.find('span', {'class' : 'price'}).text
  if soup.find('div', attrs={'data-testid': 'thumbnail-sticker'}) != None:
    status = 'unavailable'
  else:
    status = 'available'
  
  img_link = soup.select('img[alt="Thumbnail of "]')[0].get('src').split('?')[0]

  return {'name': name,'price': price, 'status': status, 'img_link': img_link}

if __name__ == "__main__":
  result = ScrapeMercariUS("https://www.mercari.com/us/item/m97348244738/")
  print("name:", result['name'], "price:", result['price'], result['status'], result['img_link'])

  result = ScrapeMercariJP("https://jp.mercari.com/item/m47474648770")
  print("name:", result['name'], "price:", result['price'], result['status'], result['img_link'])
