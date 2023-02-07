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
        if "телефонырф.рф" in q or "69" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"https://xn--e1aarjenitd2e.xn--p1ai/%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C"
    brow.get(url=w)
    try:
        brow.find_element(By.XPATH, f"/html/body/main/div[2]/div/form/div[2]/div[1]/select/option[contains(text(),'{cityr}')]").click()
        brow.find_element(By.XPATH, f"/html/body/main/div[2]/div/form/div[2]/div[2]/div[1]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /телефонырф.рф")
        pass
   
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[1]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /телефонырф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[2]/input")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: tupecl /телефонырф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[3]/input")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /телефонырф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[4]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /телефонырф.рф")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[5]/select/option[10]").click()
        brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[5]/div[1]/select/option[67]").click()
        brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[5]/button").click()
    except Exception:
        print("Ошибка: правила /телефонырф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[1]/div[6]/div[2]/div[1]/div")
        zz.clear()
        zz.send_keys(keysl)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: keysl /телефонырф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[2]/div[3]/input")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /телефонырф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[2]/div[4]/input")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /телефонырф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[2]/div[5]/input")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /телефонырф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[3]/div[1]/div[1]/table/tbody/tr/td[1]/div/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /телефонырф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[3]/div[4]/div[1]/table/tbody/tr/td[1]/div/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail1 /телефонырф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[3]/div[5]/div[1]/table/tbody/tr/td[1]/div/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /телефонырф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[4]/div/div[1]/div[2]/div[1]/input")
        zz.send_keys("")
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[4]/div/div[2]/div[2]/div[1]/input")
        zz.send_keys("")
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[4]/div/div[3]/div[2]/div[1]/input")
        zz.send_keys("")
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[4]/div/div[4]/div[2]/div[1]/input")
        zz.send_keys("")
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[4]/div/div[5]/div[2]/div[1]/input")
        zz.send_keys("")
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[4]/div/div[6]/div[2]/div[1]/input")
        zz.send_keys("")
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[4]/div/div[7]/div[2]/div[1]/input")
        zz.send_keys("")
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[4]/div/div[1]/div[2]/div[2]/input")
        zz.send_keys("")
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[4]/div/div[2]/div[2]/div[2]/input")
        zz.send_keys("")
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[4]/div/div[3]/div[2]/div[2]/input")
        zz.send_keys("")
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[4]/div/div[4]/div[2]/div[2]/input")
        zz.send_keys("")
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[4]/div/div[5]/div[2]/div[2]/input")
        zz.send_keys("")
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[4]/div/div[6]/div[2]/div[2]/input")
        zz.send_keys("")
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[4]/div/div[7]/div[2]/div[2]/input")
        zz.send_keys("")
    except Exception:
        print("Ошибка: timework /телефонырф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[5]/div[1]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /телефонырф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[5]/div[2]/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw2 /телефонырф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[5]/div[3]/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw2 /телефонырф.рф")
        pass
    sleep(3)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div[2]/div/form/div[5]/div[4]/label/input").click()
    except Exception:
        print("Ошибка: правила /телефонырф.рф")
        pass
    
    