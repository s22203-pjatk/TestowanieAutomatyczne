from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import logging
import time

logger = logging.getLogger('s22203')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driver = webdriver.Chrome()

try:
    # Test 1
    logger.info('Przechodzę na stronę z grami komputerowymi')
    driver.get('https://s22203-pjatk.vercel.app/')
    driver.maximize_window()
    logger.info('OK!')
    time.sleep(2)

    # Test 2
    logger.info('Przełączam dark mode')
    temp = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'chakra-switch')))
    temp.click()
    logger.info('OK!')
    time.sleep(2)

    # Test 3
    logger.info('Wyszukam grę -GTA V- w wyszukiwarce')
    temp = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'chakra-input__group')))
    temp.click()
    search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'chakra-input')))
    search_input.send_keys('GTA V', Keys.RETURN)
    logger.info('OK!')
    time.sleep(2)

    # Test 4
    logger.info('Przewijam stronę na dół')
    driver.execute_script("window.scrollTo(0, 600);")
    logger.info('OK!')
    time.sleep(2)

except Exception as e:
    logger.error(f'Test failed: {str(e)}')

finally:
    driver.close()