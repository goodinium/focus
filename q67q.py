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
        if "rusfirm" in q or "67" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://rusfirm.biz/add"
    brow.get(url=w)
    # https://rusfirm.biz/add   ---
    try:
        zz=brow.find_element(By.NAME, "name")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /rusfirm.biz")
        pass
    try:
        zz=brow.find_element(By.NAME, "address")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /rusfirm.biz")
        pass
    try:
        zz=brow.find_element(By.NAME, "work")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /rusfirm.biz")
        pass
    try:
        zz=brow.find_element(By.NAME, "phones")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /rusfirm.biz")
        pass
    try:
        zz=brow.find_element(By.NAME, "website")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /rusfirm.biz")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/form/div[7]/div/select/option[555]").click()
    except Exception:
        print("Ошибка: mail /rusfirm.biz")
        pass
    try:
        zz=brow.find_element(By.NAME, "other")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /rusfirm.biz")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/div[2]/div/div[2]/div/form/div[2]/div/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /rusfirm.biz")
        pass
    
    # zz=brow.find_element(By.NAME, "name")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "address")
    # zz.clear()
    # zz.send_keys(adress)
    # zz=brow.find_element(By.NAME, "work")
    # zz.clear()
    # zz.send_keys(timework)
    # zz=brow.find_element(By.NAME, "phones")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "website")
    # zz.clear()
    # zz.send_keys(url)
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/form/div[7]/div/select/option[555]").click()
    # zz=brow.find_element(By.NAME, "other")
    # zz.clear()
    # zz.send_keys(desc)