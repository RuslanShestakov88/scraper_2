import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import pymysql
from db_config import host, user, password, db_name



def connect_se () -> dict:
    os.chdir("/home/Ruslan/PycharmProjects/scraper")
    os.getcwd()
    currency_ = "$"
    url = "https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273?ad=offering"
    rq = {"price": 0, "city": "city", "description": "descriptse", "bedroom": "bedroom"}
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)

    pricese = browser.find_element(By.CLASS_NAME, 'price')
    price = pricese.text
    rq["price"] = price

    cityse = browser.find_element(By.CLASS_NAME, 'location')
    city = cityse.text
    rq["city"] = city
    
    descriptse = browser.find_element(By.CLASS_NAME, 'description')
    descript = descriptse.text
    rq["description"] = descript

    bedroomse = browser.find_element(By.CLASS_NAME, 'bedrooms')
    bedroom = bedroomse.text
    rq["bedroom"] = bedroom

    print(rq)
    return rq
    

qr = connect_se()



""" не отработиадло, попал на AttributeError: 'NoneType' object has no attribute 'cursor'
 решение нашел или не нашел в обзем не заработало """

try:
    connection = pymysql.connect(
        host = host,
        port=3306,
        user = user,
        password = password,
        database = db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("slava bogu")

    try:
        with connection.cursor() as cursor:
            create_table_query = "CREATE_TABLE 'rent'(id int)"
    finally:
        connection.close()

except Exception as ex:
    print("conection refused")
    print (ex)


""""не отработалоб попал на 
2003, "Can't connect to MySQL server on 'localhost' ([Errno 111] Connection refused"""
def create_connection_mysql(db_host, user_name, user_password, db_name = None):
    connection_db = None
    try:
        connection_db = mysql.connector.connect(
            host = db_host,
            user = user_name,
            password = user_password,
            database = db_name,
        )
        print("connected")
    except Error as db_connection_errors:
        print("raised err", db_connection_errors)
    return connection_db

conn = create_connection_mysql(db_config["mysql"]["host"],
                               db_config["mysql"]["user"],
                               db_config["mysql"]["pass"],)
# cur = conn.cursor()
with conn.cursor() as cur:
    cur = conn.cursor()
    create_db_sql_query = "CREATE DATABASE {}".format('first')
    cur.execute(create_db_sql_query)
    cur.close()
    conn.close()

conn = create_connection_mysql(db_config["mysql"]["host"],
                               db_config["mysql"]["user"],
                               db_config["mysql"]["pass"],)

with conn.cursor() as cur:
    cur = conn.cursor()
    create_db_sql_query = 
    """creation table like
    CREATE TABLE IF NOT EXIST rent (id INT AUT_INCREMENT,
                                    price: CHAR_FIELD NOT NULL,
                                    city: CHAR_FIELD NOT NULL,
                                    description: TEXT_FIELD NOT NULL,
                                    bedroom: CHAR_FIELD NOT NULL,)
     """
    cur.execute(create_db_sql_query)
    conn.commit()

    """"INSERT INTO 'rent'(rq)"""
    cur.execute(create_db_sql_query)
    conn.commit()


# create_connection_mysql()