import time

class Memory:
    def __init__(self,browser):
        self.seen = []
        self.browser = browser
        self.browser.get('https://humanbenchmark.com/tests/verbal-memory')    

    def start(self):
        self.browser.find_element_by_class_name('css-de05nr').click()
    
    def play(self,times):
        for i in range(times):
            time.sleep(0.1)
            word = self.browser.find_element_by_class_name('word').text
            if word in self.seen:
                self.browser.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[1]').click()
            else:
                self.browser.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[2]').click()
                self.seen.append(word)

        