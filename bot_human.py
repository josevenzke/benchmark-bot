from selenium import webdriver

browser = webdriver.Chrome('C:/Users/José/Downloads/chromedriver_win32/chromedriver.exe')
browser.get('https://humanbenchmark.com/tests/verbal-memory')
elem = browser.find_element_by_class_name('css-de05nr')
elem.click()

