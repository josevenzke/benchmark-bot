from selenium import webdriver
from memory import Memory
from reaction import Reaction
from aim import Aim
from chimp import Chimp
import local

class Benchmark:
    def __init__(self):
        self.browser = webdriver.Chrome(local.WINDOWS_PATH)
    
    def memory(self,times):
        x = Memory(self.browser)
        x.start()
        x.play(times)
    
    def reaction(self):
        x = Reaction(self.browser)
        x.play()
    
    def aim(self):
        x = Aim(self.browser)
        x.start()
    
    def chimp(self,times):
        x = Chimp(self.browser)
        x.start()
        x.play(times)
