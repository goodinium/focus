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
        if "narkologicheskie-kliniki" in q or "31" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://narkologicheskie-kliniki.com/dobavit-uchrezhdenie"
    brow.get(url=w)
    # https://feech.org/new-company   ---  
    try:
        zz=brow.find_element(By.NAME, "nazvanie_uchrezhdenija")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /narkologicheskie-kliniki.com")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/div/div/form/div[2]/div[2]/div/div[2]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /narkologicheskie-kliniki.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "adres")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: adress /narkologicheskie-kliniki.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "oficialnyjj_sajjt")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /narkologicheskie-kliniki.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "god_osnovanija")
        zz.clear()
        zz.send_keys("2015")
    except Exception:
        print("Ошибка: год /narkologicheskie-kliniki.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "grafik_raboty")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /narkologicheskie-kliniki.com")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/div/div/form/div[2]/div[7]/div/div[2]/div/label[1]/input").click()
        brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/div/div/form/div[2]/div[7]/div/div[2]/div/label[4]/input").click()
        brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/div/div/form/div[2]/div[7]/div/div[2]/div/label[2]/input").click()
        brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/div/div/form/div[2]/div[7]/div/div[2]/div/label[5]/input").click()
        brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/div/div/form/div[2]/div[7]/div/div[2]/div/label[6]/input").click()
    except Exception:
        print("Ошибка: категории /narkologicheskie-kliniki.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "stoimost_rubsutki")
        zz.clear()
        zz.send_keys("100")
    except Exception:
        print("Ошибка: цена /narkologicheskie-kliniki.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "kratkoe_opisanie")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /narkologicheskie-kliniki.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "vashe_imja")
        zz.clear()
        zz.send_keys(i)
    except Exception:
        print("Ошибка: i /narkologicheskie-kliniki.com")
        pass
    try:
        zz=brow.find_element(By.NAME, "vash_e-mail")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /narkologicheskie-kliniki.com")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/div/div/form/div[2]/div[12]/div/div[2]/div/label[1]/input").click()
        brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/div/div/form/div[2]/div[13]/div/div/div/label/input").click()
    except Exception:
        print("Ошибка: правила /narkologicheskie-kliniki.com")
        pass
    
    # zz=brow.find_element(By.NAME, "nazvanie_uchrezhdenija")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/div/div/form/div[2]/div[2]/div/div[2]/input")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "adres")
    # zz.clear()
    # zz.send_keys(adress)
    # zz=brow.find_element(By.NAME, "oficialnyjj_sajjt")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "god_osnovanija")
    # zz.clear()
    # zz.send_keys("2015")
    # zz=brow.find_element(By.NAME, "grafik_raboty")
    # zz.clear()
    # zz.send_keys(timework)
    # brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/div/div/form/div[2]/div[7]/div/div[2]/div/label[1]/input").click()
    # brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/div/div/form/div[2]/div[7]/div/div[2]/div/label[4]/input").click()
    # brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/div/div/form/div[2]/div[7]/div/div[2]/div/label[2]/input").click()
    # brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/div/div/form/div[2]/div[7]/div/div[2]/div/label[5]/input").click()
    # brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/div/div/form/div[2]/div[7]/div/div[2]/div/label[6]/input").click()
    # zz=brow.find_element(By.NAME, "stoimost_rubsutki")
    # zz.clear()
    # zz.send_keys("100")
    # zz=brow.find_element(By.NAME, "kratkoe_opisanie")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.NAME, "vashe_imja")
    # zz.clear()
    # zz.send_keys(i)
    # zz=brow.find_element(By.NAME, "vash_e-mail")
    # zz.clear()
    # zz.send_keys(mail)
    # brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/div/div/form/div[2]/div[12]/div/div[2]/div/label[1]/input").click()
    # brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/div/div/form/div[2]/div[13]/div/div/div/label/input").click()
