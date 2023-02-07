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
        if "spravka-region" in q or "45" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://kazan.spravka-region.ru/new_organization"
    brow.get(url=w)
    # http://spravka-region.ru/company/registration   ---
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/header/div[2]/form/select/option[contains(text(),'{cityr}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div[1]/header/div[2]/form/span[1]/select/option[contains(text(),'{city}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/form/span[2]/span/select/optgroup[4]/option[4]").click()
        sleep(1)
        brow.find_element(By.XPATH, "//*[@id=\"button_search\"]").click()
        sleep(1)
        brow.find_element(By.XPATH, "//*[@id=\"new_organization_button\"]").click()
    except Exception:
        print("Ошибка: xp /spravka-region.ru")
        pass
    sleep(1)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/form/table[1]/tbody/tr[1]/td/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /spravka-region.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/form/table[1]/tbody/tr[2]/td/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /spravka-region.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/form/table[2]/tbody/tr[1]/td/select/optgroup[4]/option[4]").click()
    except Exception:
        print("Ошибка: категории /spravka-region.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"name_add_organization_spravka\"]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /spravka-region.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/form/table[2]/tbody/tr[3]/td/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /spravka-region.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/form/table[2]/tbody/tr[4]/td/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /spravka-region.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "hour_add_organization_spravka")
        zz.click()
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /spravka-region.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/form/table[2]/tbody/tr[7]/td/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /spravka-region.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"editorAds_ifr\"]")
        zz.click()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /spravka-region.ru")
        pass
    
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/form/table[1]/tbody/tr[1]/td/input")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(fio)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/form/table[1]/tbody/tr[2]/td/input")
    # zz.clear()
    # zz.send_keys(numclinic)
    # brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/form/table[2]/tbody/tr[1]/td/select/optgroup[4]/option[4]").click()
    # zz=brow.find_element(By.XPATH, "//*[@id=\"name_add_organization_spravka\"]")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/form/table[2]/tbody/tr[3]/td/input")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/form/table[2]/tbody/tr[4]/td/input")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "hour_add_organization_spravka")
    # zz.click()
    # zz.clear()
    # zz.send_keys(timework)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/form/table[2]/tbody/tr[7]/td/input")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.XPATH, "//*[@id=\"editorAds_ifr\"]")
    # zz.click()
    # zz.send_keys(desc)
    