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
        if "companyinform" in q or "7" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://companyinform.ru/add-company"
    brow.get(url=w)
    #---------------------------------------------------
    # https://companyinform.ru/add-company   ---
    try:
        zz=brow.find_element(By.NAME, "Firm[name]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /companyinform.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[subtitle]")
        zz.clear()
        zz.send_keys("Наркологическая клиника")
    except Exception:
        print("Ошибка: сфера /companyinform.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[official_name]")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /companyinform.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[description]")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /companyinform.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[5]/select/option[10]").click()
        brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[5]/div[1]/select/option[29]").click()
    except Exception:
        print("Ошибка: категории /companyinform.ru")
        pass
    sleep(1)
    try:  
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[6]/div[2]/div[1]/div")
        zz.send_keys(keysl)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: keysl /companyinform.ru")
        pass
    try:
        sleep(2)
        brow.find_element(By.XPATH, f"/html/body/main/div[2]/div/form/div[2]/div[2]/div[1]/select/option[contains(text(),'{cityr}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/main/div[2]/div/form/div[2]/div[3]/div[1]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /companyinform.ru")
        pass
    sleep(2)
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"firm-postal\"]")
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /companyinform.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"firm-street_name\"]")
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /companyinform.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"firm-building\"]")
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /companyinform.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[3]/div[1]/div[1]/table/tbody/tr/td[1]/div/input")
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /companyinform.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[emails][0]")
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /companyinform.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[sites][0]")
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /companyinform.ru")
        pass
    try:
         zz=brow.find_element(By.NAME, "Firm[worktime][0][0]")
         zz.send_keys("00:00")
         zz=brow.find_element(By.NAME, "Firm[worktime][1][0]")
         zz.send_keys("00:00")
         zz=brow.find_element(By.NAME, "Firm[worktime][2][0]")
         zz.send_keys("00:00")
         zz=brow.find_element(By.NAME, "Firm[worktime][3][0]")
         zz.send_keys("00:00")
         zz=brow.find_element(By.NAME, "Firm[worktime][4][0]")
         zz.send_keys("00:00")
         zz=brow.find_element(By.NAME, "Firm[worktime][5][0]")
         zz.send_keys("00:00")
         zz=brow.find_element(By.NAME, "Firm[worktime][6][0]")
         zz.send_keys("00:00")
         zz=brow.find_element(By.NAME, "Firm[worktime][0][1]")
         zz.send_keys("23:30")
         zz=brow.find_element(By.NAME, "Firm[worktime][1][1]")
         zz.send_keys("23:30")
         zz=brow.find_element(By.NAME, "Firm[worktime][2][1]")
         zz.send_keys("23:30")
         zz=brow.find_element(By.NAME, "Firm[worktime][3][1]")
         zz.send_keys("23:30")
         zz=brow.find_element(By.NAME, "Firm[worktime][4][1]")
         zz.send_keys("23:30")
         zz=brow.find_element(By.NAME, "Firm[worktime][5][1]")
         zz.send_keys("23:30")
         zz=brow.find_element(By.NAME, "Firm[worktime][6][1]")
         zz.send_keys("23:30")
    except Exception:
        print("Ошибка: timework /companyinform.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "User[email]")
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /companyinform.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "User[pass1]")
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw1 /companyinform.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "User[pass2]")
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw2 /companyinform.ru")
        pass
    # sleep(2)
    # try:
    #     brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[5]/div[4]").click()
    # except Exception:
    #     print("Ошибка: правила /companyinform.ru")
    #     pass
    
    
    
    # zz=brow.find_element(By.NAME, "Firm[name]")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "Firm[subtitle]")
    # zz.clear()
    # zz.send_keys("Наркологическая клиника")
    # zz=brow.find_element(By.NAME, "Firm[official_name]")
    # zz.clear()
    # zz.send_keys(unamecl)
    # zz=brow.find_element(By.NAME, "Firm[description]")
    # zz.clear()
    # zz.send_keys(desc)
    # brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[5]/select/option[10]").click()
    # brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[5]/div[1]/select/option[29]").click()
    # # sleep(1)
    # # brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[5]/button").click()
    # sleep(1)
    # zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[6]/div[2]/div[1]/div")
    # zz.send_keys(keysl)
    # zz.send_keys(Keys.ENTER)
    # zz=brow.find_element(By.XPATH, "//*[@id=\"firm-street_name\"]")
    # zz.send_keys(street)
    # zz=brow.find_element(By.XPATH, "//*[@id=\"firm-building\"]")
    # zz.send_keys(home)
    # zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[3]/div[1]/div[1]/table/tbody/tr/td[1]/div/input")
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "Firm[emails][0]")
    # #zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "Firm[sites][0]")
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "Firm[worktime][0][0]")
    # zz.send_keys("00:00")
    # zz=brow.find_element(By.NAME, "Firm[worktime][1][0]")
    # zz.send_keys("00:00")
    # zz=brow.find_element(By.NAME, "Firm[worktime][2][0]")
    # zz.send_keys("00:00")
    # zz=brow.find_element(By.NAME, "Firm[worktime][3][0]")
    # zz.send_keys("00:00")
    # zz=brow.find_element(By.NAME, "Firm[worktime][4][0]")
    # zz.send_keys("00:00")
    # zz=brow.find_element(By.NAME, "Firm[worktime][5][0]")
    # zz.send_keys("00:00")
    # zz=brow.find_element(By.NAME, "Firm[worktime][6][0]")
    # zz.send_keys("00:00")
    # zz=brow.find_element(By.NAME, "Firm[worktime][0][1]")
    # zz.send_keys("23:30")
    # zz=brow.find_element(By.NAME, "Firm[worktime][1][1]")
    # zz.send_keys("23:30")
    # zz=brow.find_element(By.NAME, "Firm[worktime][2][1]")
    # zz.send_keys("23:30")
    # zz=brow.find_element(By.NAME, "Firm[worktime][3][1]")
    # zz.send_keys("23:30")
    # zz=brow.find_element(By.NAME, "Firm[worktime][4][1]")
    # zz.send_keys("23:30")
    # zz=brow.find_element(By.NAME, "Firm[worktime][5][1]")
    # zz.send_keys("23:30")
    # zz=brow.find_element(By.NAME, "Firm[worktime][6][1]")
    # zz.send_keys("23:30")
    # zz=brow.find_element(By.NAME, "User[email]")
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "User[pass1]")
    # zz.send_keys(passw)
    # zz=brow.find_element(By.NAME, "User[pass2]")
    # zz.send_keys(passw)
    