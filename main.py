from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import requests

def mainProgram():

    DRIVER_PATH = "D:\\apps\\chromedriver\\chromedriver.exe"
    URL_SOLOTODO = "https://www.solotodo.cl/computer_cases?motherboard_formats=251395"
    QUERY = "H200"

    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200") 

    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)


    while True:
        driver.get(URL_SOLOTODO)
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")

        # search for all elements and getting its name and price
        for element in soup.findAll('div',attrs={'class':'d-flex flex-column category-browse-result'}):
            productName = element.findAll('a', href=True)[0].text
            productPrice = element.findAll('div', attrs={'class': 'price flex-grow'})[0].text
            print("Producto %s a %s  " % (productName, productPrice) )

            if QUERY in productName:
                sendTelegramAlert("Producto %s encontrado a un precio de %s " % (productName, productPrice) )
                

        time.sleep(60)
    driver.quit()


def sendTelegramAlert(message):

    TOKEN = 'xxxx'
    CHAT_ID = 'xxxx'
   
    send_text = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + CHAT_ID + '&parse_mode=Markdown&text=' + message

    response = requests.get(send_text)
    return response.json()


mainProgram()


