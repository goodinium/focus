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
        if "firmlist.ru" in q or "33" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"https://firmlist.ru/registration"
    brow.get(url=w)
    
   
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/div/form/div[1]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /firmlist.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/div/form/div[2]/input")
        zz.clear()
        zz.send_keys(i+" "+o)
    except Exception:
        print("Ошибка: i+o /firmlist.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/div/form/div[3]/input")
        zz.clear()
        zz.send_keys(f)
    except Exception:
        print("Ошибка: f /firmlist.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/div/form/div[4]/input")
        zz.clear()
        zz.send_keys("Менеджер")
    except Exception:
        print("Ошибка: Менеджер /firmlist.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/main/div/div/form/div[5]/div[1]/div/select/option[4]").click()
        zz=brow.find_element(By.XPATH, "/html/body/main/div/div/form/div[5]/div[2]/div/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /firmlist.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/div/form/div[6]/div[1]/input")
        zz.clear()
        zz.send_keys("Наркологические клиники")
    except Exception:
        print("Ошибка: typecl /firmlist.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/div/form/div[7]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /firmlist.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/div/form/div[9]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /firmlist.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/div/form/div[10]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /firmlist.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/div/form/div[11]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /firmlist.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/div/form/div[13]/input")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /firmlist.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/div/form/div[14]/input")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /firmlist.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/div/form/div[15]/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw /firmlist.ru")
        pass
    
    