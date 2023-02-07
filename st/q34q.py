import array as arr
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def goo(brow,z,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind):
    br=brow
    brow.switch_to.window(brow.window_handles[z])
    ct1(br,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
def ct1(brow,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind):
    wwww=notwww.split("\n")
    for q in wwww:
        if "https://xn----9sbbbpi8a9bt6f.xn--p1ai" in q or "20" in q or "веб-службы.рф" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://xn----9sbbbpi8a9bt6f.xn--p1ai/?p=person&event=entity.create&entityName=User"
    brow.get(url=w)
#https://xn----9sbbbpi8a9bt6f.xn--p1ai/?p=person&event=entity.create&entityName=User -------------------
    sleep(1)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/div/div[3]/div[2]/div[1]/span/div[1]/div/span/div[2]/div[2]/span/form/div/span/div[1]/div[3]/div[2]/input")
        zz.clear()
        zz.send_keys(login)
    except Exception:
        print("Ошибка: login /веб-службы.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/div/div[3]/div[2]/div[1]/span/div[1]/div/span/div[2]/div[2]/span/form/div/span/div[1]/div[4]/div[2]/div/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw /веб-службы.рф")
        pass
    sleep(1)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/div/div[3]/div[2]/div[1]/span/div[1]/div/span/div[2]/div[2]/span/form/div/span/div[1]/div[5]/div[2]/input")
        zz.clear()
        zz.send_keys(f)
    except Exception:
        print("Ошибка: f /веб-службы.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/div/div[3]/div[2]/div[1]/span/div[1]/div/span/div[2]/div[2]/span/form/div/span/div[1]/div[6]/div[2]/input")
        zz.clear()
        zz.send_keys(i)
    except Exception:
        print("Ошибка: i /веб-службы.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/div/div[3]/div[2]/div[1]/span/div[1]/div/span/div[2]/div[2]/span/form/div/span/div[1]/div[7]/div[2]/input")
        zz.clear()
        zz.send_keys(o)
    except Exception:
        print("Ошибка: o /веб-службы.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/div/div[3]/div[2]/div[1]/span/div[1]/div/span/div[2]/div[2]/span/form/div/span/div[1]/div[8]/div[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /веб-службы.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/div/div[3]/div[2]/div[1]/span/div[1]/div/span/div[2]/div[2]/span/form/div/span/div[1]/div[9]/div[2]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /веб-службы.рф")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/center/div/div[3]/div[2]/div[1]/span/div[1]/div/span/div[2]/div[2]/span/form/div/span/div[1]/p/input").click()
    except Exception:
        print("Ошибка: правила /веб-службы.рф")
        pass
    
    # zz=brow.find_element(By.XPATH, "/html/body/center/div/div[3]/div[2]/div[1]/span/div[1]/div/span/div[2]/div[2]/span/form/div/span/div[1]/div[3]/div[2]/input")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(login)
    # zz=brow.find_element(By.XPATH, "/html/body/center/div/div[3]/div[2]/div[1]/span/div[1]/div/span/div[2]/div[2]/span/form/div/span/div[1]/div[4]/div[2]/div/input")
    # zz.clear()
    # zz.send_keys(passw)
    # sleep(1)
    # zz=brow.find_element(By.XPATH, "/html/body/center/div/div[3]/div[2]/div[1]/span/div[1]/div/span/div[2]/div[2]/span/form/div/span/div[1]/div[5]/div[2]/input")
    # zz.clear()
    # zz.send_keys(f)
    # zz=brow.find_element(By.XPATH, "/html/body/center/div/div[3]/div[2]/div[1]/span/div[1]/div/span/div[2]/div[2]/span/form/div/span/div[1]/div[6]/div[2]/input")
    # zz.clear()
    # zz.send_keys(i)
    # zz=brow.find_element(By.XPATH, "/html/body/center/div/div[3]/div[2]/div[1]/span/div[1]/div/span/div[2]/div[2]/span/form/div/span/div[1]/div[7]/div[2]/input")
    # zz.clear()
    # zz.send_keys(o)
    # zz=brow.find_element(By.XPATH, "/html/body/center/div/div[3]/div[2]/div[1]/span/div[1]/div/span/div[2]/div[2]/span/form/div/span/div[1]/div[8]/div[2]/input")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "/html/body/center/div/div[3]/div[2]/div[1]/span/div[1]/div/span/div[2]/div[2]/span/form/div/span/div[1]/div[9]/div[2]/input")
    # zz.clear()
    # zz.send_keys(numclinic)
    # brow.find_element(By.XPATH, "/html/body/center/div/div[3]/div[2]/div[1]/span/div[1]/div/span/div[2]/div[2]/span/form/div/span/div[1]/p/input").click()
    