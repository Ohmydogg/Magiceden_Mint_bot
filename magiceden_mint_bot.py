from selenium import webdriver
from shutil import which
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

def mint():

        options = Options()
        chrome_path = which("chromedriver")
        options.add_extension("Phantom.crx")
        options.add_argument("--disable-gpu")
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path=chrome_path, options=options)

        driver.get("https://magiceden.io/launchpad/cyber_ape_age")
        driver.maximize_window()
        txt = open("login.txt", 'r')
        read_txt = txt.readlines()
        values = []
        for x in read_txt:
                values.append(x)
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[@class='sc-bdfBQB fatHKg']")))
        recovery_phrase = driver.find_element(By.XPATH,"//button[@class='sc-bdfBQB fatHKg']").click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Secret phrase']")))

        text_area = driver.find_element(By.XPATH,"//textarea[@placeholder='Secret phrase']").send_keys(values[0])
        import_btn = driver.find_element(By.XPATH,"//button[@class='sc-bdfBQB bzlPNH']").click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
        password1 = driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(values[1])
        password2 = driver.find_element(By.XPATH,"//input[@placeholder='Confirm Password']").send_keys(values[1])
        check_box = driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
        submit = driver.find_element(By.XPATH,"//button[@type='submit']").click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Continue')]")))
        continue_ = driver.find_element(By.XPATH,"//button[contains(text(),'Continue')]")
        driver.execute_script ("arguments[0].click();",continue_)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Finish')]")))
        finish = driver.find_element(By.XPATH,"//button[contains(text(),'Finish')]")
        driver.execute_script ("arguments[0].click();",finish)

        main_window = driver.window_handles[0]
        driver.switch_to.window(main_window)

        select_wallet = driver.find_element(By.XPATH,"//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary']")
        select_wallet.click()

        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Phantom')]")))
        phantom = driver.find_element(By.XPATH,"//span[contains(text(),'Phantom')]")
        phantom.click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Connect')]")))
        connect = driver.find_element(By.XPATH,"//span[contains(text(),'Connect')]")
        connect.click()

        original_window = driver.current_window_handle
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(2))
        for window_handle in driver.window_handles:
                if window_handle != original_window:
                        driver.switch_to.window(window_handle)
                        break


        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Connect')]")))
        hamburger = driver.find_element(By.XPATH,"//div[@class='sc-eCstlR gZtcoP']").click()
        popup_connect = driver.find_element(By.XPATH,"//button[contains(text(),'Connect')]")
        popup_connect.click()
        driver.switch_to.window(main_window)


        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Mint your token!')]")))
        mint_your_token = driver.find_element(By.XPATH,"//button[contains(text(), 'Mint your token!')]")
        driver.execute_script ("arguments[0].click();",mint_your_token)

        original_window = driver.current_window_handle
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(2))
        for window_handle in driver.window_handles:
                if window_handle != original_window:
                        driver.switch_to.window(window_handle)
                        break

        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,"//button[contains(text(), 'Approve')]")))
        approve = driver.find_element(By.XPATH,"//button[contains(text(), 'Approve')]")
        approve.click()
        print("Minting Finished")
