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
        if "vibirai" in q or "61" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://vibirai.ru/submit.html"
    brow.get(url=w)
    # https://vibirai.ru/submit.html   --- ошибка
    try:
        zz=brow.find_element(By.NAME, "content[name]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /vibirai.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[2]/div[3]/div/div/div[2]/div[1]/div/form/div[2]/select/option[contains(text(),'{city}')]").click()

    except Exception:
        print("Ошибка: xp /vibirai.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "content[address]")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /vibirai.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "content[phone]")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /vibirai.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "content[email]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail1 /vibirai.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "content[catalog]")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /vibirai.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "content[www]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /vibirai.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "content[contact_email]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /vibirai.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "content[routine]")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /vibirai.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "content[mobile_phone]")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /vibirai.ru")
        pass
    
    # zz=brow.find_element(By.NAME, "content[name]")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "content[address]")
    # zz.clear()
    # zz.send_keys(adress)
    # zz=brow.find_element(By.NAME, "content[phone]")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "content[email]")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "content[catalog]")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.NAME, "content[www]")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "content[contact_email]")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "content[routine]")
    # zz.clear()
    # zz.send_keys(timework)
    # zz=brow.find_element(By.NAME, "content[mobile_phone]")
    # zz.clear()
    # zz.send_keys(numclinic)