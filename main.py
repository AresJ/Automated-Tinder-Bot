import pyautogui
import time
from Selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://tinder.com/app/recs")
swipeButton = driver.find_elements_by_xpath("//button[class='Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style Bxsh($bxsh-btn) Expand Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgc($c-like-green):a']")
a = 0
while a < 10:
  pyautogui.click(swipeButton)
  time.sleep(0.2)
  a += 1
