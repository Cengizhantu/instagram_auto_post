import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
from selenium.webdriver.common.by import By


def post(username, password, name, caption):
    browser = webdriver.Chrome("Your Chromedriver extension")
    browser.get("https://www.instagram.com/")

    mail = browser.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input")
    mail.send_keys(username)

    sifre = browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")

    sifre.send_keys(password)
    time.sleep(1)

    giris = browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]")
    giris.click()
    time.sleep(6)

    upload_btn = browser.find_element(By.CSS_SELECTOR,
                                      "#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg.KtFt3 > div > div:nth-child(3) > div > button > div > svg")
    upload_btn.click()

    time.sleep(1)

    select_btn = browser.find_element(By.CSS_SELECTOR,
                                      "body > div.RnEpo.gpWnf.Yx5HN > div.pbNvD > div > div > div > div.uYzeu > div._C8iK > div > div > div.qF0y9.Igw0E.rBNOH.eGOV_.ybXk5._4EzTm.kEKum > div > button")
    select_btn.click()

    # file_path = r"Your post file path"
    # time.sleep(1)
    # pyautogui.write(filepath)

    pyautogui.write("Your first step")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write("Your second step")
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(name)  # Your post image name
    pyautogui.press('enter')
    time.sleep(7)
    # Don't forget to edit if you have more steps

    nxt_btn = browser.find_element(By.CSS_SELECTOR,
                                   "body > div.RnEpo.gpWnf.Yx5HN > div.pbNvD > div > div > div > div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm > div > div > div.WaOAr._8E02J > div > button ")

    nxt_btn.click()

    time.sleep(1)

    nxt_btn2 = browser.find_element(By.CSS_SELECTOR,
                                    "body > div.RnEpo.gpWnf.Yx5HN > div.pbNvD > div > div > div > div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm > div > div > div.WaOAr._8E02J > div > button")
    nxt_btn2.click()

    # caption = 'Your caption'  # Write a caption
    time.sleep(2)
    cptn = browser.find_element(By.XPATH,
                                "/html/body/div[6]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea")
    cptn.send_keys(caption)
    time.sleep(1)
    pst_btn = browser.find_element(By.CSS_SELECTOR,
                                   'body > div.RnEpo.gpWnf.Yx5HN > div.pbNvD > div > div > div > div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm > div > div > div.WaOAr._8E02J > div > button')
    pst_btn.click()

    time.sleep(10)  # Upload Time, it depends on your file size and internet speed

    browser.quit()

    print('''
    I did it mission accomplished.
    ''')


post("username", "password", "name", "caption")