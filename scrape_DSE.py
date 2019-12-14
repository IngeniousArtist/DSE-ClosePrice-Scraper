import csv
from selenium import webdriver

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

driver.find_element_by_xpath(from_date).send_keys("01/01/2015")
driver.find_element_by_xpath(to_date).send_keys("30/06/2015")
driver.find_element_by_xpath(btn).click()

table_path = "/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td[1]/table"
table = driver.find_element_by_xpath(table_path)
with open('/Users/shahriyer/Desktop/code/data_2015_1.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile)
    for row in table.find_elements_by_tag_name('tr'):
        wr.writerow([d.text for d in row.find_elements_by_tag_name('td')])

driver.close()