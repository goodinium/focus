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
        if "moskva.russiacatalog.ru" in q or "77" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"https://moskva.russiacatalog.ru/add/"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div[2]/div[1]/div[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /bigspr.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div[2]/div[2]/div[2]/div[1]/button/span[1]").click()
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div[2]/div[2]/div[2]/div[1]/div/div/input")
        zz.clear()
        zz.send_keys("Клиники")
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: категории /bigspr.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div[2]/div[3]/div[2]/div[1]/button/span[1]").click()
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div[2]/div[3]/div[2]/div[1]/div/div/input")
        zz.clear()
        zz.send_keys(city)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: namecl /bigspr.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div[2]/div[4]/div[2]/input")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: namecl /bigspr.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div[2]/div[5]/div[2]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: namecl /bigspr.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div[2]/div[6]/div[2]/input")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: namecl /bigspr.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div[2]/div[7]/div[2]/input")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: namecl /bigspr.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div[2]/div[8]/div[2]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: namecl /bigspr.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div[2]/div[9]/div[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: namecl /bigspr.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div[2]/div[10]/div[2]/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: namecl /bigspr.ru")
        pass
    