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
        if "doski" in q or "28" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://www.doski.ru/post.php#"
    brow.get(url=w)
    # https://www.doski.ru/post.php#   ---
    try:
        brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[1]/td[2]/a").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[1]/div/table/tbody/tr[2]/td[1]/table/tbody/tr[8]/td").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[8]/td").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[5]/td[2]/span/input[2]").click()
        zz=brow.find_element(By.XPATH, "//*[@id=\"ptp2\"]")
        zz.click()
    except Exception:
        print("Ошибка: категории /www.doski.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "cname")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /www.doski.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "name")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /www.doski.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "mail")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /www.doski.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "phone")
        zz.clear()
        zz.send_keys(numn)
    except Exception:
        print("Ошибка: numn /www.doski.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "sbj")
        zz.clear()
        zz.send_keys("Наркологическая клиника Течение – медицинское учреждение.")
    except Exception:
        print("Ошибка: sbj /www.doski.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "txt")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /www.doski.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[12]/td[2]/span[1]/input[2]")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /www.doski.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "price")
        zz.clear()
        zz.send_keys("100")
    except Exception:
        print("Ошибка: цена /www.doski.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "pas")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw /www.doski.ru")
        pass
    
    # brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[1]/td[2]/a").click()
    # sleep(1)
    # brow.find_element(By.XPATH, "/html/body/div[1]/div/table/tbody/tr[2]/td[1]/table/tbody/tr[8]/td").click()
    # sleep(1)
    # brow.find_element(By.XPATH, "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[8]/td").click()
    # sleep(1)
    # brow.find_element(By.XPATH, "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td").click()
    # sleep(1)
    # brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[5]/td[2]/span/input[2]").click()
    # zz=brow.find_element(By.XPATH, "//*[@id=\"ptp2\"]")
    # zz.click()
    # zz=brow.find_element(By.NAME, "cname")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "name")
    # zz.clear()
    # zz.send_keys(fio)
    # zz=brow.find_element(By.NAME, "mail")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "phone")
    # zz.clear()
    # zz.send_keys(numn)
    # zz=brow.find_element(By.NAME, "sbj")
    # zz.clear()
    # zz.send_keys("Наркологическая клиника Течение – медицинское учреждение.")
    # zz=brow.find_element(By.NAME, "txt")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[12]/td[2]/span[1]/input[2]")
    # zz.clear()
    # zz.send_keys(adress)
    # zz=brow.find_element(By.NAME, "price")
    # zz.clear()
    # zz.send_keys("100")
    # zz=brow.find_element(By.NAME, "pas")
    # zz.clear()
    # zz.send_keys(passw)
