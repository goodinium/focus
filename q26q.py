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
        if "mycompany" in q or "54" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://mycompany.su/add"
    brow.get(url=w)
    # http://yndx.ru/company/registration   ---
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[1]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /mycompany.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[2]/input")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /mycompany.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[3]/input")
        zz.clear()
        zz.send_keys("Наркологическая клиника Течение – медицинское учреждение, в котором можно получить профессиональную помощь. Правильное лечение освобождает больного от тяжелой разрушающей жизнь патологии.")
    except Exception:
        print("Ошибка: desc1 /mycompany.su")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/div[5]/select/option[contains(text(),'{cityr}')]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/div[6]/div[1]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /mycompany.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[4]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /mycompany.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"firm-postal\"]")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /mycompany.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[8]/input")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /mycompany.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[9]/input")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /mycompany.su")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[11]/select/option[22]").click()
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[11]/div[1]/select/option[31]").click()
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[11]/button").click()
    except Exception:
        print("Ошибка: категории /mycompany.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[12]/div[2]/div[1]/div")
        zz.clear()
        zz.send_keys(keysl)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: keysl /mycompany.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[13]/div[1]/table/tbody/tr/td[1]/div/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /mycompany.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[16]/div[1]/table/tbody/tr/td[1]/div/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /mycompany.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[17]/div[1]/table/tbody/tr/td[1]/div/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /mycompany.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[1]/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys("0:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[1]/div[2]/div[2]/input")
        zz.clear()
        zz.send_keys("23:30")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[2]/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys("0:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[2]/div[2]/div[2]/input")
        zz.clear()
        zz.send_keys("23:30")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[3]/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys("0:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[3]/div[2]/div[2]/input")
        zz.clear()
        zz.send_keys("23:30")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[4]/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys("0:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[4]/div[2]/div[2]/input")
        zz.clear()
        zz.send_keys("23:30")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[5]/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys("0:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[5]/div[2]/div[2]/input")
        zz.clear()
        zz.send_keys("23:30")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[6]/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys("0:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[6]/div[2]/div[2]/input")
        zz.clear()
        zz.send_keys("23:30")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[7]/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys("0:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[7]/div[2]/div[2]/input")
        zz.clear()
        zz.send_keys("23:30")
    except Exception:
        print("Ошибка: timework /mycompany.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[20]/div[1]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /mycompany.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[20]/div[2]/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw1 /mycompany.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[20]/div[3]/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw2 /mycompany.su")
        pass
    
    
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[1]/input")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[2]/input")
    # zz.clear()
    # zz.send_keys(unamecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[3]/input")
    # zz.clear()
    # zz.send_keys("Наркологическая клиника Течение – медицинское учреждение, в котором можно получить профессиональную помощь. Правильное лечение освобождает больного от тяжелой разрушающей жизнь патологии.")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[4]/textarea")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.XPATH, "//*[@id=\"firm-postal\"]")
    # zz.clear()
    # zz.send_keys(ind)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[8]/input")
    # zz.clear()
    # zz.send_keys(street)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[9]/input")
    # zz.clear()
    # zz.send_keys(home)
    # brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[11]/select/option[22]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[11]/div[1]/select/option[31]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[11]/button").click()
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[12]/div[2]/div[1]/div")
    # zz.clear()
    # zz.send_keys(keysl)
    # zz.send_keys(Keys.ENTER)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[13]/div[1]/table/tbody/tr/td[1]/div/input")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[16]/div[1]/table/tbody/tr/td[1]/div/input")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[17]/div[1]/table/tbody/tr/td[1]/div/input")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[1]/div[2]/div[1]/input")
    # zz.clear()
    # zz.send_keys("0:00")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[1]/div[2]/div[2]/input")
    # zz.clear()
    # zz.send_keys("23:30")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[2]/div[2]/div[1]/input")
    # zz.clear()
    # zz.send_keys("0:00")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[2]/div[2]/div[2]/input")
    # zz.clear()
    # zz.send_keys("23:30")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[3]/div[2]/div[1]/input")
    # zz.clear()
    # zz.send_keys("0:00")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[3]/div[2]/div[2]/input")
    # zz.clear()
    # zz.send_keys("23:30")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[4]/div[2]/div[1]/input")
    # zz.clear()
    # zz.send_keys("0:00")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[4]/div[2]/div[2]/input")
    # zz.clear()
    # zz.send_keys("23:30")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[5]/div[2]/div[1]/input")
    # zz.clear()
    # zz.send_keys("0:00")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[5]/div[2]/div[2]/input")
    # zz.clear()
    # zz.send_keys("23:30")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[6]/div[2]/div[1]/input")
    # zz.clear()
    # zz.send_keys("0:00")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[6]/div[2]/div[2]/input")
    # zz.clear()
    # zz.send_keys("23:30")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[7]/div[2]/div[1]/input")
    # zz.clear()
    # zz.send_keys("0:00")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[19]/div[7]/div[2]/div[2]/input")
    # zz.clear()
    # zz.send_keys("23:30")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[20]/div[1]/input")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[20]/div[2]/input")
    # zz.clear()
    # zz.send_keys(passw)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[20]/div[3]/input")
    # zz.clear()
    # zz.send_keys(passw)