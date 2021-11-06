from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions import action_builder
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import time
from selenium.common import exceptions
# from pyotp import *

# def msotpauth(msdata):
#     totp = TOTP("THISWASATESTTOIMPLEMENTMFABUTITFAILED")    
#     msotpauth.token = totp.now()


msdata = {"skuurl": "https://admin.microsoft.com/#/subscriptions/webdirect/INSERT-SKUURL-INFORMATION",
            "msun": "ENTERBILLINGADMINEMAIL@conglomo.com",
            "mspd": "SUPERLONGBILLINGADMINPASSWORDTHATNOONESHOULDNOOFEVER",
            "licensechoice": "Add License"}

def browser_options():
    options = Options()
    options.headless = True
    browser_options.browser = webdriver.Chrome(options=options)
    return browser_options.browser
browser_options()



def mslogin():
    #Go to the specific subscription in question
    browser_options.browser.get(msdata["skuurl"])
    ms_username = browser_options.browser.find_element_by_css_selector('#i0116')
    ms_username.send_keys(msdata["msun"])

    #login using username and password
    ms_usernameaccept = browser_options.browser.find_element_by_css_selector('#idSIButton9')
    ms_usernameaccept.send_keys(Keys.ENTER)

    wait = WebDriverWait(browser_options.browser, 5)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#i0118')))
    ms_password = browser_options.browser.find_element_by_css_selector('#i0118')
    ms_password.send_keys(msdata["mspd"])

    ms_passwordaccept = browser_options.browser.find_element_by_css_selector('#idSIButton9')
    ms_passwordaccept.send_keys(Keys.ENTER)

    #MFA implementation if there is a way to get pyotp to work with 64base qrcodes
    # wait = WebDriverWait(browser_options.browser, 5)
    # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#idTxtBx_SAOTCC_OTC')))
    # im_username = browser_options.browser.find_element_by_css_selector('#idTxtBx_SAOTCC_OTC')
    # msotpauth()
    # im_username.send_keys(msotpauth.token)

    # im_username = browser_options.browser.find_element_by_css_selector('#idSIButton9')
    # im_username.send_keys(Keys.ENTER)

    #Getting past the reduced password inquiry webpage
    wait = WebDriverWait(browser_options.browser, 5)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#idBtn_Back')))
    reducedlogingcancel = browser_options.browser.find_element_by_css_selector('#idBtn_Back')
    reducedlogingcancel.send_keys(Keys.ENTER)
    

    #if statement flow to dictate what to do if you are adding a license or removing a license
    if msdata["licensechoice"] == "Add License":
        wait = WebDriverWait(browser_options.browser, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[starts-with(@aria-label, 'Buy licenses')]")))
        buylicensebutton = browser_options.browser.find_element_by_xpath("//*[starts-with(@aria-label, 'Buy licenses')]")
        buylicensebutton.send_keys(Keys.ENTER)



        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[starts-with(@class, 'ms-spinButton-input')]")))
        addlicenseinput = browser_options.browser.find_element_by_xpath("//*[starts-with(@class, 'ms-spinButton-input')]")
        addlicenseinputvalue = browser_options.browser.find_element_by_xpath("//*[starts-with(@class, 'ms-spinButton-input')]").get_attribute("aria-valuemin")

    
        addlicenseinputvalueint = int(addlicenseinputvalue) + 1
        addlicenseinputvaluestr = str(addlicenseinputvalueint)
        addlicenseinput.send_keys(Keys.CONTROL + "a")
        addlicenseinput.send_keys(Keys.CONTROL + "x")
        addlicenseinput.send_keys(addlicenseinputvaluestr)
        
        time.sleep(1)

        #accepting your additional license
        actions = ActionChains(browser_options.browser)
        actions.move_to_element(addlicenseinput)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    else:
        wait = WebDriverWait(browser_options.browser, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[starts-with(@aria-label, 'Remove licenses')]")))
        removelicensebutton = browser_options.browser.find_element_by_xpath("//*[starts-with(@aria-label, 'Remove licenses')]")
        removelicensebutton.send_keys(Keys.ENTER)



        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[starts-with(@class, 'ms-spinButton-input')]")))
        removelicenseinput = browser_options.browser.find_element_by_xpath("//*[starts-with(@class, 'ms-spinButton-input')]")
        removelicenseinputvalue = browser_options.browser.find_element_by_xpath("//*[starts-with(@class, 'ms-spinButton-input')]").get_attribute("aria-valuemax")

        removelicenseinputvalueint = int(removelicenseinputvalue) - 1
        removelicenseinputvaluestr = str(removelicenseinputvalueint)
        removelicenseinput.send_keys(Keys.CONTROL + "a")
        removelicenseinput.send_keys(Keys.CONTROL + "x")
        removelicenseinput.send_keys(removelicenseinputvaluestr)
        
        time.sleep(1)

        #Confirming the removal of the license
        actions = ActionChains(browser_options.browser)
        actions.move_to_element(removelicenseinput)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ENTER)
        actions.perform()

mslogin()
