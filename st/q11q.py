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
        if "topserver" in q or "46" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://topserver.ru/post_info.php?category_id=200&sel_city_id=124"
    brow.get(url=w)
    # http://yndx.ru/company/registration   ---
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[5]/form/table[1]/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /topserver.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[5]/form/table[1]/tbody/tr[3]/td[2]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /topserver.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[5]/form/table[2]/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /topserver.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[5]/form/table[2]/tbody/tr[3]/td[2]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /topserver.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[5]/form/table[2]/tbody/tr[4]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /topserver.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[5]/form/table[2]/tbody/tr[6]/td[2]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /topserver.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[5]/form/table[2]/tbody/tr[7]/td[2]/input")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /topserver.ru")
        pass
    
    # zz=brow.find_element(By.XPATH, "/html/body/div/div[5]/form/table[1]/tbody/tr[2]/td[2]/input")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div[5]/form/table[1]/tbody/tr[3]/td[2]/textarea")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div[5]/form/table[2]/tbody/tr[2]/td[2]/input")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div[5]/form/table[2]/tbody/tr[3]/td[2]/input")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div[5]/form/table[2]/tbody/tr[4]/td[2]/input")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div[5]/form/table[2]/tbody/tr[6]/td[2]/input")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div[5]/form/table[2]/tbody/tr[7]/td[2]/input")
    # zz.clear()
    # zz.send_keys(adress)