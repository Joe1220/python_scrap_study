from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
# 1이 허용, #2가 금지인 거 같음
prefs = {"profile.default_content_setting_values.notifications": 1}
chrome_options.add_experimental_option("prefs", prefs)

path = "D:\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(path, options=chrome_options)

email = 'rpehdrnfm3@naver.com'
pwd = 'whtmdgus1220!'

driver.get('https://www.facebook.com/')
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(email)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
time.sleep(5)

a = driver.find_elements_by_xpath(
    '//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a')
driver.get(a[0].get_attribute('href'))

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

information_list = soup.select(
    "#mount_0_0 > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div > div > div > div.d2edcug0.cbu4d94t.j83agx80.bp9cbjyn > div.rq0escxv.d2edcug0.ecyo15nh.hv4rvrfc.dati1w0a.tr9rh885 > div > div.rq0escxv.l9j0dhe7.du4w35lb.d2edcug0.o387gat7.buofh1pr.g5gj957u.hpfvmrgz.aov4n071.oi9244e8.bi6gxh9e.h676nmdw.aghb5jc5.rek2kq2y > div > div > div > div:nth-child(1) > div > div > div > div.sej5wr8e > div:nth-child(1) > div > ul > div > div.rq0escxv.l9j0dhe7.du4w35lb.d2edcug0.rj1gh0hx.buofh1pr.g5gj957u.hpfvmrgz.o8rfisnq.p8fzw8mz.pcp91wgn.iuny7tx3.ipjc6fyt > div > div > span")
for information in information_list:
    print(information.text)
