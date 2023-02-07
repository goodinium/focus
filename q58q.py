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
        if "spravochnik-rf" in q or "58" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://spravochnik-rf.ru/add/"
    brow.get(url=w)
    # https://spravochnik-rf.ru/add/   ---  1 капча
    try:
        zz=brow.find_element(By.NAME, "PROPERTY[NAME]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /spravochnik-rf.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[2]/div/div[1]/form/div[2]/span/select/option[contains(text(),'{city} ({cityr})')]").click()
    except Exception:
        print("Ошибка: xp /spravochnik-rf.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/form/div[3]/span/select/option[59]").click()
    except Exception:
        print("Ошибка: категории /spravochnik-rf.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "PROPERTY[PROPERTY_postcode]")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /spravochnik-rf.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "PROPERTY[PROPERTY_address]")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /spravochnik-rf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/form/div[7]/span/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /spravochnik-rf.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "PROPERTY[PROPERTY_hours][]")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /spravochnik-rf.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "PROPERTY[PROPERTY_url]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /spravochnik-rf.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "PROPERTY[PROPERTY_email]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /spravochnik-rf.ru")
        pass
    
    # zz=brow.find_element(By.NAME, "PROPERTY[NAME]")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/form/div[3]/span/select/option[59]").click()
    # zz=brow.find_element(By.NAME, "PROPERTY[PROPERTY_postcode]")
    # zz.clear()
    # zz.send_keys(ind)
    # zz=brow.find_element(By.NAME, "PROPERTY[PROPERTY_address]")
    # zz.clear()
    # zz.send_keys(adress)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/form/div[7]/span/input")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "PROPERTY[PROPERTY_hours][]")
    # zz.clear()
    # zz.send_keys(timework)
    # zz=brow.find_element(By.NAME, "PROPERTY[PROPERTY_url]")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "PROPERTY[PROPERTY_email]")
    # zz.clear()
    # zz.send_keys(mail)