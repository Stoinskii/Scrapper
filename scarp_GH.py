from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

options = webdriver.ChromeOptions()
options.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)


driver.get("https://github.com/usernam121")
repo = "https://github.com/usernam121"
#time.sleep(2)
res = driver.find_elements(By.CLASS_NAME, "repo")
link = []
flink = []

def going_for_raw(second_page):
    print("OK")
    driver.get(second_page)
    raw = driver.find_element(By.LINK_TEXT, "/repository/raw")
    #raw.click()
    #html = driver.page_source
    #html = f"{html}"
    #if "password" in html:
    #    print(f"found password {second_page}")

def loop(next_page):
    global a
    driver.get(next_page)
    res2 = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
    for a in res2:
        pass
        print(a.text)
    if "py" in a.text:
        second_page = f"{repo}/blob/main//{a.text}"
        going_for_raw(second_page)


#   elif "js" in a.text:
#      print("It worked .js is in the text")


for i in res:
    link.append(i.text)

for l in link:
    next_page = f"{repo}/{l}"
    flink.append(next_page)
    loop(next_page)

#print(link)

driver.quit()