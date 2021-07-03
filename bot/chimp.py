import time

class Chimp:
    def __init__(self,browser):
        self.browser = browser
        self.browser.get('https://humanbenchmark.com/tests/chimp')
    
    def start(self):
        x = self.browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div[2]/button').click()
    
    def play(self,times):
        for d in range(times):
            x = self.browser.find_elements_by_class_name('css-19b5rdt')
            serie = []
            for i in x:
                serie.append([int(i.text),i])
            serie.sort()
            print(serie)
            for i in serie:
                time.sleep(0.1)
                i[1].click()
            print('a')
            self.browser.find_element_by_class_name('css-de05nr').click()
            time.sleep(0.3)
            