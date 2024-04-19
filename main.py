import unittest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from easyocr import Reader
import numpy as np
from PIL import Image, ImageEnhance
import requests
from io import BytesIO

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AmazonTest(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_search_amazon(self):
        self.driver.get("https://www.amazon.it/")
        logger.info("Accessed Amazon website")
        self.handle_captcha()
        self.reject_cookies()
        self.perform_search("programmer rubber duck")
        self.access_product_page()
        self.take_screenshot()
        self.save_product_information()

    def handle_captcha(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "captchacharacters")))
            captcha_image_url = self.driver.find_element(By.TAG_NAME, 'img').get_attribute('src')
            captcha_image = Image.open(BytesIO(requests.get(captcha_image_url).content))
            enhancer = ImageEnhance.Contrast(captcha_image)
            enhanced_image = enhancer.enhance(2)
            np_image = np.array(enhanced_image)
            reader = Reader(['en'])
            results = reader.readtext(np_image)
            captcha_text = ' '.join([result[1] for result in results])
            input_box = self.driver.find_element(By.ID, "captchacharacters")
            input_box.send_keys(captcha_text)
            input_box.submit()
            WebDriverWait(self.driver, 5).until_not(EC.presence_of_element_located((By.ID, "captchacharacters")))
            logger.info("CAPTCHA successfully bypassed")
        except TimeoutException:
            logger.info("CAPTCHA was not present or resolved automatically")

    def reject_cookies(self):
        try:
            cookies_button = self.driver.find_element(By.XPATH, '//*[@id="sp-cc-rejectall-link"]')
            cookies_button.click()
            logger.info("Rejected all cookies")
        except NoSuchElementException:
            logger.info("Cookies button not found")

    def perform_search(self, query):
        search_box = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        search_box.clear()
        search_box.send_keys(query)
        search_box.submit()
        logger.info(f"Performed search for {query}")

    def access_product_page(self):
        product_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Munchkin White Hot Safety Rubber Bath Duck Toy')]"))
        )
        product_link.click()
        logger.info("Accessed product page")

    def take_screenshot(self):
        self.driver.save_screenshot("screen.png")
        logger.info("Screenshot saved")

    def save_product_information(self):
        info_element = self.driver.find_element(By.ID, "feature-bullets")
        with open("product_info.txt", "w", encoding="utf-8") as file:
            file.write(info_element.text)
        logger.info("Product information saved to file")

if __name__ == '__main__':
    unittest.main()
