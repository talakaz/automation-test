from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

traderCode = '旺妞一號'
timePeriod = '7'  # 2=1min 3=3min, 4=5min, 5=15min, 6=30min, 7=1hr, 8=2hr, 9=3hr, 10=4hr, 11=6hr, 12=12hr
macdValue = ['3', '60', '2']
smaValue = '120'
blueUpDifValue = 2
sleepTimeDivisor = 0.05

# example option: add 'incognito' command line arg to options
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
# option.add_argument("--incognito")
# option.add_argument("--headless")
# create new instance of chrome in incognito mode
browser = webdriver.Chrome(options=option)
# go to website of interest
browser.get("https://www.bitmex.com/app/trade/XBTUSD")
# wait up to 10 seconds for page to load
timeout = 10
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
# 等待載入切換到第二層iframe
time.sleep(3)
browser.switch_to.frame(browser.find_elements_by_tag_name('iframe')[0])
browser.switch_to.frame(browser.find_elements_by_tag_name('iframe')[0])
#  打開 indicator 視窗
browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[4]').click()
time.sleep(0.2)
# 選擇 MACD 線圖
browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[2]/div[3]/div/div[42]/div/div').click()
# 關閉 indicator 視窗
browser.find_element_by_xpath('/html/body/div[3]/div[3]').click()
time.sleep(0.2)
#  打開 indicator 視窗
browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[4]').click()
time.sleep(0.2)
# 選擇 SMA 線圖
browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[2]/div[3]/div/div[47]/div/div').click()
# 打開時間區間視窗
browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div/div').click()
time.sleep(0.5)
# 選擇時間區間
browser.find_element_by_xpath('/html/body/div[3]/span[' + timePeriod + ']').click()
time.sleep(2)
# 打開 SMA 選項
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/table/tbody/tr[1]/td[2]/div/div[3]/div[4]/span').click()
time.sleep(0.2)
# 打開 SMA 設定
browser.find_element_by_xpath('//body/div[3]/table/tbody/tr/td[2]').click()
# 輸入 SMA 參數
browser.find_element_by_xpath(
    '/html/body/div[3]/div[4]/div[2]/table/tbody/tr[1]/td[2]/input').send_keys(Keys.CONTROL + "a")
browser.find_element_by_xpath(
    '/html/body/div[3]/div[4]/div[2]/table/tbody/tr[1]/td[2]/input').send_keys(smaValue)
# 關閉 SMA 設定視窗
browser.find_element_by_xpath('/html/body/div[3]/div[1]/a').click()
time.sleep(0.2)
# 打開 MACD 選項
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/table/tbody/tr[3]/td[2]/div/div[3]/div/span').click()
time.sleep(0.2)
# 打開 MACD 設定
browser.find_element_by_xpath('//body/div[3]/table/tbody/tr/td[2]').click()
# 輸入 MACD 參數
browser.find_element_by_xpath(
    '/html/body/div[3]/div[4]/div[2]/table/tbody/tr[1]/td[2]/input').send_keys(Keys.CONTROL + "a")
browser.find_element_by_xpath(
    '/html/body/div[3]/div[4]/div[2]/table/tbody/tr[1]/td[2]/input').send_keys(macdValue[0])
browser.find_element_by_xpath(
    '/html/body/div[3]/div[4]/div[2]/table/tbody/tr[2]/td[2]/input').send_keys(Keys.CONTROL + "a")
browser.find_element_by_xpath(
    '/html/body/div[3]/div[4]/div[2]/table/tbody/tr[2]/td[2]/input').send_keys(macdValue[1])
browser.find_element_by_xpath(
    '/html/body/div[3]/div[4]/div[2]/table/tbody/tr[4]/td[2]/input').send_keys(Keys.CONTROL + "a")
browser.find_element_by_xpath(
    '/html/body/div[3]/div[4]/div[2]/table/tbody/tr[4]/td[2]/input').send_keys(macdValue[2])
# 關閉 MACD 設定視窗
browser.find_element_by_xpath('/html/body/div[3]/div[1]/a').click()

realTimePeriod = ''
sleepTime = 0

if timePeriod == '2':
    realTimePeriod = '1分'
    sleepTime = 60 * sleepTimeDivisor
elif timePeriod == '3':
    realTimePeriod = '3分'
    sleepTime = 180 * sleepTimeDivisor
elif timePeriod == '4':
    realTimePeriod = '5分'
    sleepTime = 300 * sleepTimeDivisor
elif timePeriod == '5':
    realTimePeriod = '15分'
    sleepTime = 900 * sleepTimeDivisor
elif timePeriod == '6':
    realTimePeriod = '30分'
    sleepTime = 1800 * sleepTimeDivisor
elif timePeriod == '7':
    realTimePeriod = '1小時'
    sleepTime = 3600 * sleepTimeDivisor
elif timePeriod == '8':
    realTimePeriod = '2小時'
    sleepTime = 7200 * sleepTimeDivisor
elif timePeriod == '9':
    realTimePeriod = '3小時'
    sleepTime = 10800 * sleepTimeDivisor
elif timePeriod == '10':
    realTimePeriod = '4小時'
    sleepTime = 14400 * sleepTimeDivisor
elif timePeriod == '11':
    realTimePeriod = '6小時'
    sleepTime = 21600 * sleepTimeDivisor
elif timePeriod == '12':
    realTimePeriod = '12小時'
    sleepTime = 43200 * sleepTimeDivisor


def get_blue():
    blue = float(browser.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div[3]/table/tbody/tr[3]/td[2]/div/div[3]/div/div/span[2]/span').text)
    return blue


def get_red():
    red = float(browser.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div[3]/table/tbody/tr[3]/td[2]/div/div[3]/div/div/span[3]/span').text)
    return red


def get_histogram():
    signal = float(browser.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div[3]/table/tbody/tr[3]/td[2]/div/div[3]/div/div/span[1]/span').text)
    return signal


def get_sma():
    sma = float(browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/table/tbody/tr[1]/td[2]/div/div[3]/div[4]/div/span[1]/span').text)
    return sma


def get_price():
    price = float(browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/table/tbody/tr[1]/td[2]/div/div[3]/div[1]/div/span[4]/span[2]').text)
    return price


# seconds = 43200
#
# for i in range(seconds):
#     time.sleep(1)
#     try:
#         print('%d seconds | blue:%.4f | red:%.4f | signal:%.4f' % (i, get_blue(), get_red(), get_histogram()))
#         # with open(r'ScrapyCounts.txt', 'w') as fileObject:
#         #     fileObject.write('%d seconds | blue:%.4f | red:%.4f "\n"' % (i, getBlue(), getRed()))
#     except Exception as e:
#         print(e.args)
