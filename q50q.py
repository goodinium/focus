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
        if "mxkr.ru" in q or "50" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="http://mxkr.ru/ru/company/registration"
    brow.get(url=w)
    sleep(1)
    # https://russiabase.ru/org/orgadd.php   ---
    try:
        zz=brow.find_element(By.NAME, "company-name")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /mxkr.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "activity")
        zz.clear()
        zz.send_keys("Наркологическая клиника")
    except Exception:
        print("Ошибка: сфера /mxkr.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "about")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /mxkr.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[2]/div/div[2]/div/div/div/form/fieldset/div[2]/div[1]/div[2]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /mxkr.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/form/fieldset/div[2]/div[1]/div[3]/input[1]")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /mxkr.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/form/fieldset/div[2]/div[1]/div[4]/input[1]")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /mxkr.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/form/fieldset/div[2]/div[2]/div/input[1]")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /mxkr.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/form/fieldset/div[2]/div[4]/div/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /mxkr.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/form/fieldset/div[2]/div[5]/div/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /mxkr.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "contact-name")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /mxkr.ru")
        pass
    
    # zz=brow.find_element(By.NAME, "company-name")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "activity")
    # zz.clear()
    # zz.send_keys("Наркологическая клиника")
    # zz=brow.find_element(By.NAME, "about")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/form/fieldset/div[2]/div[1]/div[3]/input[1]")
    # zz.clear()
    # zz.send_keys(street)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/form/fieldset/div[2]/div[1]/div[4]/input[1]")
    # zz.clear()
    # zz.send_keys(home)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/form/fieldset/div[2]/div[2]/div/input[1]")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/form/fieldset/div[2]/div[4]/div/input")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/form/fieldset/div[2]/div[5]/div/input")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "contact-name")
    # zz.clear()
    # zz.send_keys(fio)
