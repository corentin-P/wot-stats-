from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import tkinter as tk
from datetime import date
from tkinter import ttk
import matplotlib.pyplot as plt

def research():
    link = 'https://fr.wot-life.com'
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.set_window_size(1600, 1200)
    driver.get(link)
    driver.find_element_by_xpath(
        "//div[@class='cmp_ui cmp_ext_text cmp_state-stacks']/div[@class ='cmp_navi']/div/div[@class='cmp_mainButtons']/div/div/div[@class = 'cmp_button cmp_button_bg cmp_button_font_color']").click()
    driver.find_element_by_id('searchbox').send_keys(name.get() + Keys.ENTER)
    driver.execute_script("window.scrollTo(0, window.scrollY + 400)")
    driver.find_element_by_xpath("//div[@class = 'slider']/h2").click()
    driver.execute_script("window.scrollTo(0, window.scrollY + 2500)")

    time.sleep(0.5)

    liste_tanks = []
    liste_tanks2 = []

    G_stats = driver.find_elements_by_tag_name("tr")
    for i in range(5):
        print(G_stats[i].text)

    tanks = driver.find_elements_by_xpath(
        "//div[@class='slider active']/div[@class='content']/div[@id = 'tanks_wrapper']/table[@id='tanks']/tbody/tr/td")

    for i in range(len(tanks)):
        if tanks[i].text != "":
            liste_tanks.append(tanks[i].text)

    driver.close()

    for i in range(5, len(liste_tanks), 5):
        liste_tanks2.append(
            liste_tanks[i] + ";" + liste_tanks[i + 1] + ";" + liste_tanks[i + 2] + ";" + liste_tanks[i + 3] + ";" +
            liste_tanks[i + 4]+ ";"+ str(date.today()))

    with open("tanks_stats.csv", 'r+', newline='') as fichier_csv:
        reader = csv.reader(fichier_csv, delimiter=";")
        # fichier_csv.write(liste_tanks2[1])
        for row in reader:
            print(row)
        fichier_csv.write("\n")
        for i in range(len(liste_tanks2)):
            fichier_csv.write(str(liste_tanks2[i]) + "\n")

def graph():
    WN8= []
    date = []
    for i in range(len(tanks)):
        if tanks[i]["tank name"] == liste.get():
            WN8.append(tanks[i]["WN8"])
            date.append(tanks[i]["date"])
    plt.title(liste.get())
    plt.plot(date, WN8)
    plt.xlabel('date')
    plt.ylabel('WN8')
    plt.show()

mainapp = tk.Tk()
mainapp.geometry("300x300")
label = tk.Label(mainapp, text = 'Quel joueur voulez vous suivre?')
label2 = tk.Label(mainapp, text = 'Stats for a specific tank? ')
name = tk.Entry(mainapp, width = 50)
valid = tk.Button(mainapp, text = 'Upload new data', command = research)
specific_tank_btn = tk.Button(mainapp, text = 'Specific stats for a tank?', command = graph)

tanks = []
tanks_name = []

with open ('tanks_stats.csv') as fichier_csv:
    dict_csv = list(csv.DictReader(fichier_csv, delimiter=';'))
    for ligne in dict_csv:
        tanks.append(dict(ligne))

for i in range(len(tanks)):
    if tanks[i]["tank name"] not in tanks_name:
        tanks_name.append(tanks[i]["tank name"])

liste = ttk.Combobox(mainapp, values = tanks_name)
liste['state']='readonly'




label.grid(column = 1, row = 1)
name.grid(column = 1, row = 2)
valid.grid(column = 1, row=3)
label2.grid(column = 1, row = 4)
liste.grid(column = 1, row = 5)
specific_tank_btn.grid(column = 1, row = 6)

mainapp.mainloop()