import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = None


def Glogin(mail_address, password):
    # Login Page
    driver.get(
        'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

    # input Gmail
    driver.find_element(By.ID, "identifierId").send_keys(mail_address)
    driver.find_element(By.ID, "identifierNext").click()
    driver.implicitly_wait(10)

    # input Password
    driver.find_element(By.XPATH,
                        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "passwordNext").click()
    driver.implicitly_wait(10)

    # go to google home page
    driver.get('https://google.com/')
    driver.implicitly_wait(10)


def turnOffMicCam():
    # turn off Microphone
    time.sleep(2)
    print("switching off micro")
    try:
        micro_off_class = "ZB88ed"
        micro_off = driver.find_element(By.CLASS_NAME, micro_off_class)
        micro_off.click()
    except Exception as e:
        print(f"Error clicking micro: {str(e)}")

    print("switching off camera")
    try:
        camera_off_class = "GOH7Zb"
        camera_off = driver.find_element(By.CLASS_NAME, camera_off_class)
        camera_off.click()
    except Exception as e:
        print(f"Error clicking camera: {str(e)}")

    driver.implicitly_wait(100)


def joinNow():
    # Join meet
    print("in the join now function")
    try:
        jsname_value = "Qx7uuf"
        xpath_expression = f"//button[@jsname='{jsname_value}']"
        button = driver.find_element(By.XPATH, xpath_expression)
        button.click()
    except Exception as e:
        print(f"Error clicking join button: {str(e)}")


def AskToJoin():
    # Ask to Join meet
    time.sleep(3)
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, 'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()

def start_recording():
    try:
        print("opening recording menu")
        jsname_value = "NakZHc"
        xpath_expression = f"//button[@jsname='{jsname_value}']"
        button = driver.find_element(By.XPATH, xpath_expression)
        button.click()
        # recording_class = "VfPpkd-Bz112c-LgbsSe"
        # recording = driver.find_element(By.CLASS_NAME, recording_class)
        # recording.click()
    except Exception as e:
        print(f"Error clicking recording button: {str(e)}")

    try:
        print("starting recording modal")
        jsname_start_value = "wcuPXe"
        xpath_expression = f"//*[@jsname='{jsname_start_value}']"
        button_start = driver.find_element(By.XPATH, xpath_expression)
        button_start.click()
    except Exception as e:
        print(f"Error clicking recording button: {str(e)}")

    try:
        print("clicking checkbox...")
        # checkbox_element = driver.find_element_by_id("c138")
        # checkbox_element.click()
        jsname_checkbox_value = "YPqjbf"
        xpath_expression = f"//*[@jsname='{jsname_checkbox_value}']"
        checkbox_element = driver.find_element(By.XPATH, xpath_expression)
        checkbox_element.click()
    except:
        print(f"Error clicking checkbox button: {str(e)}")

    try:
        print("finalizing...")
        jsname_finalize_value = "A0ONe"
        xpath_expression = f"//button[@jsname='{jsname_finalize_value}']"
        finalize_button = driver.find_element(By.XPATH, xpath_expression)
        finalize_button.click()
    except:
        print(f"Error clicking finalize button: {str(e)}")

    try:
        print('accept...')
        # jscontroller = "soHxf"
        data_mdc_dialog_action = "A9Emjd"
        xpath_expression = f"//button[@data-mdc-dialog-action='{data_mdc_dialog_action}']"
        accept_button = driver.find_element(By.XPATH, xpath_expression)
        accept_button.click()
    except:
        print(f"Could not accept: {str(e)}")



def launch_bot(mail_address, password, meeting_id):
    # create chrome instance
    global driver
    opt = Options()
    opt.add_argument('--disable-blink-features=AutomationControlled')
    opt.add_argument('--start-maximized')
    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 0,
        "profile.default_content_setting_values.notifications": 1
    })
    driver = webdriver.Chrome(options=opt)

    # login to Google account
    Glogin(mail_address, password)

    # go to google meet
    driver.get('https://meet.google.com/' + meeting_id)
    turnOffMicCam()
    # AskToJoin()
    joinNow()
    start_recording()
