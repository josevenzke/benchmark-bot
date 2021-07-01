import time

class Reaction:
    def __init__(self,browser):
        self.browser = browser
        self.browser.get('https://humanbenchmark.com/tests/reactiontime')
    
    def play(self):
        screen = self.browser.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]')
        count = 0
        screen.click()
        while count<5:
            
            if screen.value_of_css_property("background-color") != 'rgba(206, 38, 54, 1)':
                screen.click()
                time.sleep(1)
                screen.click()
                count+=1
