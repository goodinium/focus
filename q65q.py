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
    cit=city
    for q in wwww:
        if "strananaladoni.ru" in q or "65" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"https://strananaladoni.ru/new-firm"
    brow.get(url=w)
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[2]/form/div[2]/div[2]/div[1]/select/option[contains(text(),'{cityr}')]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[2]/form/div[2]/div[3]/div[1]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: правила /strananaladoni.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[1]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /strananaladoni.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[2]/input")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: tupecl /strananaladoni.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[3]/input")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /strananaladoni.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[4]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /strananaladoni.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[5]/select/option[18]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[5]/div[1]/select/option[29]").click()
    except Exception:
        print("Ошибка: категории /strananaladoni.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[6]/div[2]/div[1]/div")
        zz.clear()
        zz.send_keys(keysl)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: keysl /strananaladoni.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[2]/div[4]/input")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /strananaladoni.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[2]/div[5]/input")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /strananaladoni.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[2]/div[6]/input")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /strananaladoni.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[3]/div[1]/div[1]/table/tbody/tr/td[1]/div/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /strananaladoni.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[3]/div[3]/div[1]/table/tbody/tr/td[1]/div/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /strananaladoni.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[3]/div[4]/div[1]/table/tbody/tr/td[1]/div/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /strananaladoni.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[4]/div[1]/div/div[1]/div/div[1]/input")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[4]/div[1]/div/div[1]/div/div[2]/input")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[4]/div[1]/div/div[2]/div/div[1]/input")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[4]/div[1]/div/div[2]/div/div[2]/input")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[4]/div[1]/div/div[3]/div/div[1]/input")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[4]/div[1]/div/div[3]/div/div[2]/input")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[4]/div[1]/div/div[4]/div/div[1]/input")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[4]/div[1]/div/div[4]/div/div[2]/input")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[4]/div[1]/div/div[5]/div/div[1]/input")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[4]/div[1]/div/div[5]/div/div[2]/input")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[4]/div[1]/div/div[6]/div/div[1]/input")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[4]/div[1]/div/div[6]/div/div[2]/input")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[4]/div[1]/div/div[7]/div/div[1]/input")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[4]/div[1]/div/div[7]/div/div[2]/input")
        zz.clear()
        zz.send_keys("00:00")
        
    except Exception:
        print("Ошибка: timework /strananaladoni.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[5]/div[1]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /strananaladoni.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[5]/div[2]/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw1 /strananaladoni.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[5]/div[3]/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw2 /strananaladoni.ru")
        pass
    sleep(2)
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[5]/div[4]/label/input").click()
    except Exception:
        print("Ошибка: правила /strananaladoni.ru")
        pass
    
    
    