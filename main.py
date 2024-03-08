from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(options=options)

LOGIN = ""
PASSWORD = ""


def authforgos (login, password):
    driver.get("https://esia.gosuslugi.ru/login/")
    sleep(5)

    loginform = driver.find_element(By.ID, "login")
    loginform.send_keys(login + Keys.TAB + password + Keys.ENTER)
    sms_code = input()
    loginform = driver.find_element(By.XPATH, "/html/body/esia-root/div/esia-login/div/div/esia-enter-mfa/esia-otp/div/form/div/esia-code-input/div/code-input/span[1]/input")
    loginform.send_keys(sms_code)

def authforportal38 (login, password):
    driver.get('https://portal38.is-mis.ru')
    sleep(5)
    try:
        form = driver.find_element(By.CLASS_NAME, 'no-mobile')
    except:
        pass
    else:
        return
    
    
    form = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[5]/p/a[1]")
    form.click()
    sleep(2)
    form = driver.find_element(By.XPATH, "/html/body/div[20]/div[2]/form[1]/p[1]/input")
    form.send_keys(login + Keys.TAB + password + Keys.ENTER)
    sleep(3)

urls = ['https://portal38.is-mis.ru/service/record/95220/380101000099122/timetable',
        'https://portal38.is-mis.ru/service/record/95220/380101000099119/timetable',
        'https://portal38.is-mis.ru/service/record/95220/380101000099117/timetable'
        ]

def get_status():

        driver.get(urls[0])
        sleep(5)
        if driver.current_url != urls[0]:
            raise NoSuchElementException
        try:
            form = driver.find_element(By.CLASS_NAME, 'free')
        except:
            pass
        else:
            return f'можно записаться к Тугариновой {urls[0]}'
        
        driver.get(urls[1])
        sleep(5)
        try:
            form = driver.find_element(By.CLASS_NAME, 'free')
        except:
            pass
        else:
            return f'можно записаться к Садурской {urls[1]}'
        
        driver.get(urls[2])
        sleep(5)
        try:
            form = driver.find_element(By.CLASS_NAME, 'free')
        except:
            pass
        else:
            return f'можно записаться к Салмину {urls[2]}'
        
        return None
        



if __name__ == '__main__':
    
    # auth(LOGIN, PASSWORD)
    authforportal38(LOGIN, PASSWORD)

    # while True:
    #     get_status()
