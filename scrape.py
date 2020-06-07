from pyvirtualdisplay import Display
import pandas as pd
import os
import sys
import glob
import time
import requests
import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


#url = "https://google.com"
url = "https://www.yayoiken.com/menu_list/"

def main():
    driver.get(url)
    
    #try:
    #    elems = driver.find_elements_by_css_selector('h3')
    #except:
    #    print("NOT FOUND")
    #for elem in elems:
        #print(elem.text)
    
    #elems[-1].location_once_scrolled_into_view
    #driver.save_screenshot('abc.png')
    
    js_script = r'''function getElemInfo(){
      var elemInfo = []
      var allElems = $('body *:visible');
      for(var i=0;i<allElems.length;i++){
        var infoJson = {};
        var elem = allElems[i];
        // Get parents
        var parents = $(elem).parents().map(function(){
        	return this.tagName;
        }).get();
        var properties = [...elem.attributes].map((x)=>[[x.name],[x.value]]);
        // Get text not surrounded by tags
        if(elem.innerHTML.length==0)
          continue;
        var parsed = $.parseHTML(elem.innerHTML);
        var extractedText = "";
        for(var j=0;j<parsed.length;j++){
          if(parsed[j].nodeName == '#text'){
            var processedText = parsed[j].textContent.trim();
            extractedText += processedText;
          }else if(parsed[j].nodeName == 'BR'){
            extractedText += '\n';
          }
        }
        if(extractedText.length != 0){
          infoJson['text'] = extractedText;
          infoJson['tag'] = elem.tagName;
          infoJson['parents'] = parents;
          infoJson['properties'] = properties;
          elemInfo.push(infoJson);
        }
      }
      return elemInfo;
    }
    
    
    return JSON.stringify(getElemInfo());
    '''
    
    returned = driver.execute_script(js_script)
    with open('page_elements.json','w',encoding='utf-8') as f:
        f.write(returned)

try:
    print("Initializing...")
    display = Display(visible=0, size=(1280, 720))
    display.start()
    
    firefox_profile = FirefoxProfile()
    driver = webdriver.Firefox(firefox_profile)
    driver.set_page_load_timeout(90)
    driver.implicitly_wait(30)
    print("Initialization completed")

    # Load jQuery
    with open('jquery.min.js') as f:
        driver.execute_script(f.read())
    main()
finally:
    print("Running Garbage Collection")
    driver.quit()
    display.stop()
