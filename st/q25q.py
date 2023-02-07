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
        if "dbo" in q or "27" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://dbo.ru/add.html"
    brow.get(url=w)
    # https://dbo.ru/add.html   ---   1 капча
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div[1]/div[2]/form/div[1]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /dbo.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div[1]/div[2]/form/div[2]/span/span[1]/span/span[1]").click()
        zz=brow.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
        zz.send_keys(city)
        zz.send_keys(Keys.ENTER)
        brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div[1]/div[2]/form/div[3]/span/span[1]/span/span[1]").click()
        zz=brow.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
        zz.send_keys("Красота, здоровье")
        zz.send_keys(Keys.ENTER)
        brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div[1]/div[2]/form/div[4]/select/option[8]").click()
    except Exception:
        print("Ошибка: категории /dbo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div[1]/div[2]/form/div[5]/div/div[1]/input")
        zz.clear()
        zz.send_keys("100")
    except Exception:
        print("Ошибка: цена /dbo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div[1]/div[2]/form/div[6]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /dbo.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "name_from")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /dbo.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "email_from")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /dbo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div[1]/div[2]/form/div[9]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /dbo.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "url")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /dbo.ru")
        pass
    
    
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div[1]/div[2]/form/div[1]/input")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div[1]/div[2]/form/div[2]/span/span[1]/span/span[1]").click()
    # zz=brow.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
    # zz.send_keys(city)
    # zz.send_keys(Keys.ENTER)
    # brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div[1]/div[2]/form/div[3]/span/span[1]/span/span[1]").click()
    # zz=brow.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
    # zz.send_keys("Красота, здоровье")
    # zz.send_keys(Keys.ENTER)
    # brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div[1]/div[2]/form/div[4]/select/option[8]").click()
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div[1]/div[2]/form/div[5]/div/div[1]/input")
    # zz.clear()
    # zz.send_keys("100")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div[1]/div[2]/form/div[6]/textarea")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.NAME, "name_from")
    # zz.clear()
    # zz.send_keys(fio)
    # zz=brow.find_element(By.NAME, "email_from")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/section/div/div[1]/div[2]/form/div[9]/input")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "url")
    # zz.clear()
    # zz.send_keys(url)
