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
        if "medfirms" in q or "48" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="http://medfirms.ru/companies/?add"
    brow.get(url=w)
    try:
        brow.find_element(By.XPATH, f"/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[8]/td[2]/select/option[contains(text(),'{cityr}')]").click()

    except Exception:
        print("Ошибка: xp /medfirms.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[1]/td[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /medfirms.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys(login)
    except Exception:
        print("Ошибка: login /medfirms.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[3]/td[2]/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw /medfirms.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[4]/td[2]/table/tbody/tr/td[1]/input[17]").click()
        brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[4]/td[2]/table/tbody/tr/td[1]/input[38]").click()
    except Exception:
        print("Ошибка: категории /medfirms.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[5]/td[2]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc1 /medfirms.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[6]/td[2]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc2 /medfirms.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[7]/td[2]/textarea")
        zz.clear()
        zz.send_keys(keysl)
    except Exception:
        print("Ошибка: keysl /medfirms.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[9]/td[2]/input")
        zz.clear()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: city /medfirms.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[10]/td[2]/textarea")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /medfirms.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[11]/td[2]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /medfirms.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[13]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /medfirms.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[14]/td[2]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /medfirms.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[15]/td[2]/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /medfirms.ru")
        pass
    
    # zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[1]/td[2]/input")
    # # zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[2]/td[2]/input")
    # zz.clear()
    # zz.send_keys(login)
    # zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[3]/td[2]/input")
    # zz.clear()
    # zz.send_keys(passw)
    # brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[4]/td[2]/table/tbody/tr/td[1]/input[17]").click()
    # brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[4]/td[2]/table/tbody/tr/td[1]/input[38]").click()
    # zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[5]/td[2]/textarea")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[6]/td[2]/textarea")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[7]/td[2]/textarea")
    # zz.clear()
    # zz.send_keys(keysl)
    # zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[9]/td[2]/input")
    # zz.clear()
    # zz.send_keys(city)
    # zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[10]/td[2]/textarea")
    # zz.clear()
    # zz.send_keys(adress)
    # zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[11]/td[2]/input")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[13]/td[2]/input")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[14]/td[2]/input")
    # # zz.click()
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[15]/td[2]/input")
    # # zz.click()
    # zz.clear()
    # zz.send_keys(fio)
    
#---------------------------------------------------
    # ci=xp[41]
    # http://yndx.ru/company/registration   ---51
    # zz=brow.find_element(By.XPATH, "/html/body/div/div[1]/div/div[2]/div/form/div[1]/input")
    # zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # # brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/div/form/div[2]/select/optgroup[7]/option[36]").click()
    
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/div/form/div[3]/input")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(adress)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/div/form/div[4]/textarea")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(numcl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/div/form/div[5]/input")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/div/form/div[6]/textarea")
    # #zz.click()
    # zz.clear()
    # zz.send_keys("График работы: "+timework+"О компании: "+desc)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/div/form/div[7]/textarea")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(keysl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/div/form/div[8]/input")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(mail)
    