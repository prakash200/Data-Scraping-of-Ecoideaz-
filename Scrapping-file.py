from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import json





flag_0 = 0


url = "https://www.ecoideaz.com/green-directory"


option = webdriver.ChromeOptions()
option.headless = True
chrome_prefs = {}
option.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
driver = webdriver.Chrome("/home/prakash/Downloads/chromedriver_linux64/chromedriver",chrome_options=option)




driver.get(url)
driver.maximize_window()
html = driver.page_source
soup = BeautifulSoup(html, 'lxml' )

states_0 = []
target = soup.find("div" , class_="sublocations")
li = target.find_all("li")
states = []
for i in li:
    link = i.find("a")
    states.append(link.get("href"))
    states_0.append(i.text)
driver.quit()




# Extracting URLS



# states_1 = []
# for i in range (len(states)):
#     flag = 0

#     option = webdriver.ChromeOptions()
#     chrome_prefs = {}
#     option.experimental_options["prefs"] = chrome_prefs
#     chrome_prefs["profile.default_content_settings"] = {"images": 2}
#     chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
#     driver = webdriver.Chrome("/home/prakash/Downloads/chromedriver_linux64/chromedriver",chrome_options=option)

#     driver.get(states[i])
#     driver.maximize_window()

#     while flag==0:
#         try :
#             button = driver.find_element_by_xpath('//*[@id="w2dc-controller-e466dbfc00ec2e1ee7c3f50402ef55d7"]/div/button')
#             driver.execute_script("arguments[0].scrollIntoView();",button)
#             button.click()
#             time.sleep(20)
#         except:
#             flag = flag+1
#     html = driver.page_source
#     soup = BeautifulSoup(html, 'lxml' )


#     target = soup.find("div" , class_="w2dc-listings-block-content")
#     article = target.find_all("article")
#     links = []
#     for j in article:
#         link = j.find("a")
#         links.append(link.get("href"))
#     states_1.append(links)
#     driver.quit()
    




#     print("Done")



# count=0
# for i in range (len(states_1)):
#     count=count+len(states_1[i])
#     print(i+1,"    ", len(states_1[i]))
# print("")
# print(count)

# with open('links_2.json', 'w') as fp:
#     json.dump(states_1, fp, indent=4) 

# print("\nDone.....\n")

print("")



## Extracting Data



file = open('links_1.json',)
links = json.load(file)


Data = {}
for i in range(5,10):
    time.sleep(30)
    key = states_0[i]
    print("State_"+str(i+1))
    Data[key]=[]
    for j in range(len(links[i])):
        time.sleep(1)
        print("link_"+str(j+1))
        dic = {}



        driver = webdriver.Chrome("/home/prakash/Downloads/chromedriver_linux64/chromedriver",chrome_options=option)
        driver.get(links[i][j])
        driver.maximize_window()
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml' )

        target = soup.find("div", class_ = "w2dc-content w2dc-listing-single")
        key_1 = target.find("h2").text
        dic[key_1]={}
        key_2 = target.find("span",class_ = "w2dc-field-caption").text
        key_2 =key_2.replace("\n","")
        value_1 = target.find("span",class_ = "w2dc-field-content").text
        value_1 = value_1.replace("\n","")
        value_1 = value_1.replace("\xa0","")
        dic[key_1][key_2] = value_1
        key_3 = target.find("div",class_ = "w2dc-fields-group-caption").text
        value_2 = target.find("div",class_ = "w2dc-field-content w2dc-field-description").text
        value_2 = value_2.replace("\n","")
        value_2 = value_2.replace("\xa0","")
        dic[key_1][key_3] = value_2
        target_1 = target.find_all("div",class_="w2dc-fields-group")
        try:
            target_1 = target_1[1]
            key_4 = target_1.find("div").text
            dic[key_1][key_4]={}
            div = target_1.find_all("div")
            div = div[1:]
            for k in range (len(div)):
                try:
                    key_5 = div[k].find("span",class_ = "w2dc-field-name").text
                except:
                    key_5 = " "
                if key_5 == "Email:" or key_5 == "Website:":
                    value_3 = div[k].find("span",class_ = "w2dc-field-content")
                    value_3 = value_3.find("a")
                    value_3 = value_3.get("href")
                else:
                    value_3 = div[k].find("span",class_ = "w2dc-field-content").text
                    value_3 = value_3.replace("\n","")
                    value_3 = value_3.replace("\t","")
                dic[key_1][key_4][key_5]=value_3
            key_6 = target.find("label",class_ ="w2dc-col-md-12 w2dc-control-label").text
            value_4 = target.find("div",class_ ="w2dc-radio").text
            value_4 = value_4.replace("\n","")
            value_4 = value_4.replace("\t","")
            dic[key_1][key_6]=value_4
        except:
            flag_0=flag_0+1
            print("flag" , i , j)
        Data[key].append(dic)
        driver.quit()
        
        

        
    

with open('Sustainable_DATA_2.json', 'w') as fp:
    json.dump(Data, fp, indent=4)    
    
print("\nDone\n")

print(flag_0)