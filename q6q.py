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
        if "baza-r" in q or "6" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="http://baza-r.ru/join/registration/"
    brow.get(url=w)
    #---------------------------------------------------
    # http://baza-r.ru/join/registration/   ---  
    try:
        zz=brow.find_element(By.NAME, "name")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /baza-r.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "email")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /baza-r.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "siteAdr")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /baza-r.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "tels")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /baza-r.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "about")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /baza-r.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "City")
        zz.clear()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: city /baza-r.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "adres")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /baza-r.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "firm_catalog")
        zz.clear()
        zz.send_keys("Наркологическая клиника")
    except Exception:
        print("Ошибка: сфера /baza-r.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/div/form/div[13]/img").click()
    except Exception:
        print("Ошибка: категории /baza-r.ru")
        pass
    sleep(1)
    try:
        zz=brow.find_element(By.NAME, "s_pass")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw /baza-r.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "s_mail")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /baza-r.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "s_contact")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /baza-r.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/div/form/div[4]/div/table/tbody/tr[2]/td/label/input").click()
        brow.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/div/form/div[4]/div/table/tbody/tr[3]/td/label/input").click()
    except Exception:
        print("Ошибка: правила /baza-r.ru")
        pass
    
    # zz=brow.find_element(By.NAME, "name")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "email")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "siteAdr")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "tels")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "about")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.NAME, "City")
    # zz.clear()
    # zz.send_keys(city)
    # zz=brow.find_element(By.NAME, "adres")
    # zz.clear()
    # zz.send_keys(adress)
    # zz=brow.find_element(By.NAME, "firm_catalog")
    # zz.clear()
    # zz.send_keys("Наркологическая клиника")
    # brow.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/div/form/div[13]/img").click()
    # sleep(1)
    # zz=brow.find_element(By.NAME, "s_pass")
    # zz.clear()
    # zz.send_keys(passw)
    # zz=brow.find_element(By.NAME, "s_mail")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "s_contact")
    # zz.clear()
    # zz.send_keys(fio)
    # brow.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/div/form/div[4]/div/table/tbody/tr[2]/td/label/input").click()
    # brow.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/div/form/div[4]/div/table/tbody/tr[3]/td/label/input").click()