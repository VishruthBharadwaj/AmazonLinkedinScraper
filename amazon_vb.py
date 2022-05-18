from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, datetime
from compare_days import dt 
today = date.today()

def convert_price_toNumber(price):
    price = price.split("₹")[1]
    try:
        price = price.split("\n")[0] + "." + price.split("\n")[1]
    except:
        Exception()
    try:
        price = price.split(",")[0] + price.split(",")[1]
    except:
        Exception()
    return float(price)
web = 'https://www.amazon.in'
driver_path = 'G:\\Amazonproductinfoscraper\\chromedriver'

options = webdriver.ChromeOptions()
#Commented headless for view of chrome
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options, executable_path=driver_path)

driver.get(web)

driver.implicitly_wait(5)
keyword = "Coffe Cups"
search = driver.find_element_by_xpath('//*[(@id = "twotabsearchtextbox")]')
search.send_keys(keyword)
# click search button
search_button = driver.find_element_by_id('nav-search-submit-button')
search_button.click()

driver.implicitly_wait(5)

list_of_dates = []
items = wait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')))
for item in items:
    # Prime Items
    datasss = item.find_elements_by_xpath(".//i[contains(@class,'a-icon a-icon-prime')]")

    if datasss!=[]:

        data_asin = item.get_attribute("data-asin")
        
        price = convert_price_toNumber(item.find_element_by_class_name('a-price').text)
        name = item.find_element_by_tag_name('h2')
        real_name = name.text
        date_to_get = item.find_element_by_css_selector("span[class='a-color-base a-text-bold']")
        date_to_get.click()
        date_to_get_ = date_to_get.text
        date_to_get_ = str(date_to_get_)
        date_to_get__ = date_to_get_.split(", ")
        date_to_get__ = date_to_get__[1]
        parsed = datetime.strptime(date_to_get__, '%b %d').date().replace(year=today.year)

        if list_of_dates==[]:
            list_of_dates.append(parsed)
        else:
            if parsed<list_of_dates[-1]:
                list_of_dates.append(parsed)
        
        if list_of_dates[-1]<=dt:

            
            #Considering the item with least delivery date
            date_to_get.click()
            j = 'https://www.amazon.in/' + 'dp/' + data_asin
            driver.get(j)
            driver.find_element_by_name('submit.add-to-cart').click()
            print('***********Adding to card**************** ')
            driver.quit()




