# Selenium Amazon Bot: The-CAPTCHA-Slayer
This is a simple python and selenium script/test for the beginners. It contain almost all the basic features you need to know to start writing tests or simple scripts with Selenium. With a little gem against the Amzaon captcha!  

![image](https://github.com/GianIac/SeleniumAmazonBot-The-CAPTCHA-Slayer/assets/80957309/9c268cf7-5cc0-4f95-9663-6ed7b20af0d8)

# Overview 
The script is designed for educational purposes to demonstrate the basics of Selenium for web automation and OCR (optical character recognition) technology for CAPTCHA bypass. Everything is designed to be simple and with few demands, so that it can become a starting point for creating a simple script and maybe defeating some damn CAPTCHA!!!

Features
<li>Website Navigation: Automatically navigates to the Amazon Italy website.</li>
<li>Incognito Mode: Launches Chrome in incognito mode to ensure a clean session without cookies or cached data.</li>
<li>CAPTCHA Bypass: Attempts to bypass Amazon's noBot control CAPTCHA up to 5 times using easyocr for the recognition.</li>
<li>Cookie Rejection: Automatically clicks the "Reject All Cookies" button for privacy.</li>
<li>Product Search: Performs a search for a predefined product ("programmer rubber duck").</li>
<li>Product Interaction: Finds and clicks on the specific product from the search results.</li>
<li>Screenshot: Takes a screenshot of the product page for reference.</li>
<li>Information Extraction: Extracts and saves the product description to a text file.</li>

Technologies Used
- Python 3
- Selenium WebDriver
- easyocr
- PIL (Python Imaging Library)
- numpy
