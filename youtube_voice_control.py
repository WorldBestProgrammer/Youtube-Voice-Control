# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 11:43:45 2022

@author: SuperUser
"""

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import speech_recognition as sr
import os
import sys
import time
import winsound
from pathlib import Path
from pprint import pprint
import re
from six.moves import queue
from temp import Turn, Search, Search_and_Turn, SKIP
from temp import driver
from selenium import webdriver
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
import os
import sounddevice as sd


n=50
SAMPLING_RATE = 22050

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


# obtain audio from the microphone
r = sr.Recognizer()
r.dynamic_energy_threshold = True
r.dynamic_energy_adjustment_ratio = 4
#r.energy_threshold = 100000000000
r.pause_threshold = 0.5

# recognize speech using Sphinx
def main():
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, phrase_time_limit=2)
        transcript=r.recognize_google(audio, language='ko-KR')
    try:
        print(r.recognize_google(audio, language='ko-KR'))
    except:
        pass
    if driver.current_url[24:29] == 'watch':
        actionChains = ActionChains(driver)
        element = driver.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
        element2 = driver.find_element_by_class_name("ytp-chrome-controls")

    if re.search(r"\b(시리야)\b", transcript, re.I):
        pause=1
        sys.stdout.write("네\n")
        winsound.PlaySound('./네.', winsound.SND_FILENAME)
        if driver.current_url[24:29] == 'watch':
            element = driver.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
            if element.get_attribute('title') != '재생(k)':
                element.click()
        switch = 3
        v=0
        while v == 0:
            v=main4()

                
            '''while (b-a < 10):
                main3()
                b=get_current_times()
                print(b)
                continue'''
                    
    if re.search(r"\b(다음 영상)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./알겠습니다!', winsound.SND_FILENAME)
        if driver.current_url[24:29] == 'watch':
            element = driver.find_element_by_xpath("//a[@class='ytp-next-button ytp-button']")
            element.click()
            SKIP()
            
    if re.search(r"\b(다음 노래)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./알겠습니다!', winsound.SND_FILENAME)
        if driver.current_url[24:29] == 'watch':
            element = driver.find_element_by_xpath("//a[@class='ytp-next-button ytp-button']")
            element.click()
            SKIP()
            
    if re.search(r"\b(재생)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound(r'./알겠습니다!', winsound.SND_FILENAME)
        if driver.current_url[24:29] == 'watch':
            element = driver.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
            if element.get_attribute('title') != '일시정지(k)':
                element.click()
    if re.search(r"\b(정지)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./정지했습니다.', winsound.SND_FILENAME)
        if driver.current_url[24:29] == 'watch':
            element = driver.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
            if element.get_attribute('title') != '재생(k)':
                element.click()
    if re.search(r"\b(멈춰 줘)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./정지했습니다.', winsound.SND_FILENAME)
        if driver.current_url[24:29] == 'watch':
            element = driver.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
            if element.get_attribute('title') != '재생(k)':
                element.click()
            
    if re.search(r"\b(많이 올려 줘|많이 키워 줘)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./네 소리를 올리겠습니다!', winsound.SND_FILENAME)                
        actionChains.move_to_element(element2).click().send_keys(Keys.ARROW_UP+Keys.ARROW_UP+Keys.ARROW_UP+Keys.ARROW_UP+Keys.ARROW_UP).perform()
        #currentVolumeDb = volume.GetMasterVolumeLevel()
        #volume.SetMasterVolumeLevel(currentVolumeDb + 10.0, None)
        

    if re.search(r"\b(소리 올려 줘|소리 키워 줘|볼륨 올려 줘)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./네 소리를 올리겠습니다!', winsound.SND_FILENAME)                
        actionChains.move_to_element(element2).click().send_keys(Keys.ARROW_UP+Keys.ARROW_UP+Keys.ARROW_UP).perform()
        #currentVolumeDb = volume.GetMasterVolumeLevel()
        #volume.SetMasterVolumeLevel(currentVolumeDb + 5.0, None)
        

    if re.search(r"\b(조금 올려 줘|좀만 올려 줘|조금만 올려 줘)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./네 소리를 올리겠습니다!', winsound.SND_FILENAME)                                
        actionChains.move_to_element(element2).click().send_keys(Keys.ARROW_UP+Keys.ARROW_UP).perform()
        #currentVolumeDb = volume.GetMasterVolumeLevel()
        #volume.SetMasterVolumeLevel(currentVolumeDb + 3.0, None)
        
            
            
    if re.search(r"\b(많이 내려 줘|많이 내려)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./네 소리를 내리겠습니다!', winsound.SND_FILENAME)                                
        actionChains.move_to_element(element2).click().send_keys(Keys.ARROW_DOWN+Keys.ARROW_DOWN+Keys.ARROW_DOWN+Keys.ARROW_DOWN+Keys.ARROW_DOWN).perform()
        #currentVolumeDb = volume.GetMasterVolumeLevel()
        #volume.SetMasterVolumeLevel(currentVolumeDb - 10.0, None)
        

    if re.search(r"\b(소리 내려 줘|볼륨 내려 줘|소리 낮춰 줘)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")           
        winsound.PlaySound('./네 소리를 내리겠습니다!', winsound.SND_FILENAME)
        actionChains.move_to_element(element2).click().send_keys(Keys.ARROW_DOWN+Keys.ARROW_DOWN+Keys.ARROW_DOWN).perform()
        #currentVolumeDb = volume.GetMasterVolumeLevel()
        #volume.SetMasterVolumeLevel(currentVolumeDb - 5.0, None)
        

    if re.search(r"\b(조금 내려 줘|좀만 낮춰 줘|조금만 낮춰 줘|조금만 내려 줘|좀만 내려 줘|조금 낮춰 줘)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./네 소리를 내리겠습니다!', winsound.SND_FILENAME)                
        actionChains.move_to_element(element2).click().send_keys(Keys.ARROW_DOWN+Keys.ARROW_DOWN).perform()
        #currentVolumeDb = volume.GetMasterVolumeLevel()
        #volume.SetMasterVolumeLevel(currentVolumeDb - 3.0, None)
     
    if re.search(r"\b(전체 화면|화면)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./알겠습니다!', winsound.SND_FILENAME)                
        actionChains.move_to_element(element2).click().send_keys('f').perform()
        
    if re.findall("검색|찾아 줘", transcript, re.I):
        keyword=re.findall("검색|찾아", transcript, re.I)
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        b=transcript.split(keyword[0])
        input2=b[0]
        Search(input2)
        winsound.PlaySound('./알겠습니다!', winsound.SND_FILENAME)
        
        v=0
        while v == 0:
            v=main5(input2)


def main4():
    with sr.Microphone() as source:
        print("무엇을 도와드릴까요?")
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=6)
        transcript=r.recognize_google(audio, language='ko-KR')
        print(transcript)
     
    
    if driver.current_url[24:29] == 'watch':
        element = driver.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
        actionChains = ActionChains(driver)
    if re.search(r"\b(들려 줘)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        a=transcript.split('들려 줘')
        input=a[0]
        winsound.PlaySound('./알겠습니다!', winsound.SND_FILENAME)
        time.sleep(1)                
        Turn(input)
    elif re.search(r"\b(틀어 줘)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        a=transcript.split('틀어 줘')
        input=a[0]
        winsound.PlaySound('./알겠습니다!', winsound.SND_FILENAME)
        time.sleep(1)
        Turn(input)
                
    elif re.search(r"\b(다음 영상)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./알겠습니다!', winsound.SND_FILENAME)
        if driver.current_url[24:29] == 'watch':
            element = driver.find_element_by_xpath("//a[@class='ytp-next-button ytp-button']")
            element.click()
            SKIP()
    elif re.search(r"\b(다음 노래)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./알겠습니다!', winsound.SND_FILENAME)
        if driver.current_url[24:29] == 'watch':
            element = driver.find_element_by_xpath("//a[@class='ytp-next-button ytp-button']")
            element.click()
            SKIP()

    elif re.search(r"\b(정지)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./알겠습니다!', winsound.SND_FILENAME)
        if driver.current_url[24:29] == 'watch':
            element = driver.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
            if element.get_attribute('title') != '재생(k)':
                element.click()
    elif re.search(r"\b(멈춰 줘)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./알겠습니다!', winsound.SND_FILENAME)
        if driver.current_url[24:29] == 'watch':
            element = driver.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
            if element.get_attribute('title') != '재생(k)':
                element.click()
    elif re.search(r"\b(재생)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./알겠습니다!', winsound.SND_FILENAME)
        if driver.current_url[24:29] == 'watch':
            element = driver.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
            if element.get_attribute('title') != '일시정지(k)':
                element.click()
                
    elif re.search(r"\b(많이 올려 줘|많이 키워 줘)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./네 소리를 올리겠습니다!', winsound.SND_FILENAME)               
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb + 10.0, None)
        pause=0

    elif re.search(r"\b(소리 올려 줘|소리 키워 줘|볼륨 올려 줘)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./네 소리를 올리겠습니다!', winsound.SND_FILENAME)               
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb + 5.0, None)
        pause=0

    elif re.search(r"\b(조금 올려 줘|좀만 올려 줘|조금만 올려 줘)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./네 소리를 올리겠습니다!', winsound.SND_FILENAME)                               
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb + 3.0, None)
        pause=0
              
            
    elif re.search(r"\b(많이 내려 줘)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./네 소리를 내리겠습니다!', winsound.SND_FILENAME)                                
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb - 10.0, None)
        pause=0

    elif re.search(r"\b(소리 내려 줘|볼륨 내려 줘)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")           
        winsound.PlaySound('./네 소리를 내리겠습니다!', winsound.SND_FILENAME) 
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb - 5.0, None)
        pause=0

    elif re.search(r"\b(조금 내려 줘|좀만 낮춰 줘|조금만 낮춰 줘|조금만 내려 줘|좀만 내려 줘|조금 낮춰 줘)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./네 소리를 내리겠습니다!', winsound.SND_FILENAME)                
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb - 3.0, None)
        pause=0

                
    elif re.findall("검색|찾아 줘", transcript, re.I):
        keyword=re.findall("검색|찾아 줘", transcript, re.I)
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        b=transcript.split(keyword[0])
        input2=b[0]
        Search(input2)
        winsound.PlaySound('./알겠습니다!', winsound.SND_FILENAME)
        #main5(input2, html_content=html_content)
        v=0
        while v == 0:
            v=main5(input2)
    
    elif transcript == 'None':
        return 0
        
    else:
        if driver.current_url[24:29] == 'watch':
            element = driver.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
            if element.get_attribute('title') != '일시정지(k)':
                element.click()
            return 5
        else:
            return 5
    
    return 5

def main5(input2):
    with sr.Microphone() as source:
        print("어느 영상을 틀어드릴까요?")
        time.sleep(1)
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=5)
        transcript=r.recognize_google(audio, language='ko-KR')        
    #try:
        print(r.recognize_google(audio, language='ko-KR'))
    #except:
    #    pass   
    
    if driver.current_url[24:29] == 'watch':
        element = driver.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
    if re.search(r"\b(첫 번째 영상|첫 번째 노래)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./알겠습니다!', winsound.SND_FILENAME)
        Search_and_Turn()
    elif re.search("두", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./알겠습니다!', winsound.SND_FILENAME)
        Search_and_Turn(1)
    elif re.search("세", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./알겠습니다!', winsound.SND_FILENAME)
        Search_and_Turn(2)
    elif re.search(r"\b(네 번째 영상|네 번째 노래)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./알겠습니다!', winsound.SND_FILENAME)
        Search_and_Turn(3)
    elif re.search(r"\b(다섯 번째 영상|다섯 번째 노래)\b", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./알겠습니다!', winsound.SND_FILENAME)
        Search_and_Turn(4)
    elif re.search("다시|나가", transcript, re.I):
        time.sleep(0.5)
        sys.stdout.write("알겠습니다~\n")
        winsound.PlaySound('./알겠습니다!', winsound.SND_FILENAME)
        main4()
    elif transcript == 'None':
        return 0
    else:
        return 0
    return 5   
        
while True:
    try:
        time.sleep(1)
        main()
    except:
        pass