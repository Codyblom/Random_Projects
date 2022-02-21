import webbrowser
import time
import random

while True:
    sites = random.choice([pornhub.com, brazzers.com])
    visit = "http://[]".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(1, 2)
    time.sleep(seconds)
