import array as arr
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def goo(brow,z,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind):
    br=brow
    try:
        brow.execute_script("window.open('');")
        brow.switch_to.window(brow.window_handles[z])
        ct1(br,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
    except Exception:
        print("")
        pass

def ct1(brow,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind):
    wwww=notwww.split("\n")
    for q in wwww:
        if "spravkainform" in q or "4" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://spravkainform.ru/add"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.NAME, "mail")
        zz.clear()
        zz.send_keys(mail)  
    except Exception:
        print("Ошибка: mail /spravkainform.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "title")
        zz.clear()
        zz.send_keys(namecl)   
    except Exception:
        print("Ошибка: namecl /spravkainform.ru")
        pass
    try:
        zz=brow.find_element(By.ID, "edit-field-title-desc-und-0-value")
        zz.clear()
        zz.send_keys("Наркологическая клиника")  
    except Exception:
        print("Ошибка: сфера /spravkainform.ru")
        pass
    try:
        zz=brow.find_element(By.ID, "edit-field-urface-und-0-value")
        zz.clear()
        zz.send_keys(unamecl)   
    except Exception:
        print("Ошибка: unamecl /spravkainform.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div[1]/div[1]/div/select[1]/option[5]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div[1]/div[1]/div/select[2]/option[22]").click()
        brow.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div[1]/div[1]/input").click()
        brow.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[3]/div[1]/div/div/select[2]/option[2]").click()
    except Exception:
        print("Ошибка: категории /spravkainform.ru")
        pass
    try:
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[3]/div[1]/div/div/select[3]/option[contains(text(),'{cityr}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[3]/div[1]/div/div/select[4]/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /spravkainform.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[3]/div[2]/div/div/input")
        zz.clear()
        zz.send_keys(street)  
    except Exception:
        print("Ошибка: street /spravkainform.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[3]/div[3]/div/div/input")
        zz.clear()
        zz.send_keys(home)  
    except Exception:
        print("Ошибка: home /spravkainform.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[3]/div[5]/div/div/input")
        zz.clear()
        zz.send_keys(timework)  
    except Exception:
        print("Ошибка: timework /spravkainform.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"edit-field-phone-und-0-value\"]")
        zz.clear()
        zz.send_keys(numclinic)  
    except Exception:
        print("Ошибка: numclinic /spravkainform.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"edit-field-mail-und-0-email\"]")
        zz.clear()
        zz.send_keys(mail)  
    except Exception:
        print("Ошибка: mail /spravkainform.ru")
        pass
    # try:
    #     zz=brow.find_element(By.XPATH, "/htm/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[4]/div[2]/div/div/table[2]/tbody/tr/td[2]/div/div/input")
    #     zz.clear()
    #     zz.send_keys(mail)  
    # except Exception:
    #     print("Ошибка: mail2 /spravkainform.ru")
    #     pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[4]/div[3]/div/div/table[2]/tbody/tr/td[2]/div/input")
        zz.clear()
        zz.send_keys(url[:-1])
        # brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[2]/div[3]/select/option[text()='{}']".format(str(city))).click()  
    except Exception:
        print("Ошибка: url /spravkainform.ru")
        pass
    # brow.get(url=w)
    # zz=brow.find_element(By.NAME, "mail")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "title")
    # zz.clear()
    # zz.send_keys(namecl) 
    # zz=brow.find_element(By.ID, "edit-field-title-desc-und-0-value")
    # zz.clear()
    # zz.send_keys("Наркологическая клиника")
    # zz=brow.find_element(By.ID, "edit-field-urface-und-0-value")
    # zz.clear()
    # zz.send_keys(unamecl) 
    # brow.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div[1]/div[1]/div/select[1]/option[5]").click()
    # sleep(1)
    # brow.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div[1]/div[1]/div/select[2]/option[22]").click()
    # brow.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div[1]/div[1]/input").click()
    # brow.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[3]/div[1]/div/div/select[2]/option[2]").click()
    # zz=brow.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[3]/div[2]/div/div/input")
    # zz.clear()
    # zz.send_keys(street)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[3]/div[3]/div/div/input")
    # zz.clear()
    # zz.send_keys(home)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[3]/div[5]/div/div/input")
    # zz.clear()
    # zz.send_keys(timework)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[4]/div[2]/div/div/table[2]/tbody/tr/td[2]/div/div/input")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div/div[4]/div[3]/div/div/table[2]/tbody/tr/td[2]/div/input")
    # zz.clear()
    # zz.send_keys(url)