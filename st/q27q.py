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
        if "wikiotzyv" in q or "55" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://rstv.wikiotzyv.org/addfirm"
    brow.get(url=w)
    # http://yndx.ru/company/registration   ---
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[1]/div[2]/div/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /yndx.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[1]/div[3]/div[1]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /yndx.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[2]/div[1]/div/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /yndx.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[2]/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: tupecl /yndx.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[2]/div[4]/div/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /yndx.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[3]/div[1]/div[1]/select[1]/option[10]").click()
    except Exception:
        print("Ошибка: категории /yndx.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[3]/div[2]/div/div[1]/div")
        zz.clear()
        zz.send_keys(keysl)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: keysl /yndx.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[4]/div[1]/div/input")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /yndx.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/div/main/div/div/form/fieldset[4]/div[2]/div/select/option[contains(text(),'{cityr}')]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/div/main/div/div/form/fieldset[4]/div[3]/div/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /yndx.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[4]/div[4]/div/input")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /yndx.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[4]/div[5]/div/input")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /yndx.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[1]/div/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /yndx.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[3]/div/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /yndx.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[4]/div/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /yndx.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[5]/div/div[1]/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys("00:00 - 23:59")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[5]/div/div[2]/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys("00:00 - 23:59")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[5]/div/div[3]/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys("00:00 - 23:59")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[5]/div/div[4]/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys("00:00 - 23:59")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[5]/div/div[5]/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys("00:00 - 23:59")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[5]/div/div[6]/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys("00:00 - 23:59")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[5]/div/div[7]/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys("00:00 - 23:59")
    except Exception:
        print("Ошибка: timework /yndx.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[6]/div[2]/div/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /yndx.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/div[1]/input").click()
        brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/div[2]/input").click()
    except Exception:
        print("Ошибка: правила /yndx.ru")
        pass
    
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[1]/div[2]/div/input")
    # zz.clear()
    # zz.send_keys(fio)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[1]/div[3]/div[1]/input")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[2]/div[1]/div/input")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[2]/div[2]/div[1]/input")
    # zz.clear()
    # zz.send_keys(tupecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[2]/div[4]/div/textarea")
    # zz.clear()
    # zz.send_keys(desc)
    # brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[3]/div[1]/div[1]/select[1]/option[10]").click()
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[3]/div[2]/div/div[1]/div")
    # zz.clear()
    # zz.send_keys(keysl)
    # zz.send_keys(Keys.ENTER)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[4]/div[1]/div/input")
    # zz.clear()
    # zz.send_keys(ind)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[4]/div[4]/div/input")
    # zz.clear()
    # zz.send_keys(street)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[4]/div[5]/div/input")
    # zz.clear()
    # zz.send_keys(home)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[1]/div/input")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[3]/div/input")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[4]/div/input")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[5]/div/div[1]/div[2]/div[1]/input")
    # zz.clear()
    # zz.send_keys("00:00 - 23:59")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[5]/div/div[2]/div[2]/div[1]/input")
    # zz.clear()
    # zz.send_keys("00:00 - 23:59")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[5]/div/div[3]/div[2]/div[1]/input")
    # zz.clear()
    # zz.send_keys("00:00 - 23:59")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[5]/div/div[4]/div[2]/div[1]/input")
    # zz.clear()
    # zz.send_keys("00:00 - 23:59")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[5]/div/div[5]/div[2]/div[1]/input")
    # zz.clear()
    # zz.send_keys("00:00 - 23:59")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[5]/div/div[6]/div[2]/div[1]/input")
    # zz.clear()
    # zz.send_keys("00:00 - 23:59")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[5]/div[5]/div/div[7]/div[2]/div[1]/input")
    # zz.clear()
    # zz.send_keys("00:00 - 23:59")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/fieldset[6]/div[2]/div/input")
    # zz.clear()
    # zz.send_keys(fio)
    # brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/div[1]/input").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/div[2]/input").click()
    