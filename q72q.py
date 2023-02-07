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
    cit=city
    for q in wwww:
        if "gmstar.ru" in q or "72" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"http://gmstar.ru/reg/company/"
    brow.get(url=w)
    try:
        brow.find_element(By.XPATH, f"/html/body/div[2]/div/div[1]/div/form/div[11]/select/option[contains(text(),'{cityr}')]").click()
    except Exception:
        print("Ошибка: xp /gmstar.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/form/div[1]/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: namecl /gmstar.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/form/div[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: namecl /gmstar.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/form/div[3]/input")
        zz.clear()
        zz.send_keys("Менеджер")
    except Exception:
        print("Ошибка: namecl /gmstar.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/form/div[4]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /gmstar.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/form/div[5]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: namecl /gmstar.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/form/div[6]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: namecl /gmstar.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/form/div[7]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: namecl /gmstar.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/form/div[8]/textarea")
        zz.clear()
        zz.send_keys(keysl)
    except Exception:
        print("Ошибка: namecl /gmstar.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/form/div[9]/input[1]")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: namecl /gmstar.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/form/div[12]/input")
        zz.clear()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: namecl /gmstar.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/form/div[13]/input")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: namecl /gmstar.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/form/div[14]/input[1]")
        zz.clear()
        zz.send_keys(numcodcity)
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/form/div[14]/input[2]")
        zz.clear()
        zz.send_keys(numclshot)
    except Exception:
        print("Ошибка: namecl /gmstar.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/form/div[21]/div/span/input[1]").click()
    except Exception:
        print("Ошибка: namecl /gmstar.ru")
        pass
    