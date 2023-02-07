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
        if "infomesto" in q or "53" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://www.infomesto.com/business/add"
    brow.get(url=w)
    # http://yndx.ru/company/registration   ---
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[1]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /www.infomesto.com")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[2]/select/option[11]").click()
        sleep(2)
        brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[3]/select/option[10]").click()
    except Exception:
        print("Ошибка: категории /www.infomesto.com")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[7]/select/option[2]").click()
        sleep(2)
        brow.find_element(By.XPATH, f"/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[8]/select/option[contains(text(),'{cityr}')]").click()
    except Exception:
        print("Ошибка: xp /www.infomesto.com")
        pass
    
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[9]/input")
        zz.clear()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: city /www.infomesto.com")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[10]/input")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /www.infomesto.com")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[11]/input")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /www.infomesto.com")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[12]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /www.infomesto.com")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[14]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /www.infomesto.com")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[15]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /www.infomesto.com")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[17]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /www.infomesto.com")
        pass
    
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[1]/input")
    # zz.clear()
    # zz.send_keys(namecl)
    # brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[2]/select/option[11]").click()
    # sleep(2)
    # brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[7]/select/option[2]").click()
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[9]/input")
    # zz.clear()
    # zz.send_keys(city)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[10]/input")
    # zz.clear()
    # zz.send_keys(street)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[11]/input")
    # zz.clear()
    # zz.send_keys(home)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[12]/input")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[14]/input")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[15]/input")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/form/dl/fieldset[17]/textarea")
    # zz.clear()
    # zz.send_keys(desc)