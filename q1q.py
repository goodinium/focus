
    
    # zz=brow.find_element(By.NAME, "title")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "offical_name")
    # zz.clear()
    # zz.send_keys(unamecl)
    # zz=brow.find_element(By.NAME, "offical_name")
    # zz.clear()
    # zz.send_keys(unamecl)
    # zz=brow.find_element(By.NAME, "body")
    # zz.clear()
    # zz.send_keys(desc)
    # brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[5]/div/div[1]/div[1]/div/select[1]/option[7]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[5]/div/div[1]/div[1]/div/select[2]/option[17]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[5]/div/div[1]/div[1]/input").click()
    # zz=brow.find_element(By.CLASS_NAME, "tag-edit")
    # zz.send_keys(keysl)
    # sleep(2)
    # zz.send_keys(Keys.ENTER)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[2]/div[2]/div/input")
    # zz.clear()
    # zz.send_keys(ind)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[2]/div[4]/div/input")
    # zz.clear()
    # zz.send_keys(street)    
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[2]/div[5]/div/input")
    # zz.clear()
    # zz.send_keys(home)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[3]/div[1]/div[1]/input")
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[3]/div[2]/div[1]/input")
    # zz.send_keys(url)
    # print(url)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[3]/div[4]/div[1]/input")
    # zz.send_keys(mail)          
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[4]/div/input")
    # zz.send_keys(timework)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/fieldset/div[1]/div[2]/div[1]/input")
    # zz.send_keys(fio)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/fieldset/div[1]/div[2]/div[2]/input")
    # zz.clear()
    # zz.send_keys("Менеджер")    
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/fieldset/div[1]/div[2]/div[3]/input")
    # zz.clear()
    # zz.send_keys(mail)  
    # sleep(2)    
    # brow.find_element(By.ID, "persinfo").click()
    # brow.find_element(By.ID, "edit-field-terms-value").click()
    
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
    sleep(5)
    wwww=notwww.split("\n")
    for q in wwww:
        if "spravochnik.city" in q or "16" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://spravochnik.city/add"
    brow.get(url=w)
    #---------------------------------------------------  
    # https://spravochnik.city/add   ---
    sleep(8)
    try:
        zz=brow.find_element(By.NAME, "FirmForm[name]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /spravochnik.city")
        pass
    try:
        zz=brow.find_element(By.NAME, "FirmForm[subtitle]")
        zz.clear()
        zz.send_keys("Наркологическая клиника")
    except Exception:
        print("Ошибка: сфера /spravochnik.city")
        pass
    try:
        zz=brow.find_element(By.NAME, "FirmForm[official_name]")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /spravochnik.city")
        pass
    try:
        zz=brow.find_element(By.NAME, "FirmForm[description]")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /spravochnik.city")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div/main/div/div/form/div[1]/div[5]/select/option[9]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div/main/div/div/form/div[1]/div[5]/div[1]/select[1]/option[71]").click()
        brow.find_element(By.XPATH, "/html/body/div/main/div/div/form/div[1]/div[5]/button").click()
    except Exception:
        print("Ошибка: категории /spravochnik.city")
        pass
    try:
        zz=brow.find_element(By.NAME, "FirmForm[relations]")
        zz.clear()
        zz.send_keys(keysl)
    except Exception:
        print("Ошибка: keysl /spravochnik.city")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div/main/div/div/form/div[2]/div[1]/select/option[contains(text(),'{cityr}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div/main/div/div/form/div[2]/div[2]/div[1]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /spravochnik.city")
        pass
    try:
        zz=brow.find_element(By.NAME, "FirmForm[postal]")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /spravochnik.city")
        pass
    try:
        zz=brow.find_element(By.NAME, "FirmForm[street]")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /spravochnik.city")
        pass
    try:
        zz=brow.find_element(By.NAME, "FirmForm[home]")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /spravochnik.city")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/main/div/div/form/div[3]/div[1]/div[1]/table/tbody/tr/td[1]/div/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /spravochnik.city")
        pass
    try:
        zz=brow.find_element(By.NAME, "FirmForm[emails][0]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /spravochnik.city")
        pass
    try:
        zz=brow.find_element(By.NAME, "FirmForm[sites][0]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /spravochnik.city")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/main/div/div/form/div[4]/div[1]/div/div[1]/div/div[1]/input")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.XPATH, "/html/body/div/main/div/div/form/div[4]/div[1]/div/div[1]/div/div[2]/input")
        zz.clear()
        zz.send_keys("23:30")
    except Exception:
        print("Ошибка: timework /spravochnik.city")
        pass
    try:
        zz=brow.find_element(By.NAME, "User[email]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /spravochnik.city")
        pass
    try:
        zz=brow.find_element(By.NAME, "User[pass1]")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw1 /spravochnik.city")
        pass
    try:
        zz=brow.find_element(By.NAME, "User[pass2]")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw2 /spravochnik.city")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div/main/div/div/form/div[5]/div[4]/label/input").click()
        brow.find_element(By.XPATH, "/html/body/div/main/div/div/form/div[5]/div[5]/label/input").click()
    except Exception:
        print("Ошибка: правила /spravochnik.city")
        pass
    # zz=brow.find_element(By.NAME, "FirmForm[name]")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "FirmForm[subtitle]")
    # zz.clear()
    # zz.send_keys("Наркологическая клиника")
    # zz=brow.find_element(By.NAME, "FirmForm[official_name]")
    # zz.clear()
    # zz.send_keys(unamecl)
    # zz=brow.find_element(By.NAME, "FirmForm[description]")
    # zz.clear()
    # zz.send_keys(desc)
    # brow.find_element(By.XPATH, "/html/body/div/main/div/div/form/div[1]/div[5]/select/option[9]").click()
    # sleep(1)
    # brow.find_element(By.XPATH, "/html/body/div/main/div/div/form/div[1]/div[5]/div[1]/select[1]/option[71]").click()
    # brow.find_element(By.XPATH, "/html/body/div/main/div/div/form/div[1]/div[5]/button").click()
    # zz=brow.find_element(By.NAME, "FirmForm[relations]")
    # zz.clear()
    # zz.send_keys(keysl)
    # zz=brow.find_element(By.NAME, "FirmForm[postal]")
    # zz.clear()
    # zz.send_keys(ind)
    # zz=brow.find_element(By.NAME, "FirmForm[street]")
    # zz.clear()
    # zz.send_keys(street)
    # zz=brow.find_element(By.NAME, "FirmForm[home]")
    # zz.clear()
    # zz.send_keys(home)
    # zz=brow.find_element(By.XPATH, "/html/body/div/main/div/div/form/div[3]/div[1]/div[1]/table/tbody/tr/td[1]/div/input")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "FirmForm[emails][0]")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "FirmForm[sites][0]")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.XPATH, "/html/body/div/main/div/div/form/div[4]/div[1]/div/div[1]/div/div[1]/input")
    # zz.clear()
    # zz.send_keys("00:00")
    # zz=brow.find_element(By.XPATH, "/html/body/div/main/div/div/form/div[4]/div[1]/div/div[1]/div/div[2]/input")
    # zz.clear()
    # zz.send_keys("23:30")
    # zz=brow.find_element(By.NAME, "User[email]")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "User[pass1]")
    # zz.clear()
    # zz.send_keys(passw)
    # zz=brow.find_element(By.NAME, "User[pass2]")
    # zz.clear()
    # zz.send_keys(passw)
    # brow.find_element(By.XPATH, "/html/body/div/main/div/div/form/div[5]/div[4]/label/input").click()
    # brow.find_element(By.XPATH, "/html/body/div/main/div/div/form/div[5]/div[5]/label/input").click()