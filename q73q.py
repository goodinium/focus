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
        if "spravka7.ru" in q or "73" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"https://spravka7.ru/add/"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/form/div[1]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /spravka7.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/form/div[2]/span/span[1]/span/ul/li/input")
        zz.clear()
        zz.send_keys("Наркологические клиники")
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: категория /spravka7.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/form/div[3]/span/span[1]/span/span[1]").click()
        zz=brow.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
        zz.clear()
        zz.send_keys(city)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: city /spravka7.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"address\"]")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: numclinic /spravka7.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/form/div[5]/div/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /spravka7.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/form/div[6]/div/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /spravka7.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/form/div[7]/div/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /spravka7.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/form/div[9]/input")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /spravka7.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/form/div[10]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /spravka7.ru")
        pass
    
    