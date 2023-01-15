#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import os
import time
from urllib.parse import quote_plus
import urllib.request
import urllib.parse
import re
import webbrowser as wb
import chromedriver_autoinstaller

#driverPath = r"C:\Users\SuperUser\Desktop\virtual secretary\chromedriver.exe"
driverPath = "./chromedriver.exe"
#dataPath = "whatsapp-assistant-bot-master/Data"
options = webdriver.ChromeOptions()
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver', options=options)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver', options=options)
#options.add_argument("--user-data-dir=" + dataPath)
#options.add_argument("--auto-open-console-for-tabs=" + dataPath)

#driver = webdriver.Chrome(options=options, executable_path=driverPath)
'''
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  #크롬드라이버 버전 확인

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')   
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')
'''
driver.implicitly_wait(10)

#%%
#"검색해줘"
def Search(input):
  #query_string = urllib.parse.urlencode({"search_query" : input})
  #html_content = urllib.request.urlopen("http://www.youtube.com/results?"+query_string)
  #driver.get("http://www.youtube.com/results?"+query_string)
  driver.get('http://youtube.com/results?search_query='+input)
  #wb.open_new('http://youtube.com/results?search_query='+input)
#print('Please Scan the QR Code and press enter')
#driver.find_element_by_id("gsr").send_keys(Keys.F12)
#input()
#print(query_string)

#%%
#"노래 틀어줘"

def Turn(input, n=0):
  query_string = urllib.parse.urlencode({"search_query" : input})
  html_content = urllib.request.urlopen("http://www.youtube.com/results?"+query_string)
  #Search(input)
  search_results = re.findall(r'/watch\?v=(.{11})', html_content.read().decode())
  #print(search_results)
  driver.get("http://www.youtube.com/watch?v={}".format(search_results[n]))
  
  try:
      driver.implicitly_wait(2)
      pre=driver.find_element_by_xpath("//div[@class='ytp-ad-text ytp-ad-preview-text']")
      #print(pre.text)
      
      if "광고" not in pre.text:
          time.sleep(7)
          element = driver.find_element_by_xpath("//button[@class='ytp-ad-skip-button ytp-button']")
          element.click()
      elif "광고가" in pre.text:
          time.sleep(7)
          try:
              pre=driver.find_element_by_xpath("//div[@class='ytp-ad-text ytp-ad-preview-text']")
              if "광고" not in pre.text:
                  time.sleep(7)
                  element = driver.find_element_by_xpath("//button[@class='ytp-ad-skip-button ytp-button']")
                  element.click()
              elif "광고가" in pre.text:
                  time.sleep(7)
              else:
                  time.sleep(16)
          except:
              pass
      else:
          time.sleep(16)
          try:
              pre=driver.find_element_by_xpath("//div[@class='ytp-ad-text ytp-ad-preview-text']")
              if "광고" not in pre.text:
                  time.sleep(7)
                  element = driver.find_element_by_xpath("//button[@class='ytp-ad-skip-button ytp-button']")
                  element.click()
              elif "광고가" in pre.text:
                  time.sleep(7)
              else:
                  time.sleep(16)
          except:
              pass
    
  #except Exception as e:
  except:
      #print("HELLO", e)
      pass
  #wb.open_new("http://www.youtube.com/watch?v={}".format(search_results[0]))
#"두번째 노래 틀어줘"
#driver.quit()
driver.get("http://www.youtube.com/")

#%%
#검색 그리고 영상 틀기
def Search_and_Turn(n=0):
  if re.search('query', driver.current_url):
    elements=driver.find_elements_by_id("thumbnail")
    list=[]
    for element in elements:
      a=element.get_attribute('href')
      list.append(a)
  driver.get(list[n+1])
  try:
      driver.implicitly_wait(2)
      pre=driver.find_element_by_xpath("//div[@class='ytp-ad-text ytp-ad-preview-text']")
      #print(pre.text)
      
      if "광고" not in pre.text:
          time.sleep(7)
          element = driver.find_element_by_xpath("//button[@class='ytp-ad-skip-button ytp-button']")
          element.click()
      elif "광고가" in pre.text:
          time.sleep(7)
          try:
              pre=driver.find_element_by_xpath("//div[@class='ytp-ad-text ytp-ad-preview-text']")
              if "광고" not in pre.text:
                  time.sleep(7)
                  element = driver.find_element_by_xpath("//button[@class='ytp-ad-skip-button ytp-button']")
                  element.click()
              elif "광고가" in pre.text:
                  time.sleep(7)
              else:
                  time.sleep(16)
          except:
              pass
      else:
          time.sleep(16)
          try:
              pre=driver.find_element_by_xpath("//div[@class='ytp-ad-text ytp-ad-preview-text']")
              if "광고" not in pre.text:
                  time.sleep(7)
                  element = driver.find_element_by_xpath("//button[@class='ytp-ad-skip-button ytp-button']")
                  element.click()
              elif "광고가" in pre.text:
                  time.sleep(7)
              else:
                  time.sleep(16)
          except:
              pass
    
  #except Exception as e:
  except:
      #print("HELLO", e)
      pass
  
#%%
# 광고 SKIP
def SKIP():
    try:
      driver.implicitly_wait(2)
      pre=driver.find_element_by_xpath("//div[@class='ytp-ad-text ytp-ad-preview-text']")
      #print(pre.text)
      
      if "광고" not in pre.text:
          time.sleep(7)
          element = driver.find_element_by_xpath("//button[@class='ytp-ad-skip-button ytp-button']")
          element.click()
      elif "광고가" in pre.text:
          time.sleep(7)
          try:
              pre=driver.find_element_by_xpath("//div[@class='ytp-ad-text ytp-ad-preview-text']")
              if "광고" not in pre.text:
                  time.sleep(7)
                  element = driver.find_element_by_xpath("//button[@class='ytp-ad-skip-button ytp-button']")
                  element.click()
              elif "광고가" in pre.text:
                  time.sleep(7)
              else:
                  time.sleep(16)
          except:
              pass
      else:
          time.sleep(16)
          try:
              pre=driver.find_element_by_xpath("//div[@class='ytp-ad-text ytp-ad-preview-text']")
              if "광고" not in pre.text:
                  time.sleep(7)
                  element = driver.find_element_by_xpath("//button[@class='ytp-ad-skip-button ytp-button']")
                  element.click()
              elif "광고가" in pre.text:
                  time.sleep(7)
              else:
                  time.sleep(16)
          except:
              pass
    except:
      #print("HELLO", e)
      pass