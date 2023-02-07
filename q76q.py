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
        if "russiacompany.ru" in q or "76" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"http://www.russiacompany.ru/index.php?m=8"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div[1]/form/div[1]/input")
        zz.clear()
        zz.send_keys("00")
    except Exception:
        print("Ошибка: namecl /www.russiacompany.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[3]/div/div[1]/div[1]/form/div[2]/select/option[contains(text(),'{cityr}')]").click()
    except Exception:
        print("Ошибка: cityr /www.russiacompany.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div[1]/form/div[3]/select/option[8]").click()
        brow.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div[1]/form/div[4]/div[1]/button").click()
    except Exception:
        print("Ошибка: категории /www.russiacompany.ru")
        pass
    sleep(2)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div[1]/form/div[1]/input")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: namecl /www.russiacompany.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div[1]/form/div[2]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: namecl /www.russiacompany.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div[1]/form/div[3]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: namecl /www.russiacompany.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div[1]/form/div[4]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: namecl /www.russiacompany.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div[1]/form/div[5]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: namecl /www.russiacompany.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div[1]/form/div[7]/input")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: namecl /www.russiacompany.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div[1]/form/div[9]/select/option[40]").click()
    except Exception:
        print("Ошибка: namecl /www.russiacompany.ru")
        pass
   