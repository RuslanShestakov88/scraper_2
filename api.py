import os
import json
import re
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

where_from = input("Where from? ")
where_to = input("Where to? ")
when = input("when a you going to? Correct format: -->day-D-M-YYYY<--  :")
params = '{"sity_from":"%s","sity_to":"%s","date_flygo":"%s"}'%(where_from, where_to, when)

def write_json(new_data, filename="Report.JSON"):
    
    desired_dir = "/home/Ruslan/PycharmProjects/scraper/"
    full_path = os.path.join(desired_dir, filename)

    with open(full_path, 'w') as f:
        json_string = json.dumps(new_data)
        f.write(json_string)

    '''SCARPER'''

def searcher(path):
    # opening JSON file
    with open(path) as file:
        data = json.load(file)
        dictionary = json.loads(data)

        sity_from = dictionary['sity_from']
        sity_to = dictionary['sity_to']
        date_flygo = dictionary['date_flygo']
    
    '''serching information you need'''
    
    # Open Browser and searching page we need
    url = "https://fly2.emirates.com/CAB/IBE/SearchAvailability.aspx"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    browser.maximize_window()
    sleep(2)
    
    # acception coocie and entring search page
    
    browser.find_element(By.ID, "onetrust-accept-btn-handler").click()
    browser.find_element(By.CLASS_NAME, "ts-session-expire--link").click()
    sleep (2)
    browser.find_element(By.ID, 'dvRadioOneway').click()
    sleep(2)

    browser.find_element(By.ID, "ctl00_c_CtWNW_ddlFrom-suggest").send_keys(sity_from)
    browser.find_element(By.ID, "ctl00_c_CtWNW_ddlFrom-suggest_option_1").click()

    browser.find_element(By.ID, "ctl00_c_CtWNW_ddlTo-suggest").send_keys(sity_to)
    browser.find_element(By.ID, "ctl00_c_CtWNW_ddlTo-suggest_option_1").click()

    sleep(1)
    browser.find_element(By.ID, 'txtDepartDate').click()
    browser.find_element(By.ID, date_flygo).click()
    sleep(2)

    browser.find_element(By.ID, 'ctl00_c_IBE_PB_FF').click()
    sleep(45)
    

    # find quatity of results
    kolich_result = browser.find_element(By.CLASS_NAME, 'ts-fbr-flight-list__header-title-content').text
    str(kolich_result)
    kolich_result_list = re.findall('(\d+)', kolich_result)
    k = int(kolich_result_list[0])

    '''scrapping information you need'''

    # selecktors for scraping first 5 results (site allways gives only 5 rusult for start)
    time_list = []
    price_list = []
    i = 0
    while i <= 4 :
        time = browser.find_element(By.ID, f'ctl00_c_FlightResultOutBound_rptBoundResult_ctl0{i}_timeDepart').text
        time_list.append(time)
        
        price_f = browser.find_element(By.ID, f'ctl00_c_FlightResultOutBound_rptBoundResult_ctl0{i}_rptClasses_ctl00_dvCabin').text
        price = int(re.search(r'\d+', price_f).group())
        price_list.append(price)
        i += 1
    
    browser.find_element(By.ID, 'ctl00_c_FlightResultOutBound_ancShowMore').click()
    sleep(4)
    
    # selecktors for scraping other results
    # Didn't use find_elementS because of choise
    j = 0    
    while j <= k - i - 1:
        time = browser.find_element(By.ID, f'rptBoundResult_ctl0{j}_timeDepart').text
        time_list.append(time)
        price_f = browser.find_element(By.ID, f'rptBoundResult_ctl0{j}_rptClasses_ctl00_dvCabin').text
        price = int(re.search(r'\d+', price_f).group())
        price_list.append(price)
        j += 1

    # packing all info to format we need
    dep_listing = []
    for i in range(len(time_list)):
        dict = {'time': time_list[i], 'price': price_list[i]}
        dep_listing.append(dict)
    
    print(dep_listing, sep='\n')
    
    
a = write_json(params)
path = "Report.JSON"
b = searcher(path)