import time

class Aim:
    def __init__(self,browser):
        self.browser = browser
        self.browser.get('https://humanbenchmark.com/tests/aim')

    def start(self):
        time.sleep(1)
        x = self.browser.find_element_by_class_name('css-ad1j3y')
        self.browser.execute_script("arguments[0].click();", x)