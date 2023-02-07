import array as arr
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def goo(brow,z,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind):
    br=brow
    brow.execute_script("window.open('');")
    brow.switch_to.window(brow.window_handles[z])
    ct1(br,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
def ct1(brow,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind):
    wwww=notwww.split("\n")
    cit=city
    for q in wwww:
        if "bizly.ru" in q or "75" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"https://bigspr.ru/add/"
    brow.get(url="http://translit-online.ru/")
    
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[3]/form/textarea[1]")
        # zz.clear()
        zz.click()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: переход1 /bizly.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div/div[3]/form/div[2]/div/input[1]").click()
    except Exception:
        print("Ошибка: переход2 /bizly.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[3]/form/textarea[2]").text
        # zz.click()
        # zz=zz.text()
        zz=zz.lower()
        print(zz)
        brow.get(url=f"https://{zz}.bizly.ru/add/")
        # brow.find_element(By.XPATH, "/html/body/div[1]/header/div[3]/div[2]/nav/ul/li[2]/a").click()
    except Exception:
        print("Ошибка: переход3 /bizly.ru")
        pass
    
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/form/div/div/div[1]/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /bigspr.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[3]/form/div/div/div[2]/div[2]/div[1]/div/div/span[1]/span[1]/span").click()
        zz=brow.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
        zz.clear()
        zz.send_keys("Наркологические клиники")
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: категории /bizly.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[3]/form/div/div/div[3]/div[2]/div[1]/span/span[1]/span/span[1]").click()
        zz=brow.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
        zz.clear()
        zz.send_keys(city)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: city /bizly.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/form/div/div/div[3]/div[4]/div[1]/div/input")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /bizly.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/form/div/div/div[4]/div[2]/div[1]/div/div/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /bizly.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/form/div/div/div[5]/div[2]/div[1]/div/div/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /bizly.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/form/div/div/div[6]/div[2]/div[1]/div/div/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /bizly.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/form/div/div/div[8]/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /bizly.ru")
        pass
 
    
    