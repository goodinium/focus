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
        if "mediapure.ru" in q or "82" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"https://ruscatalog.org/company/add/"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/form/div[1]/div/div[1]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /ruscatalog.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/form/div[1]/div/div[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /ruscatalog.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/form/div[1]/div/div[3]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /ruscatalog.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/form/div[1]/div/div[4]/div[1]/table/tbody/tr/td[1]/div/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /ruscatalog.org")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/form/div[2]/div/div[1]/div[1]/span/span[1]/span/span[1]").click()
        zz=brow.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
        zz.clear()
        zz.send_keys(city)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: city /ruscatalog.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/form/div[2]/div/div[1]/div[2]/input")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /ruscatalog.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/form/div[2]/div/div[1]/div[4]/input")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /ruscatalog.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/form/div[2]/div/div[1]/div[5]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl2 /ruscatalog.org")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/form/div[3]/div[2]/div[1]/label[1]").click()
    except Exception:
        print("Ошибка: timework /ruscatalog.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/form/div[6]/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /ruscatalog.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/form/div[7]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /ruscatalog.org")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/form/div[9]/label/input").click()

    except Exception:
        print("Ошибка: правила /ruscatalog.org")
        pass

    
    