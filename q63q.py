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
        if "https://xn--80aae9bdmgfd2k.xn--p1ai" in q or "63" in q or "твоястрана.рф" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://xn--80aae9bdmgfd2k.xn--p1ai/%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C"
    brow.get(url=w)
    #---------------------------------------------------
    # https://xn--80aae9bdmgfd2k.xn--p1ai/   ---
    try:
        zz=brow.find_element(By.NAME, "Firm[name]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /твоястрана.рф")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[subtitle]")
        zz.clear()
        zz.send_keys("Наркологическая клиника")
    except Exception:
        print("Ошибка: сфера /твоястрана.рф")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[official_name]")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /твоястрана.рф")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[description]")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /твоястрана.рф")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[5]/select/option[10]").click()
        brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[5]/div[1]/select/option[11]").click()
        brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[5]/button").click()
    except Exception:
        print("Ошибка: категории /твоястрана.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[6]/div[2]/div[1]/div")
        zz.clear()
        zz.send_keys(keysl)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: keysl /твоястрана.рф")
        pass
    try:
        sleep(2)
        brow.find_element(By.XPATH, f"/html/body/main/div[2]/div/form/div[2]/div[1]/select/option[contains(text(),'{cityr}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/main/div[2]/div/form/div[2]/div[2]/div[1]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /твоястрана.рф")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[postal]")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /твоястрана.рф")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[street_name]")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /твоястрана.рф")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[building]")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /твоястрана.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[3]/div[1]/div[1]/table/tbody/tr/td[1]/div/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /твоястрана.рф")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[emails][0]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /твоястрана.рф")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[sites][0]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /твоястрана.рф")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[worktime][0][0]")
        zz.clear()
        zz.send_keys("0:00")
        zz=brow.find_element(By.NAME, "Firm[worktime][1][0]")
        zz.clear()
        zz.send_keys("0:00")
        zz=brow.find_element(By.NAME, "Firm[worktime][2][0]")
        zz.clear()
        zz.send_keys("0:00")
        zz=brow.find_element(By.NAME, "Firm[worktime][3][0]")
        zz.clear()
        zz.send_keys("0:00")
        zz=brow.find_element(By.NAME, "Firm[worktime][4][0]")
        zz.clear()
        zz.send_keys("0:00")
        zz=brow.find_element(By.NAME, "Firm[worktime][5][0]")
        zz.clear()
        zz.send_keys("0:00")
        zz=brow.find_element(By.NAME, "Firm[worktime][6][0]")
        zz.clear()
        zz.send_keys("23:30")
        zz1=brow.find_element(By.NAME, "Firm[worktime][0][1]")
        zz1.clear()
        zz1.send_keys("23:30")
        zz1=brow.find_element(By.NAME, "Firm[worktime][1][1]")
        zz1.clear()
        zz1.send_keys("23:30")
        zz1=brow.find_element(By.NAME, "Firm[worktime][2][1]")
        zz1.clear()
        zz1.send_keys("23:30")
        zz1=brow.find_element(By.NAME, "Firm[worktime][3][1]")
        zz1.clear()
        zz1.send_keys("23:30")
        zz1=brow.find_element(By.NAME, "Firm[worktime][4][1]")
        zz1.clear()
        zz1.send_keys("23:30")
        zz1=brow.find_element(By.NAME, "Firm[worktime][5][1]")
        zz1.clear()
        zz1.send_keys("23:30")
        zz1=brow.find_element(By.NAME, "Firm[worktime][6][1]")
        zz1.clear()
        zz1.send_keys("23:30")
    except Exception:
        print("Ошибка: timework /твоястрана.рф")
        pass
    try:
        zz1=brow.find_element(By.NAME, "User[email]")
        zz1.clear()
        zz1.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /твоястрана.рф")
        pass
    try:
        zz1=brow.find_element(By.NAME, "User[pass1]")
        zz1.clear()
        zz1.send_keys(passw)
    except Exception:
        print("Ошибка: passw1 /твоястрана.рф")
        pass
    try:
        zz1=brow.find_element(By.NAME, "User[pass2]")
        zz1.clear()
        zz1.send_keys(passw)
    except Exception:
        print("Ошибка: passw2 /твоястрана.рф")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[5]/div[4]/label/input").click()
        brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[6]/label/input").click()
    except Exception:
        print("Ошибка: правила /твоястрана.рф")
        pass
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
    # brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[5]/div[1]/select/option[11]").click()
    # brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[5]/button").click()
    # zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[6]/div[2]/div[1]/div")
    # zz.clear()
    # zz.send_keys(keysl)
    # zz.send_keys(Keys.ENTER)
    # zz=brow.find_element(By.NAME, "Firm[postal]")
    # zz.clear()
    # zz.send_keys(ind)
    # zz=brow.find_element(By.NAME, "Firm[street_name]")
    # zz.clear()
    # zz.send_keys(street)
    # zz=brow.find_element(By.NAME, "Firm[building]")
    # zz.clear()
    # zz.send_keys(home)
    # zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[3]/div[1]/div[1]/table/tbody/tr/td[1]/div/input")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "Firm[emails][0]")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "Firm[sites][0]")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "Firm[worktime][0][0]")
    # zz.clear()
    # zz.send_keys("0:00")
    # zz=brow.find_element(By.NAME, "Firm[worktime][1][0]")
    # zz.clear()
    # zz.send_keys("0:00")
    # zz=brow.find_element(By.NAME, "Firm[worktime][2][0]")
    # zz.clear()
    # zz.send_keys("0:00")
    # zz=brow.find_element(By.NAME, "Firm[worktime][3][0]")
    # zz.clear()
    # zz.send_keys("0:00")
    # zz=brow.find_element(By.NAME, "Firm[worktime][4][0]")
    # zz.clear()
    # zz.send_keys("0:00")
    # zz=brow.find_element(By.NAME, "Firm[worktime][5][0]")
    # zz.clear()
    # zz.send_keys("0:00")
    # zz=brow.find_element(By.NAME, "Firm[worktime][6][0]")
    # zz.clear()
    # zz.send_keys("23:30")
    # zz1=brow.find_element(By.NAME, "Firm[worktime][0][1]")
    # zz1.clear()
    # zz1.send_keys("23:30")
    # zz1=brow.find_element(By.NAME, "Firm[worktime][1][1]")
    # zz1.clear()
    # zz1.send_keys("23:30")
    # zz1=brow.find_element(By.NAME, "Firm[worktime][2][1]")
    # zz1.clear()
    # zz1.send_keys("23:30")
    # zz1=brow.find_element(By.NAME, "Firm[worktime][3][1]")
    # zz1.clear()
    # zz1.send_keys("23:30")
    # zz1=brow.find_element(By.NAME, "Firm[worktime][4][1]")
    # zz1.clear()
    # zz1.send_keys("23:30")
    # zz1=brow.find_element(By.NAME, "Firm[worktime][5][1]")
    # zz1.clear()
    # zz1.send_keys("23:30")
    # zz1=brow.find_element(By.NAME, "Firm[worktime][6][1]")
    # zz1.clear()
    # zz1.send_keys("23:30")
    # zz1=brow.find_element(By.NAME, "User[email]")
    # zz1.clear()
    # zz1.send_keys(mail)
    # zz1=brow.find_element(By.NAME, "User[pass1]")
    # zz1.clear()
    # zz1.send_keys(passw)
    # zz1=brow.find_element(By.NAME, "User[pass2]")
    # zz1.clear()
    # zz1.send_keys(passw)
    # brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[5]/div[4]/label/input").click()
    # brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[6]/label/input").click()