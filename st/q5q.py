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
        if "otzyvgid" in q or "5" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="http://otzyvgid.ru/dobavit-kompaniju.html"
    brow.get(url=w)
    #---------------------------------------------------
    try:
        zz=brow.find_element(By.NAME, "Places[name]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /otzyvgid.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/div[2]/div[4]/form/div[1]/div[1]/div[2]/div/div[1]/div").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[14]/div[2]/div[2]/div/div/ul/li[2]/ul/li[9]/div/span[3]/a/span").click()
        brow.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/div[2]/div[4]/form/div[1]/div[2]/div[2]/div/div[1]/div").click()
        sleep(1)
    except Exception:
        print("Ошибка: категории /otzyvgid.ru")
        pass
    try:
        bb=city[0]
        brow.find_element(By.LINK_TEXT, bb).click()
        sleep(1)
        brow.find_element(By.LINK_TEXT, city).click()
    except Exception:
        print("Ошибка: город /otzyvgid.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Places[work_time]")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /otzyvgid.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Places[address]")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /otzyvgid.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Places[phone]")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /otzyvgid.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Places[email]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /otzyvgid.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Places[site]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /otzyvgid.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Places[description]")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /otzyvgid.ru")
        pass
    # zz=brow.find_element(By.NAME, "Places[name]")
    # zz.clear()
    # zz.send_keys(namecl)
    # brow.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/div[2]/div[4]/form/div[1]/div[1]/div[2]/div/div[1]/div").click()
    # sleep(1)
    # brow.find_element(By.XPATH, "/html/body/div[14]/div[2]/div[2]/div/div/ul/li[2]/ul/li[9]/div/span[3]/a/span").click()
    # brow.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/div[2]/div[4]/form/div[1]/div[2]/div[2]/div/div[1]/div").click()
    # sleep(1)
    # bb=city[0]
    # brow.find_element(By.LINK_TEXT, bb).click()
    # sleep(1)
    # brow.find_element(By.LINK_TEXT, city).click()
    # zz=brow.find_element(By.NAME, "Places[work_time]")
    # zz.clear()
    # zz.send_keys(timework)
    # zz=brow.find_element(By.NAME, "Places[address]")
    # zz.clear()
    # zz.send_keys(adress)
    # zz=brow.find_element(By.NAME, "Places[phone]")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "Places[email]")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "Places[site]")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "Places[description]")
    # zz.clear()
    # zz.send_keys(desc)