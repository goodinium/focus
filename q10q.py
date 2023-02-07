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
    sleep(1)
    wwww=notwww.split("\n")
    for q in wwww:
        if "123ru" in q or "13" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://123ru.market/blok/add.php"
    brow.get(url=w)
    sleep(3)
    # https://123ru.market/blok/add.php   --- 1 капча
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/div[1]/div[2]/div[2]/label/input").click()
        brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[6]/td[2]/div/select/option[5]").click()
        brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[7]/td[2]/div/select/option[2]").click()
        brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[11]/td/table/tbody/tr[1]/td[2]/div/select/option[6]").click()
    except Exception:
        print("Ошибка: правила /123ru.market")
        pass
    try:
        cr=cityr.split(" ")
        cr1=cr[0]
        cr2=cr[1]
        if "область" in cr2:
            cr2=cr2[:-4]
            cityr=cr1+" "+cr2+"."
        else:
            cityr=cr1+" "+cr2
        brow.find_element(By.XPATH, f"/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[1]/td[2]/div/select/option[contains(text(),'{cityr}')]").click()
        brow.find_element(By.XPATH, f"/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[2]/td[2]/div/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /123ru.market")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[11]/td/table/tbody/tr[2]/td[2]/div/div/input[1]")
        zz.clear()
        zz.send_keys("100")
    except Exception:
        print("Ошибка: цена /123ru.market")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[12]/td/div/div[2]/div/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /123ru.market")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[13]/td/div/div[2]/div/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /123ru.market")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[14]/td/div/div[2]/div/input")
        zz.clear()
        zz.send_keys(i)
    except Exception:
        print("Ошибка: i /123ru.market")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[15]/td/div/div[2]/div/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /123ru.market")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"one\"]")
        zz.click()
        zz.send_keys(numn)
    except Exception:
        print("Ошибка: numn /123ru.market")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[18]/td/div/div[2]/div/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /123ru.market")
        pass
    # brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/div[1]/div[2]/div[2]/label/input").click()
    # brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[6]/td[2]/div/select/option[5]").click()
    # brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[7]/td[2]/div/select/option[2]").click()
    # brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[11]/td/table/tbody/tr[1]/td[2]/div/select/option[6]").click()
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[11]/td/table/tbody/tr[2]/td[2]/div/div/input[1]")
    # #zz.click()
    # zz.clear()
    # zz.send_keys("100")
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[12]/td/div/div[2]/div/input")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[13]/td/div/div[2]/div/textarea")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[14]/td/div/div[2]/div/input")
    # zz.clear()
    # zz.send_keys(i)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[15]/td/div/div[2]/div/input")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "//*[@id=\"one\"]")
    # zz.click()
    # zz.send_keys(numn)
    # zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/form/table/tbody/tr[18]/td/div/div[2]/div/input")
    # zz.clear()
    # zz.send_keys(url)
