import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

on = True
while on:
    def five_seconds():
        time.sleep(5)
        driver_location = "/usr/bin/chromedriver" # Need to change to location of the chromedriver
        binary_location = "/usr/bin/google-chrome" # Need to change to location of the google-chrome

        options = webdriver.ChromeOptions()
        options.binary_location = binary_location

        driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)


        driver.get("https://www.amazon.pl/Kalado-Odkurzacz-Bezprzewodowy-Odkurzacze-Bezszczotkowy/dp/B09PMKYLK4/ref=sr_1_9?__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=39AZF0QT0GS10&keywords=odkurzacz&qid=1684528587&sprefix=odkurzac%2Caps%2C107&sr=8-9")
        price = driver.find_element(By.CLASS_NAME, "a-price-whole")
        print(price.text)
        driver.quit()
    five_seconds()