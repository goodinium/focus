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
        if "msk.damspravku" in q or "41" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://msk.damspravku.ru/companies/new"
    brow.get(url=w)
    #--------------------------------------------------- 
    #https://msk.damspravku.ru/companies -------------------
    sleep(1)
    try:
        zz=brow.find_element(By.NAME, "company[name]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /msk.damspravku.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div/div/main/div/section/form/div[3]/a").click()
    except Exception:
        print("Ошибка: категории /msk.damspravku.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div/main/div/section/form/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys("7")
    except Exception:
        print("Ошибка:  /msk.damspravku.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div/main/div/section/form/div[2]/div[2]/input")
        zz.clear()
        zz.send_keys(numcodcity)
    except Exception:
        print("Ошибка: numcodcity /msk.damspravku.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div/main/div/section/form/div[2]/div[3]/input")
        zz.clear()
        zz.send_keys(numclshot)
    except Exception:
        print("Ошибка: numclshot /msk.damspravku.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "company[site]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /msk.damspravku.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "company[email]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /msk.damspravku.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "company[work_time]")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /msk.damspravku.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "company[addr_attributes][pindex]")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /msk.damspravku.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div/main/div/section/form/div[11]/input")
        zz.clear()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: city /msk.damspravku.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div/main/div/section/form/div[12]/input")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /msk.damspravku.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div/main/div/section/form/div[13]/input")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /msk.damspravku.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "company[description]")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /msk.damspravku.ru")
        pass
    # sleep(1)
    # zz=brow.find_element(By.NAME, "company[name]")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # brow.find_element(By.XPATH, "/html/body/div/div/main/div/section/form/div[3]/a").click()
    # zz=brow.find_element(By.XPATH, "/html/body/div/div/main/div/section/form/div[2]/div[1]/input")
    # zz.clear()
    # zz.send_keys("7")
    # zz=brow.find_element(By.XPATH, "/html/body/div/div/main/div/section/form/div[2]/div[2]/input")
    # zz.clear()
    # zz.send_keys(numcodcity)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div/main/div/section/form/div[2]/div[3]/input")
    # zz.clear()
    # zz.send_keys(numclshot)
    # zz=brow.find_element(By.NAME, "company[site]")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "company[email]")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "company[work_time]")
    # zz.clear()
    # zz.send_keys(timework)
    # zz=brow.find_element(By.NAME, "company[addr_attributes][pindex]")
    # zz.clear()
    # zz.send_keys(ind)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div/main/div/section/form/div[11]/input")
    # zz.clear()
    # zz.send_keys(city)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div/main/div/section/form/div[12]/input")
    # zz.clear()
    # zz.send_keys(street)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div/main/div/section/form/div[13]/input")
    # zz.clear()
    # zz.send_keys(home)
    # zz=brow.find_element(By.NAME, "company[description]")
    # zz.clear()
    # zz.send_keys(desc)