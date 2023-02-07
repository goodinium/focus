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
        if "feech" in q or "40" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://feech.org/new-company"
    brow.get(url=w)
    # https://feech.org/new-company   ---  0+-
    try:
        zz=brow.find_element(By.NAME, "username")
        zz.clear()
        zz.send_keys(i)
    except Exception:
        print("Ошибка: i /feech.org")
        pass
    try:
        zz=brow.find_element(By.NAME, "usermail")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /feech.org")
        pass
    try:
        zz=brow.find_element(By.NAME, "name")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /feech.org")
        pass
    try:
        zz=brow.find_element(By.NAME, "subtitle")
        zz.clear()
        zz.send_keys("Наркологическая клиника")
    except Exception:
        print("Ошибка: сфера /feech.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div/form/fieldset[2]/div[5]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /feech.org")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div/form/fieldset[2]/div[6]/div[1]/select[1]/option[17]").click()
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div/form/fieldset[2]/div[6]/div[1]/select[2]/option[51]").click()
    except Exception:
        print("Ошибка: категория /feech.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div/form/fieldset[2]/div[7]/div/div[1]/div")
        zz.clear()
        zz.send_keys(keysl)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: keysl /feech.org")
        pass
    try:
        zz=brow.find_element(By.NAME, "worktime[0][]")
        zz.clear()
        zz.send_keys("00:00 - 23:59")
        zz=brow.find_element(By.NAME, "worktime[1][]")
        zz.clear()
        zz.send_keys("00:00 - 23:59")
        zz=brow.find_element(By.NAME, "worktime[2][]")
        zz.clear()
        zz.send_keys("00:00 - 23:59")
        zz=brow.find_element(By.NAME, "worktime[3][]")
        zz.clear()
        zz.send_keys("00:00 - 23:59")
        zz=brow.find_element(By.NAME, "worktime[4][]")
        zz.clear()
        zz.send_keys("00:00 - 23:59")
        zz=brow.find_element(By.NAME, "worktime[5][]")
        zz.clear()
        zz.send_keys("00:00 - 23:59")
        zz=brow.find_element(By.NAME, "worktime[6][]")
        zz.clear()
        zz.send_keys("00:00 - 23:59")
    except Exception:
        print("Ошибка: timework /feech.org")
        pass
    try:
        zz=brow.find_element(By.NAME, "postal")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /feech.org")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/div/form/fieldset[3]/div[4]/div[1]/select[1]/option[contains(text(),'{cityr}')]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/div/form/fieldset[3]/div[4]/div[1]/select[2]/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: категория /feech.org")
        pass
    try:
        zz=brow.find_element(By.NAME, "street")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /feech.org")
        pass
    try:
        zz=brow.find_element(By.NAME, "home")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /feech.org")
        pass
    try:
        zz=brow.find_element(By.NAME, "phone[]")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /feech.org")
        pass
    try:
        zz=brow.find_element(By.NAME, "email[]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /feech.org")
        pass
    try:
        zz=brow.find_element(By.NAME, "site[]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /feech.org")
        pass
    try:
        zz=brow.find_element(By.NAME, "official_name")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /feech.org")
        pass
    sleep(5)
    try:
        brow.find_element(By.XPATH, "//*[@id=\"persinfo\"]").click()
    except Exception:
        print("Ошибка: правила /feech.org")
        pass
    
    # zz=brow.find_element(By.NAME, "username")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(i)
    # zz=brow.find_element(By.NAME, "usermail")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "name")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "subtitle")
    # zz.clear()
    # zz.send_keys("Наркологическая клиника")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div/form/fieldset[2]/div[5]/textarea")
    # zz.clear()
    # zz.send_keys(desc)
    # brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div/form/fieldset[2]/div[6]/div[1]/select[1]/option[17]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div/form/fieldset[2]/div[6]/div[1]/select[2]/option[51]").click()
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div/form/fieldset[2]/div[7]/div/div[1]/div")
    # zz.clear()
    # zz.send_keys(keysl)
    # zz.send_keys(Keys.ENTER)
    # zz=brow.find_element(By.NAME, "worktime[0][]")
    # zz.clear()
    # zz.send_keys("00:00 - 23:59")
    # zz=brow.find_element(By.NAME, "worktime[1][]")
    # zz.clear()
    # zz.send_keys("00:00 - 23:59")
    # zz=brow.find_element(By.NAME, "worktime[2][]")
    # zz.clear()
    # zz.send_keys("00:00 - 23:59")
    # zz=brow.find_element(By.NAME, "worktime[3][]")
    # zz.clear()
    # zz.send_keys("00:00 - 23:59")
    # zz=brow.find_element(By.NAME, "worktime[4][]")
    # zz.clear()
    # zz.send_keys("00:00 - 23:59")
    # zz=brow.find_element(By.NAME, "worktime[5][]")
    # zz.clear()
    # zz.send_keys("00:00 - 23:59")
    # zz=brow.find_element(By.NAME, "worktime[6][]")
    # zz.clear()
    # zz.send_keys("00:00 - 23:59")
    # zz=brow.find_element(By.NAME, "postal")
    # zz.clear()
    # zz.send_keys(ind)
    # zz=brow.find_element(By.NAME, "street")
    # zz.clear()
    # zz.send_keys(street)
    # zz=brow.find_element(By.NAME, "home")
    # zz.clear()
    # zz.send_keys(home)
    # zz=brow.find_element(By.NAME, "phone[]")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "email[]")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "site[]")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "official_name")
    # zz.clear()
    # zz.send_keys(unamecl)
    # brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div/form/fieldset[6]/div/input").click()