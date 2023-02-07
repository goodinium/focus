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
    for q in wwww:
        if "otzywy" in q or "26" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://www.otzywy.com/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%8E/"
    brow.get(url=w)
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/div[1]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: namecl /www.otzywy.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "name")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /www.otzywy.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "activity")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /www.otzywy.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "web")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /www.otzywy.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "email")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /www.otzywy.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "addr")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /www.otzywy.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "tel")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /www.otzywy.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "worktime")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /www.otzywy.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "fullname")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /www.otzywy.com")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[11]/textarea")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /www.otzywy.com")
        pass
    
    # zz=brow.find_element(By.NAME, "name")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "activity")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.NAME, "web")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "email")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "addr")
    # zz.clear()
    # zz.send_keys(adress)
    # zz=brow.find_element(By.NAME, "tel")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "worktime")
    # zz.clear()
    # zz.send_keys(timework)
    # zz=brow.find_element(By.NAME, "fullname")
    # zz.clear()
    # zz.send_keys(fio)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[11]/textarea")
    # zz.clear()
    # zz.send_keys(numclinic)