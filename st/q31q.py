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
        if "orgpage" in q or "36" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://www.orgpage.ru/Cabinet/Create/"
    brow.get(url=w)
    sleep(1)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div[2]/form/div[2]/div[2]/div/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /www.orgpage.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div[2]/form/div[3]/div/textarea")
        zz.clear()
        zz.send_keys("Наркологическая клиника")
    except Exception:
        print("Ошибка: сфера /www.orgpage.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div[2]/form/div[4]/div[1]/div[1]/div[2]/input")
        zz.clear()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: city /www.orgpage.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div[2]/form/div[4]/div[2]/div/input")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /www.orgpage.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div[2]/form/div[5]/div[1]/div/div[3]/input")
        zz.clear()
        zz.send_keys(numcodcity)
    except Exception:
        print("Ошибка: numcodcity /www.orgpage.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div[2]/form/div[5]/div[1]/div/div[5]/input")
        zz.clear()
        zz.send_keys(numclshot)
    except Exception:
        print("Ошибка: numclshot /www.orgpage.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div[2]/form/div[7]/div/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /www.orgpage.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div[2]/form/div[8]/div[1]/div[2]/input")
        zz.clear()
        zz.send_keys("Наркологические клиники")
    except Exception:
        print("Ошибка: сфера2 /www.orgpage.ru")
        pass
    try:
        sleep(2)
        brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div/div[1]/button").click()
        sleep(1)
    except Exception:
        print("Ошибка: категории /www.orgpage.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div/div/form/div[2]/div[1]/div/div[3]/input")
        zz.clear()
        zz.send_keys(i)
    except Exception:
        print("Ошибка: i /www.orgpage.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div/div/form/div[2]/div[1]/div/div[4]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /www.orgpage.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div/div/form/div[2]/div[1]/div/div[5]/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw /www.orgpage.ru")
        pass
    
    # zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div[2]/form/div[2]/div[2]/div/input")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div[2]/form/div[3]/div/textarea")
    # zz.clear()
    # zz.send_keys("Наркологическая клиника")
    # zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div[2]/form/div[4]/div[1]/div[1]/div[2]/input")
    # zz.clear()
    # zz.send_keys(city)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div[2]/form/div[4]/div[2]/div/input")
    # zz.clear()
    # zz.send_keys(adress)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div[2]/form/div[5]/div[1]/div/div[3]/input")
    # zz.clear()
    # zz.send_keys(numcodcity)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div[2]/form/div[5]/div[1]/div/div[5]/input")
    # zz.clear()
    # zz.send_keys(numclshot)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div[2]/form/div[7]/div/textarea")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div[2]/form/div[8]/div[1]/div[2]/input")
    # zz.clear()
    # zz.send_keys("Наркологические клиники")
    # sleep(2)
    # brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div/div[1]/button").click()
    # sleep(1)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div/div/form/div[2]/div[1]/div/div[3]/input")
    # zz.clear()
    # zz.send_keys(i)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div/div/form/div[2]/div[1]/div/div[4]/input")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div/div/form/div[2]/div[1]/div/div[5]/input")
    # zz.clear()
    # zz.send_keys(passw)
