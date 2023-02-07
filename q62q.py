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
        if "www.barahla.net" in q or "62" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"https://www.barahla.net/add"
    brow.get(url=w)
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/form/div/div/div/label[3]/span").click()
    except Exception:
        print("Ошибка: ifff /www.barahla.net")
        pass
    sleep(2)
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/form/div/div/span/div/label[4]/span").click()
    except Exception:
        print("Ошибка: ifff /www.barahla.net")
        pass
    sleep(2)
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/form/div/div/span/div[2]/label[4]/span").click()
    except Exception:
        print("Ошибка: ifff /www.barahla.net")
        pass
    sleep(2)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/form/div[2]/div[3]/span/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /www.barahla.net")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/form/div[2]/div[5]/div[3]/span/input")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /www.barahla.net")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"new_content\"]")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: ciadress /www.barahla.net")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/form/div[2]/div[9]/label[2]").click()
    except Exception:
        print("Ошибка: desc /www.barahla.net")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/form/div[2]/div[10]/div[1]/span/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /www.barahla.net")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/form/div[2]/div[10]/div[2]/span/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: ifff /www.barahla.net")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/form/div[2]/div[10]/div[3]/span/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw1 /www.barahla.net")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/form/div[2]/div[10]/div[4]/span/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw2 /www.barahla.net")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/form/div[2]/div[10]/div[5]/span/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /www.barahla.net")
        pass
    
    
    
    