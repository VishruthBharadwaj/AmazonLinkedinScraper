from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

import time
def run(email, password):

	driver_path = 'G:\\Amazonproductinfoscraper\\chromedriver'

	options = webdriver.ChromeOptions()
	#Commented headless for view of chrome
	# options.add_argument('--headless')
	driver = webdriver.Chrome(options=options, executable_path=driver_path)
	driver.get('https://www.linkedin.com/')

	#Login username/password
	email_box = driver.find_element_by_id('session_key')
	email_box.send_keys(email)
	pass_box = driver.find_element_by_id('session_password')
	pass_box.send_keys(password)
	submit_button = driver.find_element_by_class_name('sign-in-form__submit-button')
	submit_button.click()
	search_text = 'AutoDS'

	search_container = driver.get('https://www.linkedin.com/search/results/all/?keywords='+search_text)

	driver.find_elements_by_xpath('.//span[@class = "entity-result__title-text t-16"]')[0].click()
	time.sleep(10)
    
		
un = input('Enter your Email: ')
pw = input('Enter your Password: ')
run(un, pw)
