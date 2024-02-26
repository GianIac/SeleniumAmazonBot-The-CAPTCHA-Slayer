import time
import unittest
import logging
import requests
import easyocr
import numpy as np
from io import BytesIO
from PIL import Image, ImageEnhance
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Amazon_Test(unittest.TestCase):

    def setUp(self):
        # Create an instance of Chrome Options
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        # Creates a webdriver instance with the specified options
        self.driver = webdriver.Chrome(options=chrome_options)

    def tearDown(self):
        self.driver.quit()

    def test_get_and_search_amazon(self):
        """
        Tests successfully reaching the Amazon website and performing a search.

        Steps:
            0. Visit the Amazon website.
            1. Maximize the browser window
            2. Bypass Amazon noBot control (if you are a good boy, you can use the Amazon Developer Api)
            3. Click the "Reject All Cookies" button.
            4. Enter a search query 
            5. Submit the search.
            6. Find the specific product
            7. Click the product link.
            8. Take a screenshot.
            9. Extract and save information from the product description to a txt file.
        """

        # Visit Amazon
        site = "https://www.amazon.it/"
        self.driver.get(site)
        logger.info("Reached Amazon website")

        # Maximize window
        self.driver.maximize_window()
        logger.info("Window maximized")

        #Bypass Amazon noBot control
        for attempt in range(5):  # max 5
            try:
                inputBox = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "captchacharacters"))
                )
                inputBox.send_keys("YOU CAN'T FUCK WITH MY BOTs, MUHAHAHAAH!")
                inputBox.clear()
                captcha_image_url = self.driver.find_element(By.TAG_NAME, 'img').get_attribute('src')
                response = requests.get(captcha_image_url)
                captcha_image = Image.open(BytesIO(response.content))
                enhancer = ImageEnhance.Contrast(captcha_image)
                enhanced_image = enhancer.enhance(2)
                np_image = np.array(enhanced_image)
                reader = easyocr.Reader(['en'])
                results = reader.readtext(np_image)
                captcha_text = ' '.join([result[1] for result in results])
                inputBox.send_keys(captcha_text)
                inputBox.submit()
                logger.info("CAPTCHA attempt submitted.")

                # Please wait briefly and see if the CAPTCHA is still present or if we have been redirected
                time.sleep(2)
                WebDriverWait(self.driver, 3).until_not(
                    EC.presence_of_element_located((By.ID, "captchacharacters"))
                )
                logger.info("CAPTCHA bypassed.")
                break
            except TimeoutException:
                logger.info("CAPTCHA still present or page not loaded as expected, retrying...")

        # Reject cookies
        try:
            cookies_button = self.driver.find_element(By.XPATH, '//*[@id="sp-cc-rejectall-link"]')
            logger.info("Found cookies button")
            cookies_button.click()
            logger.info("Clicked cookies button")
        except NoSuchElementException:
            logger.info("Cookies button not found - continuing without clicking")

        # Search element
        searchtextbox = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        logger.info("Found search textbox")
        searchtextbox.send_keys("THIS SCRIPT CONTAINS THE BASIC SELENIUM FUNCTIONS FOR BEGINNERS! ")
        logger.info("Entered search query")
        time.sleep(5)  # Wait for search results to load (modify as needed)
        searchtextbox.clear()
        searchtextbox.send_keys("programmer rubber duck")
        logger.info("Entered specific product search")
        searchtextbox.submit()
        logger.info("Submitted search")

        # Find specific product
        element_prd = self.driver.find_element(By.XPATH, f"//*[contains(text(), 'Munchkin White Hot Safety Rubber Bath Duck Toy, Pack of 1')]")
        logger.info("Found product element")
        element_prd.click()
        logger.info("Clicked product link")

        # Take screenshot
        self.driver.save_screenshot("screen.png")
        logger.info("Saved screenshot")

        # Extract and save product information
        info_elm = self.driver.find_element(By.ID, "feature-bullets")
        info_text = info_elm.text
        with open("info_div.txt", "w", encoding="utf-8") as file:
            file.write(info_text)
        logger.info("Saved product information to 'info_div.txt'")

#**Run the Test:**
if __name__ == '__main__':
    unittest.main()
