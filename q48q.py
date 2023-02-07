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
        if "loglink" in q or "48" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="http://www.loglink.ru/catalog/add/"
    brow.get(url=w)
    # http://www.loglink.ru/catalog/add/   ---
    try:
        zz=brow.find_element(By.NAME, "company_caption")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /www.loglink.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[6]/td[2]/select/option[2]").click()
    except Exception:
        print("Ошибка: категории /www.loglink.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "url")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /www.loglink.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "email")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /www.loglink.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "phone")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /www.loglink.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[12]/td[2]/select/option[contains(text(),'{cityr}')]").click()
    except Exception:
        print("Ошибка: xp /www.loglink.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "city")
        zz.clear()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: city1 /www.loglink.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "village")
        zz.clear()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: city2 /www.loglink.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "zip_code")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /www.loglink.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "address")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /www.loglink.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "short_description")
        zz.clear()
        zz.send_keys("Наркологическая клиника – медицинское учреждение, в котором можно получить профессиональную помощь.")
    except Exception:
        print("Ошибка: desc1 /www.loglink.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "full_description")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc2 /www.loglink.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "private_contact_face")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /www.loglink.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "private_phone")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /www.loglink.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "private_email")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /www.loglink.ru")
        pass
    
    # zz=brow.find_element(By.NAME, "company_caption")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[6]/td[2]/select/option[2]").click()
    # zz=brow.find_element(By.NAME, "url")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "email")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "phone")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "city")
    # zz.clear()
    # zz.send_keys(city)
    # zz=brow.find_element(By.NAME, "village")
    # zz.clear()
    # zz.send_keys(city)
    # zz=brow.find_element(By.NAME, "zip_code")
    # zz.clear()
    # zz.send_keys(ind)
    # zz=brow.find_element(By.NAME, "address")
    # zz.clear()
    # zz.send_keys(adress)
    # zz=brow.find_element(By.NAME, "short_description")
    # zz.clear()
    # zz.send_keys("Наркологическая клиника – медицинское учреждение, в котором можно получить профессиональную помощь.")
    # zz=brow.find_element(By.NAME, "full_description")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.NAME, "private_contact_face")
    # zz.clear()
    # zz.send_keys(fio)
    # zz=brow.find_element(By.NAME, "private_phone")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "private_email")
    # zz.clear()
    # zz.send_keys(mail)
