import time, sys
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  

#List View Version

def checkByDay(month="Jun", day="26th", nights=1):
    if(len(sys.argv)==2):   #First Argument is day eg. 26th
        day = sys.argv[1]
    elif(len(sys.argv)==3): #Second Argument is month eg. Jun
        month = sys.argv[2]
    elif(len(sys.argv)==4): #Third Argument is nights eg. 3
        nights = sys.argv[3]

    park = "Banff"
    site = "TwoJackLakeside"
    global driver, availability
    availability = False
    driver = webdriver.Chrome('./chromedriver')
    #Search Two Jack Lakeside
    driver.get("https://reservation.pc.gc.ca/%s/%s?Calendar" %(park, site))

    #Enter Month, Day and Number of Nights to Stay
    driver.find_element_by_xpath("//select[@name='selArrMth']/option[text()='%s']" %month).click()
    driver.find_element_by_xpath("//select[@name='selArrDay']/option[text()='%s']" %day).click()
    driver.find_element_by_xpath("//select[@name='selNumNights']/option[text()='%s']" %nights).click()

    #Go to List View
    driver.find_element_by_id("MainContentPlaceHolder_ListLink").click()

    #Enter Tent as Equipment and 4 as group size
    driver.find_element_by_xpath("//select[@id='selPartySize']/option[text()='4']").click()
    driver.find_element_by_id("selEquipmentSub").click()
    driver.find_element_by_xpath("//option[@value='LargeTent']").click() 

    #Visual Adjustments to the tab
    driver.execute_script("document.body.style.zoom='80%'")
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    driver.execute_script("window.scrollTo(0, 200)") 

    #Check the list and print if there is an available spot. If there is no availability, tag won't be found
    try:
        availability = driver.find_element_by_xpath('//td/img[@alt="Available"]')
        #print (availability.tag_name)   #for debugging
        parent = availability.find_element_by_xpath('./../..')
        spot = parent.find_elements_by_tag_name("td")[1]
        #print (parent.tag_name)        #for debugging
        print("\nAvailability at " + spot.text)
        checkAllCalendar()
        availability = True
    except NoSuchElementException:
        print("No Availability")
        #checkByDay(month="Jun", day="26th", nights=1)
    

def checkAllCalendar():
    #New Tab for Searching all Campsite
    
    driver.execute_script("window.open('about:blank', 'tab3');")
    driver.switch_to.window("tab3")
    driver.get("https://reservation.pc.gc.ca/Banff?Calendar")
    #All entries are taken from previous tab automatically
    driver.find_element_by_id("selEquipmentSub").click()
    driver.find_element_by_xpath("//option[@value='LargeTent']").click() 

    #Visual Adjustments to the tab
    driver.execute_script("document.body.style.zoom='80%'")
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    driver.execute_script("window.scrollTo(0, 200)") 
    return driver

waittime = 900 # in terms of seconds. Every 15 minutes
while True:
    a = datetime.now().second
    if (a % waittime) == 0: 
        checkByDay()        # Do the task
        if availability:
            break           # if an availability found, stop the code
        sleep(5)            # wait 5 seconds before closing the browser
        driver.quit()
        while True:         # discard any milliseconds or duplicated 15 minutes
            a = datetime.now().second
            if (a % waittime) != 0:
                break
        

