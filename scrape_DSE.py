#DSE BD Closing Price Scraper
#by
#http://github.com/IngeniousArtist

import csv
from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup

start = datetime.now()

chromedriver_location = "/Users/shahriyer/Desktop/code/chromedriver"
driver = webdriver.Chrome(chromedriver_location)
driver.get('http://dsebd.org/data_archive.php')

from_date = '//*[@id="ClosePDate"]'
to_date = '//*[@id="ClosePDate1"]'
btn = '/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/input'

from_element =driver.find_element_by_xpath(from_date)
driver.execute_script("arguments[0].min = '2015-01-01'", from_element)
to_element =driver.find_element_by_xpath(to_date)
driver.execute_script("arguments[0].min = '2015-01-01'", to_element)

#10957 Rows
driver.find_element_by_xpath(from_date).send_keys("01/01/2015")
driver.find_element_by_xpath(to_date).send_keys("30/06/2015")
driver.find_element_by_xpath(btn).click()

content = driver.page_source

soup = BeautifulSoup(content, 'lxml')

driver.close()

stock_table = soup.find("table", attrs={"border":"0", "cellpadding":"3", "width":"100%","bgcolor":"#808000", "cellspacing":"1"})
stock_table_data = stock_table.tbody.find_all("tr")  # contains whatever rows

print("Number of Rows in Dataset:")
print(len(stock_table_data))

data = [[] for x in range(len(stock_table_data)-1)]

for i in range(len(stock_table_data)-1):
    for td in stock_table_data[i].find_all("td"):
        data[i].append(td.font.text)

with open("/Users/shahriyer/Desktop/code/Data_2015_1.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(data)

finish = datetime.now() - start

print("TIME TAKEN TO COMPLETE:")
print(finish)
