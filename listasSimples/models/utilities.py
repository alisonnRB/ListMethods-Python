import os
import time

class Utilities:
    def clean(self, seconds=0):
        time.sleep(seconds)
        if os.name == 'nt':
            os.system('cls')
        else: 
            os.system('clear')