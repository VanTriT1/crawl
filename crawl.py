# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException   
import warnings
warnings.filterwarnings("ignore")

header = ['Country', '2017', '2018', 'Rejon']
df = pd.DataFrame(columns=header)
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome('chromedriver.exe')
url = 'http://statisticstimes.com/demographics/countries-by-population.php'
def crawlFromStatisticstimes(url):
    driver.get(url)
    years = []
    index = 0
    try:
        tables = driver.find_element_by_id('table_id')
        try:
            tbody = tables.find_element_by_tag_name('tbody')
            trs = tbody.find_elements_by_tag_name('tr')
            while trs:
                tr = trs.pop()
                try:
                    tds = tr.find_elements_by_tag_name('td')
                    print(tds[1].text + ", " + tds[2].text + ", " + tds[3].text + ", " + tds[7].text)
                    df.set_value(index, "Country", tds[1].text)
                    df.set_value(index, "2017", tds[2].text)
                    df.set_value(index, "2018", tds[3].text)
                    df.set_value(index, "Rejon", tds[7].text)
                except NoSuchElementException:
                    break
                index = index + 1
        except NoSuchElementException:
            pass
    except NoSuchElementException:
        pass       
    return df

crawlFromStatisticstimes(url).to_csv('data.csv', encoding='utf-8', index=None)
        