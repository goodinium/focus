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
        if "ot-boli.ru" in q or "70" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"https://ot-boli.ru/%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C_%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D0%BA%D1%83"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/table/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /ot-boli.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/table/tbody/tr[4]/td[2]/span/span[1]/span/span[1]").click()
        zz=brow.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
        zz.clear()
        zz.send_keys(cityr)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: cityr /ot-boli.ru")
        pass
    sleep(2)
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/span/span[1]/span/span[1]").click()
        zz=brow.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
        zz.clear()
        zz.send_keys(city)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: city /ot-boli.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/table/tbody/tr[6]/td[2]/select/optgroup[1]/option[6]").click()

    except Exception:
        print("Ошибка: категории /ot-boli.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/table/tbody/tr[7]/td[2]/input")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /ot-boli.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/table/tbody/tr[8]/td[2]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /ot-boli.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/table/tbody/tr[9]/td[2]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /ot-boli.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/table/tbody/tr[13]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /ot-boli.ru")
        pass
    