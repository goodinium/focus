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
        if "cabinet.tradedir" in q or "17" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://cabinet.tradedir.ru/users/goods/"
    brow.get(url=w)
    # print(numclshot[3:])
    #---------------------------------------------------
    # https://cabinet.tradedir.ru/users/goods/   ---   не до конца
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div/div[3]/div[2]/div[2]/form[1]/table/tbody/tr[1]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /cabinet.tradedir.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div/div[3]/div[2]/div[2]/form[1]/table/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw1 /cabinet.tradedir.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "_name")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /cabinet.tradedir.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "_fio")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /cabinet.tradedir.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "_login")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /cabinet.tradedir.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "_password")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw2 /cabinet.tradedir.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "_password2")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw3 /cabinet.tradedir.ru")
        pass
    
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div/div[3]/div[2]/div[2]/form[2]/table/tbody/tr[7]/td[2]/input[2]").click()
    except Exception:
        print("Ошибка: регистрация /cabinet.tradedir.ru")
        pass
    sleep(3)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div/div[3]/div[2]/div[2]/form/table[1]/tbody/tr[3]/td[2]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /cabinet.tradedir.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div/div[3]/div[2]/div[2]/form/table[2]/tbody/tr[4]/td[2]/input")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /cabinet.tradedir.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"_street\"]")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /cabinet.tradedir.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"_house\"]")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /cabinet.tradedir.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"_ph_1\"]")
        zz.clear()
        zz.send_keys("7")
        zz=brow.find_element(By.XPATH, "//*[@id=\"_ph_2\"]")
        zz.clear()
        zz.send_keys(numcodcity)
        zz=brow.find_element(By.XPATH, "//*[@id=\"_ph_3\"]")
        zz.clear()
        zz.send_keys(numclshot)
    except Exception:
        print("Ошибка: numclshot /cabinet.tradedir.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div/div[3]/div[2]/div[2]/form/table[2]/tbody/tr[10]/td[2]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: passw3 /cabinet.tradedir.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div/div[3]/div[2]/div[2]/form/table[3]/tbody/tr[1]/td[2]/select/option[59]").click()
        brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div/div[3]/div[2]/div[2]/form/table[3]/tbody/tr[2]/td[2]/select/option[5]").click()
    except Exception:
        print("Ошибка: категория /cabinet.tradedir.ru")
        pass