# import required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
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
    driver.find_element(By.XPATH,
                        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()

    # turn off camera
    time.sleep(1)
    driver.find_element(By.XPATH,
                        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
    driver.implicitly_wait(3000)


def joinNow():
    # Join meet
    print("in the join now function")
    try:
        text_to_click = "Join now"

        # Construct an XPath that finds any element by its innerHTML containing the specified text
        # xpath_expression = f"//*[contains(., '{text_to_click}')]"
        jsname_value = "Qx7uuf"
        xpath_expression = f"//button[@jsname='{jsname_value}']"

        # Wait until the element is clickable
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_expression)))
        # Wait for the button to be clickable
        button = driver.find_element(By.XPATH, xpath_expression)
        # driver.find_element(By.XPATH, "//span[contains(text(), 'Join now')]").click()
        button.click()

        # button = WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, xpath_expression))
        # )
        print("we see the button on page:")
        # print(button)
        # Click the button
        # actions = ActionChains(driver)
        # actions.move_to_element(button).perform()
        # actions.click().perform()
    except Exception as e:
        print(f"Error clicking button: {str(e)}")

    # button_1 = driver.find_element(By.CSS_SELECTOR,
    #                                'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt')
    # if button_1:
    #     button_1.click()
    # else:
    #     button = driver.find_element(By.XPATH, "//span[text()='Ask to join']")
    #     if (button):
    #         button.click()
    #     else:
    #         button = driver.find_element(By.XPATH, "//span[text()='Join now']")
    #         if (button):
    #             button.click()
    #         else:
    #             button_2 = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
    #             if (button_2):
    #                 button_2.click()


def AskToJoin():
    # Ask to Join meet
    time.sleep(3)
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, 'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()


# Ask to join and join now buttons have same xpaths


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
    # turnOffMicCam()
    # AskToJoin()
    joinNow()
