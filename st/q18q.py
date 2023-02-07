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
        if "dorus" in q or "7" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="http://www.dorus.ru/add.html"
    brow.get(url=w)
    #--------------------------------------------------- 
    #https://msk.damspravku.ru/companies -------------------  1 капча
    sleep(1)
    try:
        brow.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div/div/table/tbody/tr[5]/td[2]/select/optgroup[19]/option[15]").click()
    except Exception:
        print("Ошибка: категории /www.dorus.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "title")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /www.dorus.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "text")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /www.dorus.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "price")
        zz.clear()
        zz.send_keys("100")
    except Exception:
        print("Ошибка: цена /www.dorus.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "name")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /www.dorus.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div/div[3]/div[1]/div/div/table/tbody/tr[21]/td[2]/table/tbody/tr/td[1]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: категории /www.dorus.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "email")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /www.dorus.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "phone")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /www.dorus.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "url")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /www.dorus.ru")
        pass
    # brow.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div/div/table/tbody/tr[5]/td[2]/select/optgroup[19]/option[15]").click()
    # zz=brow.find_element(By.NAME, "title")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "text")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.NAME, "price")
    # zz.clear()
    # zz.send_keys("100")
    # zz=brow.find_element(By.NAME, "name")
    # zz.clear()
    # zz.send_keys(fio)
    # zz=brow.find_element(By.NAME, "email")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "phone")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "url")
    # zz.clear()
    # zz.send_keys(url)