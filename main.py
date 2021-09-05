from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

link = 'https://fr.wot-life.com'
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.set_window_size(1600,1200)
driver.get(link)

driver.find_element_by_xpath("//div[@class='cmp_ui cmp_ext_text cmp_state-stacks']/div[@class ='cmp_navi']/div/div[@class='cmp_mainButtons']/div/div/div[@class = 'cmp_button cmp_button_bg cmp_button_font_color']").click()
name = 'clashcoco'#str(input("quel joueur voulez vous suivre? "))
driver.find_element_by_id('searchbox').send_keys(name + Keys.ENTER)


"""stats_generals = driver.find_elements_by_id('tab1')

for i in range(len('tab1')):
    print(stats_generals[i].text)"""
driver.execute_script("window.scrollTo(0, window.scrollY + 400)")

driver.find_element_by_xpath("//div[@class = 'slider']/h2").click()
driver.execute_script("window.scrollTo(0, window.scrollY + 2500)")

time.sleep(0.5)

tanks = driver.find_elements_by_tag_name("tr")
#tanks = driver.find_elements_by_class_name("content")
for i in range(len('tanks')):
    print(tanks[i].text)
