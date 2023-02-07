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
        if "наркологические-клиники.рф" in q or "79" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"https://xn----7sbjiaqbcaanddceiwnhb2b3a0l.xn--p1ai/kontakty"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/form/div[2]/div[1]/div/div[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /наркологические-клиники.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/form/div[2]/div[2]/div/div[2]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /наркологические-клиники.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/form/div[2]/div[3]/div/div[2]/input")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /наркологические-клиники.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/form/div[2]/div[4]/div/div[2]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /наркологические-клиники.рф")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/form/div[2]/div[5]/div/div[2]/div/label[1]/input").click()
        brow.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/form/div[2]/div[5]/div/div[2]/div/label[4]/input").click()
        brow.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/form/div[2]/div[5]/div/div[2]/div/label[5]/input").click()
    except Exception:
        print("Ошибка: keysl /наркологические-клиники.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/form/div[2]/div[6]/div/div[2]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /наркологические-клиники.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/form/div[2]/div[7]/div/div[2]/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /наркологические-клиники.рф")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/form/div[2]/div[9]/div/div[2]/div/label[1]/input").click()
        brow.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/form/div[2]/div[10]/div/div/div/label/input").click()
    except Exception:
        print("Ошибка: правила /наркологические-клиники.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/form/div[2]/div[8]/div/div[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /наркологические-клиники.рф")
        pass
    
    