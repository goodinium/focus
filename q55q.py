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
        if "allinform" in q or "55" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://www.allinform.ru/page39.html"
    brow.get(url=w)
    # https://www.allinform.ru/page39.html   ---  0 иногда 1, капча
    try:
        zz=brow.find_element(By.NAME, "org_name")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /www.allinform.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "your_address")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /www.allinform.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[8]/section/form/div[1]/table/tbody/tr[7]/td/table/tbody/tr[3]/td[1]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /www.allinform.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "your_email")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /www.allinform.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "your_url")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /www.allinform.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[8]/section/form/div[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/span").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[8]/section/form/div[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/span").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[8]/section/div[4]/table/tbody/tr/td/table[2]/tbody/tr/td/span[9]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[8]/section/form/div[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/span").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[8]/section/div[13]/div/table/tbody/tr/td[4]/table/tbody/tr[15]/td/span").click()
    except Exception:
        print("Ошибка: категории /www.allinform.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "your_comments")
        zz.clear()
        zz.send_keys(keysl)
    except Exception:
        print("Ошибка: keysl /www.allinform.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "your_name")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /www.allinform.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "your_spec")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /www.allinform.ru")
        pass
    
    # zz=brow.find_element(By.NAME, "org_name")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "your_address")
    # zz.clear()
    # zz.send_keys(adress)
    # zz=brow.find_element(By.XPATH, "/html/body/div[8]/section/form/div[1]/table/tbody/tr[7]/td/table/tbody/tr[3]/td[1]/input")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "your_email")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "your_url")
    # zz.clear()
    # zz.send_keys(url)
    # brow.find_element(By.XPATH, "/html/body/div[8]/section/form/div[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/span").click()
    # sleep(1)
    # brow.find_element(By.XPATH, "/html/body/div[8]/section/form/div[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/span").click()
    # sleep(1)
    # brow.find_element(By.XPATH, "/html/body/div[8]/section/div[4]/table/tbody/tr/td/table[2]/tbody/tr/td/span[9]").click()
    # sleep(1)
    # brow.find_element(By.XPATH, "/html/body/div[8]/section/form/div[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/span").click()
    # sleep(1)
    # brow.find_element(By.XPATH, "/html/body/div[8]/section/div[13]/div/table/tbody/tr/td[4]/table/tbody/tr[15]/td/span").click()
    # zz=brow.find_element(By.NAME, "your_comments")
    # zz.clear()
    # zz.send_keys(keysl)
    # zz=brow.find_element(By.NAME, "your_name")
    # zz.clear()
    # zz.send_keys(fio)
    # zz=brow.find_element(By.NAME, "your_spec")
    # zz.clear()
    # zz.send_keys(timework)