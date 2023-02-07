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
        if "fis" in q or "50" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://fis.ru/reg?linkid=topgreen"
    brow.get(url=w)
    # http://yndx.ru/company/registration   ---51
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[2]/form/table/tbody/tr[1]/td[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /fis.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[2]/div[4]/div[1]/div[2]/form/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[2]/div/select/option[contains(text(),'{city}')]").click()

    except Exception:
        print("Ошибка: xp /fis.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[2]/form/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[3]/input")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /fis.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[2]/form/table/tbody/tr[3]/td[2]/div/div/input[1]")
        zz.clear()
        zz.send_keys("7")
    except Exception:
        print("Ошибка: 7 /fis.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[2]/form/table/tbody/tr[3]/td[2]/div/div/input[2]")
        zz.clear()
        zz.send_keys(numcodcity)
    except Exception:
        print("Ошибка: numcodcity /fis.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[2]/form/table/tbody/tr[3]/td[2]/div/div/input[3]")
        zz.clear()
        zz.send_keys(numclshot)
    except Exception:
        print("Ошибка: numclshot /fis.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[2]/form/table/tbody/tr[4]/td[2]/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /fis.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /fis.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[2]/form/table/tbody/tr[6]/td[2]/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw /fis.ru")
        pass
    
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[2]/form/table/tbody/tr[1]/td[2]/input")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[2]/form/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[3]/input")
    # zz.clear()
    # zz.send_keys(adress)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[2]/form/table/tbody/tr[3]/td[2]/div/div/input[1]")
    # zz.clear()
    # zz.send_keys("7")
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[2]/form/table/tbody/tr[3]/td[2]/div/div/input[2]")
    # zz.clear()
    # zz.send_keys(numcodcity)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[2]/form/table/tbody/tr[3]/td[2]/div/div/input[3]")
    # zz.clear()
    # zz.send_keys(numclshot)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[2]/form/table/tbody/tr[4]/td[2]/input")
    # zz.clear()
    # zz.send_keys(fio)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/input")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[2]/form/table/tbody/tr[6]/td[2]/input")
    # zz.clear()
    # zz.send_keys(passw)