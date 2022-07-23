import time
import tkinter as tk
from tkinter import simpledialog

import lxml
import requests as req
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import models as m

# python -m pip install requests

NUI = ''
root = tk.Tk()
root.withdraw()
NUI = simpledialog.askstring("NUI",
                             "Enter NUI:",
                             parent=root)

chrome_driver_path = "C:/Users/Admin/Development/chromedriver.exe"
driver_service = Service(executable_path=chrome_driver_path)

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-setuid-sandbox")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=driver_service, options=chrome_options)

web_url = 'https://arbk.rks-gov.net/'
driver.get(web_url)

txtNUI = driver.find_element(By.ID, 'txtNumriBiznesit')
txtNUI.send_keys(NUI)
# 80400721

# main_page = driver.window_handles[0]
btnSubmit = driver.find_element(By.ID, 'Submit1')
btnSubmit.click()

time.sleep(3)

for handle in driver.window_handles:
    driver.switch_to.window(handle)

row = driver.find_element(
    By.CSS_SELECTOR, 'table.views-table.cols-4 tbody tr td a')

response = req.get(row.get_attribute('href'))
soup = BeautifulSoup(response.text, 'lxml')

business_data_table = soup.select('table.views-table.cols-4')
business_data = business_data_table[0].select('tbody tr')

business = m.BusinessInfo()
business.Name = business_data[0].select('td > span')[0].getText().strip()
business.TradeName = business_data[1].select('td > span')[0].getText().strip()
business.Type = business_data[2].select('td > span')[0].getText().strip()
business.NUI = business_data[3].select('td > span')[0].getText().strip()
business.BusinessNo = business_data[4].select('td > span')[0].getText().strip()
business.FiscalNo = business_data[5].select('td > span')[0].getText().strip()
business.NoOfEmployees = business_data[7].select('td > span')[
    0].getText().strip()
business.RegistrationDate = business_data[8].select('td > span')[
    0].getText().strip()
business.Municipality = business_data[9].select('td > span')[
    0].getText().strip()
business.Address = business_data[10].select('td > span')[0].getText().strip()
business.PhoneNo = business_data[11].select('td > span')[0].getText().strip()
business.Email = business_data[12].select('td > span')[0].getText().strip()
business.KBRAStatus = business_data[14].select('td > span')[
    0].getText().strip()
business.TAKStatus = business_data[16].select('td > span')[0].getText().strip()
business.BaseURL = row.get_attribute('href')
print()
print(business)

time.sleep(3)
driver.quit()
