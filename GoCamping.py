from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
#Search Two Jack Lakeside
driver.get("https://reservation.pc.gc.ca/Banff/TwoJackLakeside?Calendar")

#Enter Month, Day and Number of Nights to Stay
driver.find_element_by_xpath("//select[@name='selArrMth']/option[text()='Jun']").click()
driver.find_element_by_xpath("//select[@name='selArrDay']/option[text()='26th']").click()
driver.find_element_by_xpath("//select[@name='selNumNights']/option[text()='4']").click()

#Go to Calendar View
driver.find_element_by_id("MainContentPlaceHolder_CalendarLink").click()

#Enter Tent as Equipment and 4 as group size
driver.find_element_by_xpath("//select[@id='selPartySize']/option[text()='4']").click()
driver.find_element_by_id("selEquipmentSub").click()
driver.find_element_by_xpath("//option[@value='LargeTent']").click() 

#Visual Adjustments to the tab
driver.execute_script("document.body.style.zoom='80%'")
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
driver.execute_script("window.scrollTo(0, 200)") 

#Check the calendar and print if there is an available spot
if (driver.find_element_by_class_name("avail")):
    availability = driver.find_element_by_class_name("avail")
    parent = availability.find_element_by_xpath('..')
    print("\nAvailability at " + parent.text)
else:
    print("\nNot Available")

#Also check the whole site for other openings
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