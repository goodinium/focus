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
        if "https://xn--h1alffa9f.xn--80abbembcyvesfij3at4loa4ff.xn--p1ai" in q or "3" in q or "россия.бесплатныеобъявления.рф" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://xn--h1alffa9f.xn--80abbembcyvesfij3at4loa4ff.xn--p1ai/podat"
    brow.get(url=w)
#--------------------------------------------------- 
# https://xn--h1alffa9f.xn--80abbembcyvesfij3at4loa4ff.xn--p1ai/podat   --- 2 капча и гуглкапча
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/form/table[1]/tbody/tr[1]/td[2]/select/option[15]").click()
        brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/form/table[1]/tbody/tr[2]/td[2]/select/option[13]").click()
    except Exception:
        print("Ошибка: категории /россия.бесплатныеобъявления.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/form/table[1]/tbody/tr[6]/td[2]/div[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /россия.бесплатныеобъявления.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/form/table[1]/tbody/tr[7]/td[2]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /россия.бесплатныеобъявления.рф")
        pass
    try:
        zz=brow.find_element(By.NAME, "Price")
        zz.clear()
        zz.send_keys("100")
    except Exception:
        print("Ошибка: цена /россия.бесплатныеобъявления.рф")
        pass
    try:
        # sleep(1)
        # brow.find_element(By.XPATH, f"//*[@id=\"CitySelectorId\"]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div[2]/div[1]/div/form/table[1]/tbody/tr[9]/td[2]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /россия.бесплатныеобъявления.рф")
        pass
    try:
        zz=brow.find_element(By.NAME, "Url")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /россия.бесплатныеобъявления.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/form/table[2]/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /россия.бесплатныеобъявления.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/form/table[2]/tbody/tr[3]/td[2]/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw1 /россия.бесплатныеобъявления.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/form/table[2]/tbody/tr[4]/td[2]/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw2 /россия.бесплатныеобъявления.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/form/table[2]/tbody/tr[5]/td[2]/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /россия.бесплатныеобъявления.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/form/table[2]/tbody/tr[6]/td[2]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /россия.бесплатныеобъявления.рф")
        pass
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/form/table[1]/tbody/tr[1]/td[2]/select/option[15]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/form/table[1]/tbody/tr[2]/td[2]/select/option[13]").click()
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/form/table[1]/tbody/tr[6]/td[2]/div[2]/input")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/form/table[1]/tbody/tr[7]/td[2]/textarea")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.NAME, "Price")
    # zz.clear()
    # zz.send_keys("100")
    # zz=brow.find_element(By.NAME, "Url")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/form/table[2]/tbody/tr[2]/td[2]/input")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/form/table[2]/tbody/tr[3]/td[2]/input")
    # zz.clear()
    # zz.send_keys(passw)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/form/table[2]/tbody/tr[4]/td[2]/input")
    # zz.clear()
    # zz.send_keys(passw)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/form/table[2]/tbody/tr[5]/td[2]/input")
    # zz.clear()
    # zz.send_keys(fio)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/form/table[2]/tbody/tr[6]/td[2]/input")
    # zz.clear()
    # zz.send_keys(numclinic)