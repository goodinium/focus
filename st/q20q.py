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
        if "llike" in q or "3" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://llike.ru/add_company"
    brow.get(url=w)
    #---------------------------------------------------1 капча
    try:
        zz=brow.find_element(By.NAME, "company_name")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /llike.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/section/form/table/tbody/tr[2]/td[2]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /llike.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "post_address")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /llike.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/section/form/table/tbody/tr[4]/td[2]/div/div/input")
        zz.click()
        sleep(2)
        # zz.clear()
        zz.send_keys(numn)
    except Exception:
        print("Ошибка: numn /llike.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "company_email")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /llike.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "website")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /llike.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/section/form/table/tbody/tr[7]/td[2]/select/option[15]").click()
        sleep(1)
    except Exception:
        print("Ошибка: категории /llike.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/section/form/table/tbody/tr[8]/td[2]/div/div/div/div/iframe")
        zz.click()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /llike.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "user_name")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /llike.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "user_email")
        #zz.click()
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /llike.ru")
        pass
    # zz=brow.find_element(By.NAME, "company_name")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "post_address")
    # zz.clear()
    # zz.send_keys(adress)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/section/form/table/tbody/tr[4]/td[2]/div/div/input")
    # zz.click()
    # sleep(2)
    # zz.clear()
    # zz.send_keys(numn)
    # print(numn)
    # zz=brow.find_element(By.NAME, "company_email")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "website")
    # zz.clear()
    # zz.send_keys(url)
    # brow.find_element(By.XPATH, "/html/body/div[1]/section/form/table/tbody/tr[7]/td[2]/select/option[15]").click()
    # sleep(1)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/section/form/table/tbody/tr[8]/td[2]/div/div/div/div/iframe")
    # zz.click()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.NAME, "user_name")
    # zz.clear()
    # zz.send_keys(fio)
    # zz=brow.find_element(By.NAME, "user_email")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(mail)


