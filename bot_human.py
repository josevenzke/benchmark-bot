from selenium import webdriver
import time

browser = webdriver.Chrome('C:/Users/José/Downloads/chromedriver_win32/chromedriver.exe')
browser.get('https://humanbenchmark.com/tests/verbal-memory')
elem = browser.find_element_by_class_name('css-de05nr')
elem.click()

seen = []

while True:
    time.sleep(0.1)
    word = browser.find_element_by_class_name('word').text
    print(word)
    if word in seen:
        browser.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[1]').click()
    else:
        browser.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[2]').click()
        seen.append(word)
    