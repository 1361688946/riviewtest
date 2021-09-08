from selenium import  webdriver

browser =webdriver.Chrome()
url='http://www.baidu.com'
browser.get(url)
browser.maximize_window()
print(browser.title)
browser.close()