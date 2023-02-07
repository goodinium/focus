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
    cit=city
    for q in wwww:
        if "spravochnikov" in q or "40" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="httru/"
    brow.get(url="http://translit-online.ru/")
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[3]/form/textarea[1]")
        # zz.clear()
        zz.click()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: переход1 /spravochnikov.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div/div[3]/form/div[2]/div/input[1]").click()
    except Exception:
        print("Ошибка: переход2 /spravochnikov.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[3]/form/textarea[2]").text
        # zz.click()
        # zz=zz.text()
        zz=zz.lower()
        print(zz)
        brow.get(url=f"https://{zz}.spravochnikov.ru/user/registration")
        # brow.find_element(By.XPATH, "/html/body/div[1]/header/div[3]/div[2]/nav/ul/li[2]/a").click()
    except Exception:
        print("Ошибка: переход3 /spravochnikov.ru")
        pass
    sleep(2)
    # try:
    #     brow.find_element(By.LINK_TEXT, city).click()
    #     sleep(2)
    #     brow.switch_to.window(brow.window_handles[z+1])
    #     ur=brow.current_url
    #     ur=ur+"user/registration"
    #     brow.switch_to.window(brow.window_handles[z])
    # except Exception:
    #     print("Ошибка: ссылки /spravochnikov.ru")
    #     pass
    # brow.get(url=ur)
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[1]/div[1]/select[1]/option[12]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[1]/div[1]/select[2]/option[39]").click()
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[1]/div[1]/button").click()
    except Exception:
        print("Ошибка: категории /spravochnikov.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[1]/div[3]/div/div[1]/div")
        zz.send_keys(keysl)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: keysl /spravochnikov.ru")
        pass
    try:
        zz=brow.find_element(By.ID, "field_spec")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /spravochnikov.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "title")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /spravochnikov.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[3]/div/form/fieldset[2]/div[3]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /spravochnikov.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[2]/div[4]/input")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /spravochnikov.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[2]/div[5]/input")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /spravochnikov.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[2]/div[8]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /spravochnikov.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[2]/div[11]/input")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /spravochnikov.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[2]/div[13]/input[1]")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /spravochnikov.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[2]/div[14]/input[1]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /spravochnikov.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[2]/fieldset/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[2]/fieldset/div[2]/div[2]/input")
        zz.clear()
        zz.send_keys("23:59")
    except Exception:
        print("Ошибка: timework /spravochnikov.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[3]/div[1]/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /spravochnikov.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[3]/div[2]/input")
        zz.clear()
        zz.send_keys("Менеджер")
    except Exception:
        print("Ошибка: Менеджер /spravochnikov.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/div[1]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /spravochnikov.ru")
        pass
    try:
        brow.find_element(By.ID, "terms").click()
        brow.find_element(By.NAME, "pesinfo").click()
    except Exception:
        print("Ошибка: правила /spravochnikov.ru")
        pass
    
    
    # brow.find_element(By.LINK_TEXT, city).click()
    # sleep(2)
    # brow.switch_to.window(brow.window_handles[z+1])
    # ur=brow.current_url
    # ur=ur+"user/registration"
    # brow.switch_to.window(brow.window_handles[z])
    # # print(ur) 
    # brow.get(url=ur)
    # brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[1]/div[1]/select[1]/option[12]").click()
    # sleep(1)
    # brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[1]/div[1]/select[2]/option[39]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[1]/div[1]/button").click()
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[1]/div[3]/div/div[1]/div")
    # #zz.click()
    # zz.send_keys(keysl)
    # zz.send_keys(Keys.ENTER)
    # zz=brow.find_element(By.ID, "field_spec")
    # zz.clear()
    # zz.send_keys(desc)
    # zz=brow.find_element(By.NAME, "title")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[2]/div[4]/input")
    # zz.clear()
    # zz.send_keys(street)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[2]/div[5]/input")
    # zz.clear()
    # zz.send_keys(home)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[2]/div[8]/input")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[2]/div[11]/input")
    # zz.clear()
    # zz.send_keys(unamecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[2]/div[13]/input[1]")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[2]/div[14]/input[1]")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[2]/fieldset/div[2]/div[1]/input")
    # zz.clear()
    # zz.send_keys("00:00")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[2]/fieldset/div[2]/div[2]/input")
    # zz.clear()
    # zz.send_keys("23:59")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[3]/div[1]/input")
    # zz.clear()
    # zz.send_keys(fio)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/fieldset[3]/div[2]/input")
    # zz.clear()
    # zz.send_keys("Менеджер")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/form/div[1]/input")
    # zz.clear()
    # zz.send_keys(mail)
    # brow.find_element(By.ID, "terms").click()
    # brow.find_element(By.NAME, "pesinfo").click()