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
        if "orgsinfo" in q or "51" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://orgsinfo.ru/neworg"
    brow.get(url=w)
    # http://yndx.ru/company/registration   ---
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[1]/div/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /orgsinfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[3]/div/input")
        zz.clear()
        zz.send_keys("Наркологическая клиника – медицинское учреждение, в котором можно получить профессиональную помощь. Правильное лечение освобождает больного от тяжелой разрушающей жизнь патологии.")
    except Exception:
        print("Ошибка: desc1 /orgsinfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[4]/div/input")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /orgsinfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[5]/div/input")
        zz.clear()
        zz.send_keys("1217776689575")
    except Exception:
        print("Ошибка:  /orgsinfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[7]/div/input")
        zz.clear()
        zz.send_keys(numpl)
    except Exception:
        print("Ошибка: numpl /orgsinfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[8]/div[1]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /orgsinfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[8]/div[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail1 /orgsinfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[9]/div/textarea")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /orgsinfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[10]/div/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /orgsinfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[11]/div[1]/div/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /orgsinfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[11]/div[2]/div/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /orgsinfo.ru")
        pass
    
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[1]/div/input")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[3]/div/input")
    # zz.clear()
    # zz.send_keys("Наркологическая клиника – медицинское учреждение, в котором можно получить профессиональную помощь. Правильное лечение освобождает больного от тяжелой разрушающей жизнь патологии.")
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[4]/div/input")
    # zz.clear()
    # zz.send_keys(ciadress)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[5]/div/input")
    # zz.clear()
    # zz.send_keys("1217776689575")
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[7]/div/input")
    # zz.clear()
    # zz.send_keys(numpl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[8]/div[1]/input")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[8]/div[2]/input")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[9]/div/textarea")
    # zz.clear()
    # zz.send_keys(timework)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[10]/div/textarea")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[11]/div[1]/div/input")
    # zz.clear()
    # zz.send_keys(fio)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/div[11]/div[2]/div/input")
    # zz.clear()
    # zz.send_keys(mail)