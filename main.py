from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

DRIVER_PATH = "D:\\apps\\chromedriver\\chromedriver.exe"
URL_SOLOTODO = "https://www.solotodo.cl/computer_cases?motherboard_formats=251395"

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200") 

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)


while True:
    driver.get(URL_SOLOTODO)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

    for element in soup.findAll('div',attrs={'class':'d-flex flex-column category-browse-result'}):
        productName = element.findAll('a', href=True)[0].text
        productPrice = element.findAll('div', attrs={'class': 'price flex-grow'})[0].text
        print("Gabinete %s a %s  " % (productName, productPrice) )

    time.sleep(60)

driver.quit()