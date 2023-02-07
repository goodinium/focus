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
        if "rydo" in q or "4" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://rydo.ru/podat-obyavlenie/"
    brow.get(url=w)
    #---------------------------------------------------
    # https://dbo.ru/add.html   ---
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/form/div[1]/div[2]/span").click()
        sleep(1)
        e=brow.find_element(By.CLASS_NAME, "location_select")
        e1=e.find_element(By.PARTIAL_LINK_TEXT, ob).click()
    except Exception:
        print("Ошибка: город /rydo.ru")
        pass
    try:
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/form/div[2]/div[2]/div/ul[2]/li[4]/a").click()
        brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/form/div[2]/div[2]/div/ul[2]/li[16]/a").click()
        brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/form/div[2]/div[2]/div/ul[2]/li[6]/a").click()
    except Exception:
        print("Ошибка: категории /rydo.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "title")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /rydo.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "info")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /rydo.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "price")
        zz.clear()
        zz.send_keys("100")
    except Exception:
        print("Ошибка: цена /rydo.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "contact_phone")
        zz.clear()
        zz.send_keys(numn)
    except Exception:
        print("Ошибка: numn /rydo.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "contact_email")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /rydo.ru")
        pass
    # brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/form/div[1]/div[2]/span").click()
    # sleep(1)
    # e=brow.find_element(By.CLASS_NAME, "location_select")
    # e1=e.find_element(By.PARTIAL_LINK_TEXT, ob).click()
    # # brow.find_element(By.LINK_TEXT, ci).click()
    # sleep(1)
    # brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/form/div[2]/div[2]/div/ul[2]/li[4]/a").click()
    # brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/form/div[2]/div[2]/div/ul[2]/li[16]/a").click()
    # brow.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/form/div[2]/div[2]/div/ul[2]/li[6]/a").click()
    # zz=brow.find_element(By.NAME, "title")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "info")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.NAME, "price")
    # zz.clear()
    # zz.send_keys("100")
    # zz=brow.find_element(By.NAME, "contact_phone")
    # zz.clear()
    # zz.send_keys(numn)
    # zz=brow.find_element(By.NAME, "contact_email")
    # zz.clear()
    # zz.send_keys(mail)
