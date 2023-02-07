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
        if "spravkaru.info" in q or "6" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://spravkaru.info/create/company"
    brow.get(url=w)
    #---------------------------------------------------
    # https://spravkaru.info/create/company   ---
    try:
        zz=brow.find_element(By.NAME, "name")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /spravkaru.info")
        pass
    try:
        zz=brow.find_element(By.NAME, "subtitle")
        zz.clear()
        zz.send_keys("Наркологическая клиника")
    except Exception:
        print("Ошибка: сфера /spravkaru.info")
        pass
    try:
        zz=brow.find_element(By.NAME, "official_name")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /spravkaru.info")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[2]/form/div/div[4]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /spravkaru.info")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[2]/form/div/div[5]/div[1]/select[1]/option[7]").click()
        brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[2]/form/div/div[5]/div[1]/select[2]/option[40]").click()
        brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[2]/form/div/div[5]/div[1]/span").click()
    except Exception:
        print("Ошибка: категории /spravkaru.info")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[2]/form/div/div[6]/div/div[1]/div")
        zz.clear()
        zz.send_keys(keysl)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: keysl /spravkaru.info")
        pass
    
    try:
        zz=brow.find_element(By.NAME, "postal")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /spravkaru.info")
        pass
    try:
        zz=brow.find_element(By.NAME, "street")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /spravkaru.info")
        pass
    try:
        zz=brow.find_element(By.NAME, "home")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /spravkaru.info")
        pass
    try:
        zz=brow.find_element(By.NAME, "phone[]")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /spravkaru.info")
        pass
    try:
        zz=brow.find_element(By.NAME, "site[]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /spravkaru.info")
        pass
    try:
        zz=brow.find_element(By.NAME, "email[]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /spravkaru.info")
        pass
    try:
        zz=brow.find_element(By.NAME, "worktime[0][work][0]")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.NAME, "worktime[1][work][0]")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.NAME, "worktime[2][work][0]")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.NAME, "worktime[3][work][0]")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.NAME, "worktime[4][work][0]")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.NAME, "worktime[5][work][0]")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.NAME, "worktime[6][work][0]")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.NAME, "worktime[0][work][1]")
        zz.clear()
        zz.send_keys("23:59")
        zz=brow.find_element(By.NAME, "worktime[1][work][1]")
        zz.clear()
        zz.send_keys("23:59")
        zz=brow.find_element(By.NAME, "worktime[2][work][1]")
        zz.clear()
        zz.send_keys("23:59")
        zz=brow.find_element(By.NAME, "worktime[3][work][1]")
        zz.clear()
        zz.send_keys("23:59")
        zz=brow.find_element(By.NAME, "worktime[4][work][1]")
        zz.clear()
        zz.send_keys("23:59")
        zz=brow.find_element(By.NAME, "worktime[5][work][1]")
        zz.clear()
        zz.send_keys("23:59")
        zz=brow.find_element(By.NAME, "worktime[6][work][1]")
        zz.clear()
        zz.send_keys("23:59")
    except Exception:
        print("Ошибка: timework /spravkaru.info")
        pass
    try:
        zz=brow.find_element(By.NAME, "user_email")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /spravkaru.info")
        pass
    try:
        zz=brow.find_element(By.NAME, "user_pass1")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw1 /spravkaru.info")
        pass
    try:
        zz=brow.find_element(By.NAME, "user_pass2")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw2 /spravkaru.info")
        pass
    try:
        sleep(5)
        brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[2]/form/div/div[11]/input").click()
        brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[2]/form/div/div[12]/input").click()
    except Exception:
        print("Ошибка: правила /spravkaru.info")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/div[4]/div[1]/div[2]/form/div/div[7]/div[1]/div/div/select[1]/option[contains(text(),'{cityr}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div[1]/div[4]/div[1]/div[2]/form/div/div[7]/div[1]/div/div/select[2]/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: x[] /spravkaru.info")
        pass
   
    # zz=brow.find_element(By.NAME, "name")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "subtitle")
    # zz.clear()
    # zz.send_keys("наркологическая клиника")
    # zz=brow.find_element(By.NAME, "official_name")
    # zz.clear()
    # zz.send_keys(unamecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[2]/form/div/div[4]/textarea")
    # zz.clear()
    # zz.send_keys(desc)
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[2]/form/div/div[5]/div[1]/select[1]/option[7]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[2]/form/div/div[5]/div[1]/select[2]/option[40]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[2]/form/div/div[5]/div[1]/span").click()
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[2]/form/div/div[6]/div/div[1]/div")
    # zz.clear()
    # zz.send_keys(keysl)
    # zz.send_keys(Keys.ENTER)
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
    # zz=brow.find_element(By.NAME, "site[]")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "email[]")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "worktime[0][work][0]")
    # zz.clear()
    # zz.send_keys("00:00")
    # zz=brow.find_element(By.NAME, "worktime[1][work][0]")
    # zz.clear()
    # zz.send_keys("00:00")
    # zz=brow.find_element(By.NAME, "worktime[2][work][0]")
    # zz.clear()
    # zz.send_keys("00:00")
    # zz=brow.find_element(By.NAME, "worktime[3][work][0]")
    # zz.clear()
    # zz.send_keys("00:00")
    # zz=brow.find_element(By.NAME, "worktime[4][work][0]")
    # zz.clear()
    # zz.send_keys("00:00")
    # zz=brow.find_element(By.NAME, "worktime[5][work][0]")
    # zz.clear()
    # zz.send_keys("00:00")
    # zz=brow.find_element(By.NAME, "worktime[6][work][0]")
    # zz.clear()
    # zz.send_keys("00:00")
    # zz=brow.find_element(By.NAME, "worktime[0][work][1]")
    # zz.clear()
    # zz.send_keys("23:59")
    # zz=brow.find_element(By.NAME, "worktime[1][work][1]")
    # zz.clear()
    # zz.send_keys("23:59")
    # zz=brow.find_element(By.NAME, "worktime[2][work][1]")
    # zz.clear()
    # zz.send_keys("23:59")
    # zz=brow.find_element(By.NAME, "worktime[3][work][1]")
    # zz.clear()
    # zz.send_keys("23:59")
    # zz=brow.find_element(By.NAME, "worktime[4][work][1]")
    # zz.clear()
    # zz.send_keys("23:59")
    # zz=brow.find_element(By.NAME, "worktime[5][work][1]")
    # zz.clear()
    # zz.send_keys("23:59")
    # zz=brow.find_element(By.NAME, "worktime[6][work][1]")
    # zz.clear()
    # zz.send_keys("23:59")
    # zz=brow.find_element(By.NAME, "user_email")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "user_pass1")
    # zz.clear()
    # zz.send_keys(passw)
    # zz=brow.find_element(By.NAME, "user_pass2")
    # zz.clear()
    # zz.send_keys(passw)
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[2]/form/div/div[11]/input").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[2]/form/div/div[12]/input").click()