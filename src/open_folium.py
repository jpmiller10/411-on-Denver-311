import time
from selenium import webdriver
tmpurl = 'file:/Users/Andy/Galvanize/Capstone1/Journalists-Under-Fire/maps/ImprisonedByCountry.html'
# download screenshot of map
delay = 5
browser = webdriver.Firefox()
browser.get(tmpurl)
# give the map tiles some time to load
time.sleep(delay)
browser.save_screenshot('../images/ImprisonedByCountryMap.png')
browser.quit()
file:/Users/josh/galvanize/repos/411-on-Denver-311/folium_heat.html

def