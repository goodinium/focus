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
        if "495ru" in q or "69" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="http://495ru.ru/q/show_edit_adv/"
    brow.get(url=w)
    # http://495ru.ru/q/show_edit_adv/   ---  1капча
    try:
        brow.find_element(By.XPATH, "/html/body/div[3]/form/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/select/option[18]").click()
        brow.find_element(By.XPATH, "/html/body/div[3]/form/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/select/option[2]").click()
        brow.find_element(By.XPATH, "/html/body/div[3]/form/table/tbody/tr[1]/td/table/tbody/tr[5]/td[2]/select/option[3]").click()
    except Exception:
        print("Ошибка: категории /495ru.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "UserName")
        zz.click()
        zz.clear()
        zz.send_keys(i)
    except Exception:
        print("Ошибка: i /495ru.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "UserEmail")
        zz.click()
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /495ru.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/form/table/tbody/tr[1]/td/table/tbody/tr[10]/td[2]/input")
        zz.click()
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /495ru.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[3]/form/table/tbody/tr[1]/td/table/tbody/tr[12]/td[2]/a").click()
    except Exception:
        print("Ошибка:  /495ru.ru")
        pass
    try:
        # sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div[3]/form/table/tbody/tr[1]/td/table/tbody/tr[11]/td[2]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /495ru.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Url")
        zz.click()
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /495ru.ru")
        pass
    
    try:
        zz=brow.find_element(By.NAME, "Header")
        zz.click()
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /495ru.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Comment")
        zz.click()
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /495ru.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "Price")
        zz.click()
        zz.clear()
        zz.send_keys("100")
    except Exception:
        print("Ошибка: цена /495ru.ru")
        pass
    
    # brow.find_element(By.XPATH, "/html/body/div[3]/form/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/select/option[18]").click()
    # brow.find_element(By.XPATH, "/html/body/div[3]/form/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/select/option[2]").click()
    # brow.find_element(By.XPATH, "/html/body/div[3]/form/table/tbody/tr[1]/td/table/tbody/tr[5]/td[2]/select/option[3]").click()
    # zz=brow.find_element(By.NAME, "UserName")
    # zz.click()
    # zz.clear()
    # zz.send_keys(i)
    # zz=brow.find_element(By.NAME, "UserEmail")
    # zz.click()
    # zz.clear()
    # zz.send_keys(mail)
    # # sleep
    # zz=brow.find_element(By.XPATH, "/html/body/div[3]/form/table/tbody/tr[1]/td/table/tbody/tr[10]/td[2]/input")
    # zz.click()
    # zz.clear()
    # zz.send_keys(numclinic)
    # # brow.find_element(By.XPATH, ci).click()
    # brow.find_element(By.XPATH, "/html/body/div[3]/form/table/tbody/tr[1]/td/table/tbody/tr[12]/td[2]/a").click()
    # zz=brow.find_element(By.NAME, "Url")
    # zz.click()
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "Header")
    # zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "Comment")
    # zz.click()
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.NAME, "Price")
    # zz.click()
    # zz.clear()
    # zz.send_keys("100")
