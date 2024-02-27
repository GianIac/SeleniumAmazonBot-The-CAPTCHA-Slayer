# Selenium Amazon Bot: The-CAPTCHA-Slayer
This is a simple python and selenium script/test for the beginners. It contains almost all the basic features you need to know to start writing tests or simple scripts with Selenium. With a little gem against the Amazon captcha!  

![image](https://github.com/GianIac/SeleniumAmazonBot-The-CAPTCHA-Slayer/assets/80957309/9c268cf7-5cc0-4f95-9663-6ed7b20af0d8)

# Overview 
The script is designed for educational purposes to demonstrate the basics of Selenium for web automation and OCR (optical character recognition) technology for CAPTCHA bypass. Everything is designed to be simple and with few demands, so that it can become a starting point for creating a simple script and maybe defeating some damn CAPTCHA!!!

<h5>Features</h5>
<li>Website Navigation: Automatically navigates to the Amazon Italy website.</li>
<li>Incognito Mode: Launches Chrome in incognito mode to ensure a clean session without cookies or cached data.</li>
<li>CAPTCHA Bypass: Attempts to bypass Amazon's noBot control CAPTCHA up to 5 times using easyocr for the recognition.</li>
<li>Cookie Rejection: Automatically clicks the "Reject All Cookies" button for privacy.</li>
<li>Product Search: Performs a search for a predefined product ("programmer rubber duck").</li>
<li>Product Interaction: Finds and clicks on the specific product from the search results.</li>
<li>Screenshot: Takes a screenshot of the product page for reference.</li>
<li>Information Extraction: Extracts and saves the product description to a text file.</li>
<p></p>

<h5>Technologies Used</h5>
<li>Python 3</li>
<li>Selenium WebDriver</li>
<li>easyocr</li>
<li>PIL (Python Imaging Library)</li>
<li>numpy</li>
<br>

![image](https://github.com/GianIac/SeleniumAmazonBot-The-CAPTCHA-Slayer/assets/80957309/22f1fb46-6d44-4544-9b59-6dda6c7f3efa)

# Installation and Setup
Before running the script, you need to install several dependencies. Make sure you have Python 3 installed on your system. You can download Python 3 from here:
https://www.python.org/downloads/
Install Dependencies
Open your terminal or command prompt and install the required Python packages using pip, Python's package installer. 
Run the following commands:
<h6> >> pip install -r requirements.txt</h6>

<h5>Libraries Used:</h5>
<li>Selenium WebDriver: Automates web browser interaction from Python. 
  [Selenium Documentation] (https://www.selenium.dev/documentation/)</li>
<li>Requests: Simplifies making HTTP requests. 
  [Requests Documentation] (https://pypi.org/project/requests/)</li>
<li>easyocr: Performs Optical Character Recognition (OCR) to read text from images. 
  [easyocr GitHub](https://github.com/JaidedAI/EasyOCR/tree/master) && [easyocr for py] https://pypi.org/project/easyocr/</li>
<li>Pillow (PIL Fork): Python Imaging Library adds image processing capabilities. 
  [Pillow Documentation] (https://pillow.readthedocs.io/en/stable/)</li>
<li>NumPy: Adds support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions. 
  [NumPy Documentation] (https://numpy.org/)</li>
<br>
<h5>Running the Script</h5>
Once all dependencies are installed you can run the script with the following command in your terminal or command prompt:
<h6> >> python main.py</h6>

CAPTCHA bypass --> Execution video:
https://github.com/GianIac/SeleniumAmazonBot-The-CAPTCHA-Slayer/assets/80957309/7861e46b-f008-4d4c-b4d4-3607c242ee41




# Notes
If you prefer not to download all libraries locally, you can set up a virtual environment using either PyCharm or Visual Studio Code, depending on your preference.
For PyCharm:
Go to "File" > "New Project" to create a new project.
Clone the desired repository into the project directory.
Open "File" > "Settings" (or press CTRL+ALT+S) to access the settings.
Navigate to "Project: [project's name]" > "Python Interpreter".
Click on the "+" symbol to add a new interpreter.
From here, you can set up a new virtual environment and add the necessary libraries to your project by searching for and installing them through the provided graphical interface.

<h3>Ethics:</h3>
Ok bro... I have to write this, bypassing the CAPTCHA is unethical, sites like Amazon offer APIs for developers!
I created this script for educational purposes only. I hope Jeff Bezos doesn't hate me :) 

