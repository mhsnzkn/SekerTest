from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys

gen_data = pd.read_excel('Param.xlsx', sheet_name='Sayfa2')
url = gen_data["url"][0]
page = gen_data["page"][0]

browser = webdriver.Chrome()

browser.get(url)
email = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")

email.send_keys("22853489832")
password.send_keys("123ASdf.,")

login_button = browser.find_element_by_id("login")
login_button.click()

browser.execute_script("window.location.href='"+page+"'")

browser.find_element_by_id("btnYeniKayit").click()
time.sleep(3)

browser.execute_script("EkranKontrol()")
time.sleep(5)

params = pd.read_excel('Param.xlsx', sheet_name='Sayfa1')

for i in params.index:
    print(params["id"][i] , params["value"][i], sep=" ==> ")
    cmd = "$('#"+str(params["id"][i])+"').val('"+str(params["value"][i])+"')"
    print(cmd)
    browser.execute_script(cmd)


time.sleep(2)
browser.execute_script("EkranKontrol()")
time.sleep(3)
save_button = browser.find_element_by_xpath("/html/body/div[20]/div[3]/button[1]")
save_button.click()

rows = find_element_by_xpath('//tr[@role="row"]')
print(len(rows))




#time.sleep(30)





# search_bar = browser.find_element_by_xpath("//*[@id='ember29']/input")
# search_bar.send_keys("#python")
# search_bar.send_keys(Keys.RETURN)
# time.sleep(10)

# contacts = browser.find_element_by_xpath("//*[@id='mynetwork-tab-icon']")
# contacts.click()
# time.sleep(5)

# contact_button = browser.find_element_by_class_name("mn-community-summary__entity-info")
# contact_button.click()
# time.sleep(5)

# for i in range(1,3):
    # browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    # time.sleep(3)

# followers = browser.find_elements_by_class_name("mn-connection-card__details")
# fallowerList=[]

# for follower in followers:
    # fallowerList.append(follower.text)

# with open ("follower.txt","w",encoding = "UTF-8") as file:
    # for follower in fallowerList:
        # file.write(follower + "/n")
# time.sleep(5)

#browser.quit()
















