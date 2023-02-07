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
        if "1000dosok" in q or "42" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://1000dosok.ru/doski.php?r=1005"
    brow.get(url=w)
    # http://yndx.ru/company/registration   ---
    try:
        brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/noindex/form/table/tbody/tr[1]/td[2]/select/option[8]").click()
        brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/noindex/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/input").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/form/div[2]/span/select/option[2]").click()
    except Exception:
        print("Ошибка: категории /1000dosok.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/form/div[3]/span/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /1000dosok.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/form/div[4]/span/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: категории /1000dosok.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/form/div[5]/span/input[1]")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /1000dosok.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/form/div[6]/span/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /1000dosok.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/form/div[8]/span/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /1000dosok.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/form/div[9]/font/span/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /1000dosok.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/form/div[10]/span/font[1]/input")
        zz.clear()
        zz.send_keys("99")
    except Exception:
        print("Ошибка: цена /1000dosok.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/form/div[11]/span/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /1000dosok.ru")
        pass
    
    # brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/noindex/form/table/tbody/tr[1]/td[2]/select/option[8]").click()
    # brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/noindex/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/input").click()
    # sleep(1)
    # brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/form/div[2]/span/select/option[2]").click()
    # zz=brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/form/div[3]/span/input")
    # zz.clear()
    # zz.send_keys(fio)
    # zz=brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/form/div[5]/span/input[1]")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/form/div[6]/span/input")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/form/div[8]/span/input")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/form/div[9]/font/span/input")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/form/div[10]/span/font[1]/input")
    # zz.clear()
    # zz.send_keys("99")
    # zz=brow.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/form/div[11]/span/textarea")
    # zz.clear()
    # zz.send_keys(desc)
    