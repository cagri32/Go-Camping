import time, sys, argparse
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  

# Following piece of code is utilized to receive arguments to run the script with
parser=argparse.ArgumentParser()
parser.add_argument('--month', help='Enter the first 3 letters of the month you want to visit in eg. Jun, Aug')
parser.add_argument('--day', help='Enter the day as ordinal number eg. 1st, 5th, 23rd')
parser.add_argument('--nights', help='Enter the number of nights you want to stay eg. 1, 2, 5')
parser.add_argument('--park', help='Enter the name of the park you want to visit eg. Banff, Bruce Peninsula')
parser.add_argument('--site', help='Enter the name of the site you want to camp at eg. Two Jack Lakeside')
argms=parser.parse_args()
# pass parameters as --bar=bar-val and access them using argms.bar

#List View Version

#Default arguments passed to make sure no field is left empty
def checkByDay(month="Jun", day="26th", nights=1, park = "Banff", site = "TwoJackLakeside"):
    if (argms.month != None): month = argms.month       # Use the parameters if passed any
    if (argms.day != None): day = argms.day
    if (argms.nights != None): nights = argms.nights
    if (argms.park != None): park = argms.park
    if (argms.site != None): site = argms.site

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

waittime = 10 # in terms of seconds. Every 15 minutes
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
        

