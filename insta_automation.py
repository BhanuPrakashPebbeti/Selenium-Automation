from time import sleep,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

username = input("Enter email id  :")
password = input("enter password  :")

try:
    print("Trying to connect to instagram")
    driver = webdriver.Chrome(r"E:\My projects\Selenium automation\chromedriver") #give path of the chromedriver in your pc
    driver.get("https://www.instagram.com/?hl=en")

except:
    print('Error in establishing instagram connection')
    print('Connection was closed')

def login_func():
    #input("press any key to continue")
    user = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')))
    user.send_keys(username)
    pwd = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div[1]/div[2]/div/label/input')))
    pwd.send_keys(password)
    pwd.send_keys(Keys.RETURN)
    logininfo_button = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
    logininfo_button.click()

    notification = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/div[3]/button[2]')))
    notification.click()

def logout_func():
    profile_photo = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img')))
    profile_photo.click()
    logout = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div')))
    logout.click()

def profile_func():
    profilephoto = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img')))
    profilephoto.click()
    profile = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div')))
    profile.click()

def scrape_following():
    num_following = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span')))
    print("following no :",int(num_following.text))
    following = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')))
    following.click()
    sleep(10)
    fBody1 = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,"//div[@class='isgrP']")))
    while True:
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].scrollHeight;', fBody1)
        sleep(0.75)
        k = driver.find_elements_by_xpath("//div[@class='isgrP']//li")
        print(len(k))
        if len(k) == int(num_following.text):
            break

    k = driver.find_elements_by_xpath("//div[@class='isgrP']//li")
    following_list = []
    for i in range(len(k)):
        j = k[i].text
        s = j.split("\n")
        following_list.append(s[0])
    close_following = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[1]/div/div[2]/button/div")))
    close_following.click()
    return (len(following_list),following_list)

def scrape_followers():
    num_followers = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')))
    print("follower no :",int(num_followers.text))
    followers = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')))
    followers.click()
    sleep(10)
    fBody2 = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"//div[@class='isgrP']")))
    while True:
        driver.execute_script('arguments[0].scrollTop =  arguments[0].scrollTop + arguments[0].scrollHeight;', fBody2)
        sleep(0.75)
        l = driver.find_elements_by_xpath("//div[@class='isgrP']//li")
        if len(l) == int(num_followers.text):
            break

    l = driver.find_elements_by_xpath("//div[@class='isgrP']//li")
    followers_list = []
    for i in range(len(l)):
        j = l[i].text
        s = j.split("\n")
        followers_list.append(s[0])
    close_following = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/div/div[2]/button/div")))
    close_following.click()
    return ( len(followers_list), followers_list )

start = time()
login_func()
profile_func()
following_num, following_list = scrape_following()
followers_num, follower_list = scrape_followers()
logout_func()
driver.close()
end = time()

print("No of following scrapped:",following_num)
print("No of followers scrapped :",followers_num)
print("Time taken to scrap",following_num+followers_num,"profiles is",end-start,"sec")
q=[]
for i in following_list:
    if i not in follower_list:
        q.append(i)

print("People who are not following back are :")
[print(j) for j in q]
