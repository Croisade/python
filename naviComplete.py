from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import xlrd
import sys
import os

if len(sys.argv) < 2:
    print ("\nUsage: " + sys.argv[0] + " <NewAccount> <Mirror>\n")
    sys.exit()

options = Options()
options.add_argument("--headless") 
options.add_argument('--disable-gpu')   
driver = webdriver.Chrome(executable_path = r'')
username = sys.argv[1]



#SETS THE INITIAL GROUP FOR USER
driver.get("")
nav1 = driver.find_element_by_id("MenuList_HyperLink1_11")
nav1.click()

elem = driver.find_element_by_id("__USERID__")
elem.send_keys('foobar\\' + sys.argv[1])

elem = driver.find_element_by_id("__GROUPID__")
elem.send_keys('foobar-Intranet')

elem2 = driver.find_element_by_id("__USERNAME__")
elem2.send_keys('foobar\\' + sys.argv[1])

time.sleep(1)
elem = driver.find_element_by_id("__ADD__").click()

elem2.send_keys(Keys.RETURN)


time.sleep(1)

#COPIES NDC GROUPS FROM LIKE USER
driver.get("")

elem = driver.find_element_by_id("__LOGIN__")
elem.send_keys('foobar\\' + sys.argv[1])

elem2 = driver.find_element_by_id("__OPTION__")
elem2.send_keys('foobar\\' + sys.argv[2])


elem = driver.find_element_by_id("__LIKELOGIN__").click()

time.sleep(1)

elem2.send_keys(Keys.RETURN)

time.sleep(1)

#DOWNLOADS SPREADSHEET
driver.get("")

elem = driver.find_element_by_id("__USERID__")
elem.send_keys('foobar\\' + sys.argv[2])
elem.send_keys(Keys.RETURN)

elem = driver.find_element_by_id("foobar").click()
time.sleep(1)


#WORKSHEET FOR NON NDC GROUPS
driver.get("")

nfi = xlrd.open_workbook(r"")
worksheet = nfi.sheet_by_index(0)

for i in range(worksheet.nrows):
    c0 = [worksheet.row_values(i)[1] for i in range(worksheet.nrows) if worksheet.row_values(i)[1]]

postal = [s for s in c0 if "NDC" not in s]
postal.pop(0)
length = len(postal)
print(length)
i = 0
while i < length:
    elem = driver.find_element_by_id("__USERID__")
    elem.send_keys('foobar\\' + sys.argv[1])

    elem = driver.find_element_by_id("__GROUPID__")
    elem.send_keys(str(postal[i]))

    elem2 = driver.find_element_by_id("__USERNAME__")
    elem2.send_keys('foobar\\' + sys.argv[1])

    time.sleep(2)
    elem = driver.find_element_by_id("__ADD__").click()

    elem2.send_keys(Keys.RETURN)

    i += 1

    time.sleep(1)

    

    driver.find_element_by_id('__USERID__').clear()
    driver.find_element_by_id('__GROUPID__').clear()
    driver.find_element_by_id('__USERNAME__').clear()
    driver.find_element_by_id("__ADD__").click()

    time.sleep(1)


driver.close()
if os.path.exists(r''):
    os.remove(r'')
else:
  print("The file does not exist") 



