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
        if "opt-union" in q or "43" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://www.opt-union.ru/registration/"
    brow.get(url=w)
    # https://www.opt-union.ru/registration/   --- ошибка
    try:
        zz=brow.find_element(By.NAME, "Registration[email]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /www.opt-union.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Registration[password]")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw /www.opt-union.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Registration[company]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /www.opt-union.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div/div/div[3]/table/tbody/tr[2]/td[3]/div[1]/form/fieldset[2]/table/tbody/tr[2]/td[2]/select/option[34]").click()
        brow.find_element(By.XPATH, f"/html/body/div/div/div[3]/table/tbody/tr[2]/td[3]/div[1]/form/fieldset[2]/table/tbody/tr[3]/td[2]/select/option[contains(text(),'{cityr}')]").click()

    except Exception:
        print("Ошибка: city /www.opt-union.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Registration[city]")
        zz.clear()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: city /www.opt-union.ru")
        pass
    
    # zz=brow.find_element(By.NAME, "Registration[email]")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "Registration[password]")
    # zz.clear()
    # zz.send_keys(passw)
    # zz=brow.find_element(By.NAME, "Registration[company]")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "Registration[city]")
    # zz.clear()
    # zz.send_keys(city)