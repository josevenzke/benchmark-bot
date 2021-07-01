from selenium import webdriver
from memory import Memory
from reaction import Reaction

class Benchmark:
    def __init__(self):
        self.browser = webdriver.Chrome('/home/desjrv/Downloads/chromedriver_linux64/chromedriver')
    
    def memory(self,times):
        x = Memory(self.browser)
        x.start()
        x.play(times)
    
    def reaction(self):
        x = Reaction(self.browser)
        x.play()