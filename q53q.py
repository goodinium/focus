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
        if "moskva.reginforms" in q or "53" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="http://moskva.reginforms.ru/spravka/add-company.html"
    brow.get(url=w)
    # try:
    #     brow.find_element(By.XPATH, "/html/body/div/div[2]/header/div[1]/div[1]/div/span/span").click()
    #     zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/header/div[1]/div[1]/div/div/form/input")
    #     zz.click()
    #     zz.send_keys(city.lower())
    #     brow.find_element(By.XPATH, "/html/body/div/div[2]/header/div[1]/div[1]/div/div/ul").click()
    #     sleep(1)
    #     brow.find_element(By.XPATH, "/html/body/div/div[2]/footer/nav/ul/li[8]/a").click()
    # except Exception:
    #     print("Ошибка: переход1 /reginforms.ru")
    #     pass
    # sleep(1)
    # http://moskva.reginforms.ru/spravka/add-company.html   ---
    try:
        zz=brow.find_element(By.NAME, "name_firm")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /reginforms.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "type_firm")
        zz.clear()
        zz.send_keys("Наркологическая клиника")
    except Exception:
        print("Ошибка: сфера /reginforms.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "about")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /reginforms.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "working_hours")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /reginforms.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/section/article/div/div[1]/form/ul/li[5]/select/option[8]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/section/article/div/div[1]/form/ul/li[6]/ul/li[124]/nobr/input").click()
    except Exception:
        print("Ошибка: категории /reginforms.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div/div[2]/div/div[3]/section/article/div/div[1]/form/ul/li[8]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: категории /reginforms.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "address")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /reginforms.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "phone_mobile")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /reginforms.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "email_firm")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail1 /reginforms.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "site_firm")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /reginforms.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "user_mail")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /reginforms.ru")
        pass
    
    # zz=brow.find_element(By.NAME, "name_firm")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "type_firm")
    # zz.clear()
    # zz.send_keys("Наркологическая клиника")
    # zz=brow.find_element(By.NAME, "about")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.NAME, "working_hours")
    # zz.clear()
    # zz.send_keys(timework)
    # brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/section/article/div/div[1]/form/ul/li[5]/select/option[8]").click()
    # sleep(1)
    # brow.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/section/article/div/div[1]/form/ul/li[6]/ul/li[124]/nobr/input").click()
    # zz=brow.find_element(By.NAME, "address")
    # zz.clear()
    # zz.send_keys(adress)
    # zz=brow.find_element(By.NAME, "phone_mobile")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "email_firm")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "site_firm")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "user_mail")
    # zz.clear()
    # zz.send_keys(mail)