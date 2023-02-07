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
        if "orghost" in q or "60" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://orghost.ru/"
    brow.get(url=w)
    # https://orghost.ru/   ---  1 капча,недо конц
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/footer/div/div[2]/div[1]/ul/li[1]/a").click()
    except Exception:
        print("Ошибка: категории /orghost.ru")
        pass
    sleep(4)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div/form/table/tbody/tr[1]/td[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /orghost.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "phone")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /orghost.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "site")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /orghost.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "addr_city")
        zz.clear()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: city /orghost.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "address")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /orghost.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "about")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /orghost.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div/form/table/tbody/tr[7]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /orghost.ru")
        pass
    # brow.find_element(By.XPATH, "/html/body/div[2]/footer/div/div[2]/div[1]/ul/li[1]/a").click()
    # sleep(1)
    # zz=brow.find_element(By.NAME, "phone")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "site")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "addr_city")
    # zz.clear()
    # zz.send_keys(city)
    # zz=brow.find_element(By.NAME, "address")
    # zz.clear()
    # zz.send_keys(adress)
    # zz=brow.find_element(By.NAME, "about")
    # zz.clear()
    # zz.send_keys(desc)
    
    
    
    # zz=brow.find_element(By.NAME, "email")
    # zz.clear()
    # zz.send_keys(mail)
