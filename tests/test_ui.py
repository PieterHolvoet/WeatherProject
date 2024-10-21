from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_weather_search():
    driver = webdriver.Chrome()
    driver.get('http://localhost:5000/')
    city_input = driver.find_element_by_id('city')
    city_input.send_keys('New York')
    city_input.send_keys(Keys.RETURN)
    # Add logic to check if the result is displayed correctly.
    driver.quit()
