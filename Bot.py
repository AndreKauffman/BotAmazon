import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup


class Amazon:
    def __init__(self, name_product):
        self.name_product = 'Iphone'
        self.driver = webdriver.Chrome(executable_path=r'C:\Área de Trabalho\ProjetoAmazon\driver\chromedriver.exe')

    def login(self):
        driver = self.driver
        driver.get('https://www.amazon.com.br/')
        time.sleep(1)
        user_element = driver.find_element_by_xpath("//input[@name='field-keywords']")
        user_element.send_keys(self.name_product)
        time.sleep(0.5)
        user_element.send_keys(Keys.RETURN)
        time.sleep(3)

    def take_data(self):
        driver = self.driver
        nomes = []
        price = []
        data_product1 = driver.find_element_by_xpath("//div[@class='s-desktop-content s-opposite-dir sg-row']")
        html_content1 = data_product1.get_attribute('outerHTML')
        soup1 = BeautifulSoup(html_content1, 'html.parser')

        for c in soup1:
            separar_nome = c.find_all('span', class_='a-size-base-plus a-color-base a-text-normal')
            separar_preço = c.find_all('span', class_='a-price-whole')
            for nome in separar_nome:
                nomes.append(nome.next_element)
            for preço in separar_preço:
                price.append(preço.next_element)

        while True:
            if len(price) > len(nomes) - 1:
                break
            add = '0'
            price.append(add)
        driver.quit()

        colunas = 'NomeProduct'.split()
        dados = pd.DataFrame(data=nomes, index=price, columns=colunas)
        dados.to_excel('Projeto.xlsx')
        print(dados)


bot = Amazon('iphone')
bot.login()
bot.take_data()
