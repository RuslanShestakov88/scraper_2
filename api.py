import os
import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

mail_name = input("mail adress? ")
password = input("password? ")
params = '{"mail adress":"%s","password":"%s"}'%(mail_name, password)

def write_json(new_data, filename="MailPass.JSON"):
    
    desired_dir = "/home/Ruslan/PycharmProjects/scraper_to_docker/"
    full_path = os.path.join(desired_dir, filename)

    with open(full_path, 'w') as f:
        json_string = json.dumps(new_data)
        f.write(json_string)

    '''SCARPER'''

def reader(path):
    # opening JSON file
    with open(path) as file:
        data = json.load(file)
        dictionary = json.loads(data)

        mail_name = dictionary['mail adress']
        password = dictionary['password']

    return mail_name, password
    
def scraper(mail_name, password):    
    '''serching information you need'''
    print("============================")
    print(mail_name)
    print(password)
    print("============================")

    # Open Browser and searching page we need
    url = "https://account.proton.me/signup"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    browser.maximize_window()
    browser.implicitly_wait(20)
    
    iframe = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/iframe')
    browser.switch_to.frame(iframe)
    sleep(1)
    browser.find_element(By.ID, "email").send_keys(mail_name)
    browser.switch_to.default_content()
    sleep(1)
    
    browser.find_element(By.ID, "password").send_keys(password)
    sleep(1)
    browser.find_element(By.ID, "repeat-password").send_keys(password)
    sleep(1)

    # browser.find_element(By.CLASS_NAME, "button w100 button-large button-solid-norm mt1-5").click()
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/button').click()
    sleep(3)

    iframe_local = browser.find_element(By.XPATH, '//*[@id="key_0"]/iframe')
    browser.switch_to.frame(iframe_local)
    iframe_check = browser.find_element(By.XPATH, '//*[@id="html_element"]/iframe')
    browser.switch_to.frame(iframe_check)
    browser.find_element(By.ID, "checkbox").click()
    # browser.find_element(By.XPATH, '//*[@id="checkbox"]').click()
    browser.switch_to.default_content
    sleep(3)

#a = write_json(params)
path = "MailPass.JSON"
b = reader(path)
c = scraper(mail_name, password)