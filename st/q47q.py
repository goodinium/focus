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
        if "www.spr" in q or "47" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://www.spr.ru/checkplus.php"
    brow.get(url=w)
#https://saratov.moyaspravka.ru/ -------------------
    try:
        brow.find_element(By.XPATH, "/html/body/div/section/div[1]/div/div[1]/form/div[1]/label[1]").click()
    except Exception:
        print("Ошибка: категории /www.spr.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "name")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /www.spr.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"description\"]")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /www.spr.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "address")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /www.spr.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "phone[]")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /www.spr.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "site[]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /www.spr.ru")
        pass
    
    # brow.find_element(By.XPATH, "/html/body/div/section/div[1]/div/div[1]/form/div[1]/label[1]").click()
    # zz=brow.find_element(By.NAME, "name")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.XPATH, "//*[@id=\"description\"]")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.NAME, "address")
    # zz.clear()
    # zz.send_keys(street)
    # zz=brow.find_element(By.NAME, "phone[]")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "site[]")
    # zz.clear()
    # zz.send_keys(url)
    
    
    
    # zz=brow.find_element(By.NAME, "adres2")
    # zz.clear()
    # zz.send_keys(home)
    # zz=brow.find_element(By.NAME, "email")
    # zz.clear()
    # zz.send_keys(mail)
    