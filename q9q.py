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
        if "spravkarf24" in q or "12" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://spravkarf24.ru/new-firm"
    brow.get(url=w)
    #---------------------------------------------------
    # https://spravkarf24.ru/new-firm   ---  0
    try:
        zz=brow.find_element(By.NAME, "Firm[name]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[subtitle]")
        zz.clear()
        zz.send_keys("Наркологическая клиника")
    except Exception:
        print("Ошибка: сфера /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[official_name]")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[description]")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /guidetorussia.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/main/div[3]/div/form/div[1]/div[5]/select/option[38]").click()
        brow.find_element(By.XPATH, "/html/body/main/div[3]/div/form/div[1]/div[5]/div[1]/select/option[7]").click()
        brow.find_element(By.XPATH, "/html/body/main/div[3]/div/form/div[1]/div[5]/button").click()
    except Exception:
        print("Ошибка: категории /guidetorussia.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/main/div[3]/div/form/div[2]/div[1]/select/option[contains(text(),'{cityr}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/main/div[3]/div/form/div[2]/div[2]/div[1]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: категории /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[postal]")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[street_name]")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[building]")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[3]/div/form/div[3]/div[1]/div[1]/table/tbody/tr/td[1]/div/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[emails][0]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[sites][0]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Firm[worktime]")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "User[email]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "User[pass1]")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw1 /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "User[pass2]")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw2 /guidetorussia.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/main/div[3]/div/form/div[5]/div[4]/label").click()
    except Exception:
        print("Ошибка: правила /guidetorussia.ru")
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
    # brow.find_element(By.XPATH, "/html/body/main/div[3]/div/form/div[1]/div[5]/select/option[38]").click()
    # brow.find_element(By.XPATH, "/html/body/main/div[3]/div/form/div[1]/div[5]/div[1]/select/option[7]").click()
    # brow.find_element(By.XPATH, "/html/body/main/div[3]/div/form/div[1]/div[5]/button").click()
    # zz=brow.find_element(By.NAME, "Firm[postal]")
    # zz.clear()
    # zz.send_keys(ind)
    # zz=brow.find_element(By.NAME, "Firm[street_name]")
    # zz.clear()
    # zz.send_keys(street)
    # zz=brow.find_element(By.NAME, "Firm[building]")
    # zz.clear()
    # zz.send_keys(home)
    # zz=brow.find_element(By.XPATH, "/html/body/main/div[3]/div/form/div[3]/div[1]/div[1]/table/tbody/tr/td[1]/div/input")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "Firm[emails][0]")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "Firm[sites][0]")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "Firm[worktime]")
    # zz.clear()
    # zz.send_keys(timework)
    # zz=brow.find_element(By.NAME, "User[email]")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "User[pass1]")
    # zz.clear()
    # zz.send_keys(passw)
    # zz=brow.find_element(By.NAME, "User[pass2]")
    # zz.clear()
    # zz.send_keys(passw)
    # brow.find_element(By.XPATH, "/html/body/main/div[3]/div/form/div[5]/div[4]/label").click()