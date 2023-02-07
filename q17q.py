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
        if "korden" in q or "22" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://korden.org/companies/new"
    brow.get(url=w)
    # https://korden.org/companies/new   ---
    try:
        zz=brow.find_element(By.NAME, "email")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /korden.org")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[5]/div/form/div[2]/div[1]/div/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /korden.org")
        pass
    try:
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[5]/div/form/div[3]/div[1]/div/div/div/div/div[1]/div[2]/a[6]/div").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[5]/div/form/div[3]/div[1]/div/div/div/div/div[2]/div[2]/a[6]/div").click()
    except Exception:
        print("Ошибка: категории /korden.org")
        pass
    try:
        zz=brow.find_element(By.NAME, "title")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /korden.org")
        pass
    try:
        zz=brow.find_element(By.NAME, "address")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /korden.org")
        pass
    try:
        zz=brow.find_element(By.NAME, "contact_face")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /korden.org")
        pass
    try:
        zz=brow.find_element(By.NAME, "phone")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /korden.org")
        pass
    try:
        zz=brow.find_element(By.NAME, "site_url")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /korden.org")
        pass
    try:
        zz=brow.find_element(By.NAME, "anons")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /korden.org")
        pass
    
    # zz=brow.find_element(By.NAME, "email")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(mail)
    # sleep(1)
    # brow.find_element(By.XPATH, "/html/body/div[5]/div/form/div[3]/div[1]/div/div/div/div/div[1]/div[2]/a[6]/div").click()
    # sleep(1)
    # brow.find_element(By.XPATH, "/html/body/div[5]/div/form/div[3]/div[1]/div/div/div/div/div[2]/div[2]/a[6]/div").click()
    # zz=brow.find_element(By.NAME, "title")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "address")
    # zz.clear()
    # zz.send_keys(adress)
    # zz=brow.find_element(By.NAME, "contact_face")
    # zz.clear()
    # zz.send_keys(fio)
    # zz=brow.find_element(By.NAME, "phone")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "site_url")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "anons")
    # zz.clear()
    # zz.send_keys(desc)