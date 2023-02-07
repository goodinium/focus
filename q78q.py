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
        if "bigspravka.ru" in q or "78" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"https://bigspravka.ru/addorg/"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div/form/input[2]")
        zz.clear()
        zz.send_keys(i+" "+o)
    except Exception:
        print("Ошибка: i+o /bigspravka.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div/form/input[3]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /bigspravka.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div/form/input[4]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /bigspravka.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div/form/input[5]")
        zz.clear()
        zz.send_keys(cityr+", "+city+", "+street+", "+home)
    except Exception:
        print("Ошибка: adres /bigspravka.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div/form/input[6]")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /bigspravka.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div/form/input[7]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /bigspravka.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div/form/textarea[1]")
        zz.clear()
        zz.send_keys(keysl)
    except Exception:
        print("Ошибка: keysl /bigspravka.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div/form/textarea[2]")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /bigspravka.ru")
        pass
    
   

    