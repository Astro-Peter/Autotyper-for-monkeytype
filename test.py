from selenium import webdriver
import pyautogui
import time

# opens monkeytype in firefox and gives some time to accept cookies
browser=webdriver.Firefox()
browser.get("http://monkeytype.com")
time.sleep(2)


time_start = time.time()
html = browser.page_source
words = html.split("<letter>")[1:]
need_to_type = [' ']
while time.time() - time_start:
    for i in words:
        need_to_type.append(i[0])
        if len(i) > 10:
            need_to_type.append(' ')
    print(''.join(need_to_type))
    pyautogui.typewrite(need_to_type, interval=0.001)
    print('\n')
    html = browser.page_source
    words = html.split("<letter>")[1:]
    need_to_type = [' ']

time.sleep(10)
browser.close()
