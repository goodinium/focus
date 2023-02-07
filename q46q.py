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
        if "catalog-777" in q or "46" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://catalog-777.com/add-company/"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.NAME, "ent_name")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /catalog-777.com")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/div[4]/div/div[2]/select/option[contains(text(),'{cityr}')]").click()
    except Exception:
        print("Ошибка: xp /catalog-777.com")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[1]/input[30]").click()
    except Exception:
        print("Ошибка: категории /catalog-777.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "ent_address")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /catalog-777.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "ent_coord")
        zz.clear()
        zz.send_keys("55.652654,38.619035")
    except Exception:
        print("Ошибка: коорд /catalog-777.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "ent_phone")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /catalog-777.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "ent_email")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /catalog-777.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "ent_site")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /catalog-777.com")
        pass
    try:
        # brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[3]/div").click()
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[3]/div/div/iframe")
        zz.click()
        # zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /catalog-777.com")
        pass
    
    # zz=brow.find_element(By.NAME, "ent_name")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[1]/input[30]").click()
    # zz=brow.find_element(By.NAME, "ent_address")
    # zz.clear()
    # zz.send_keys(ciadress)
    # zz=brow.find_element(By.NAME, "ent_coord")
    # zz.clear()
    # zz.send_keys("55.652654,38.619035")
    # zz=brow.find_element(By.NAME, "ent_phone")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "ent_email")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "ent_site")
    # zz.clear()
    # zz.send_keys(url)
    
    
    
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[3]/div").click()
    # brow.find_element(By.XPATH, "//*[@id=\"cke_1_contents\"]").click()
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[3]/div/div/iframe")
    # zz.click()
    # sleep(1)
    # zz.clear()
    # zz.send_keys(desc)