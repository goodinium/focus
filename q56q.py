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
        if "spravka.me" in q or "56" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://omsk.spravka.me/add/firm"
    # brow.get(url=w)
    brow.get(url="http://translit-online.ru/")
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[3]/form/textarea[1]")
        # zz.clear()
        zz.click()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: переход1 /spravka.me")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div/div[3]/form/div[2]/div/input[1]").click()
    except Exception:
        print("Ошибка: переход2 /spravka.me")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[3]/form/textarea[2]").text
        # zz.click()
        # zz=zz.text()
        zz=zz.lower()
        print(zz)
        brow.get(url=f"https://{zz}.spravka.me/add/firm")
        # brow.find_element(By.XPATH, "/html/body/div[1]/header/div[3]/div[2]/nav/ul/li[2]/a").click()
    except Exception:
        print("Ошибка: переход3 /spravka.me")
        pass
    sleep(2)
    # http://yndx.ru/company/registration   ---
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/select[1]/option[contains(text(),'{cityr}')]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/select[2]/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /spravka.me")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[6]/input[2]").click()
    except Exception:
        print("Ошибка: правила /spravka.me")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[1]/div[5]/div[1]/select[1]/option[8]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[1]/div[5]/div[1]/select[2]/option[193]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[1]/div[5]/div[1]/input").click()
    except Exception:
        print("Ошибка: категории /spravka.me")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[1]/div[1]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /spravka.me")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[1]/div[2]/input")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: tupecl /spravka.me")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[1]/div[3]/input")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /spravka.me")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[1]/div[4]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /spravka.me")
        pass
    
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[1]/div[6]/div[1]/input")
        zz.clear()
        zz.send_keys(keysl)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: keysl /spravka.me")
        pass
    
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"firm-postal\"]")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /spravka.me")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[2]/div[3]/input")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /spravka.me")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[2]/div[4]/input")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /spravka.me")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[3]/div[1]/input[1]")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /spravka.me")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[3]/div[2]/input[1]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /spravka.me")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[3]/div[3]/input[1]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /spravka.me")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"worktimestring\"]")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /spravka.me")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[5]/div[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /spravka.me")
        pass
    # sleep(5)
    
    
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[1]/div[1]/input")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[1]/div[2]/input")
    # zz.clear()
    # zz.send_keys(tupecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[1]/div[3]/input")
    # zz.clear()
    # zz.send_keys(unamecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[1]/div[4]/textarea")
    # zz.clear()
    # zz.send_keys(desc)
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[1]/div[5]/div[1]/select[1]/option[8]").click()
    # sleep(1)
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[1]/div[5]/div[1]/select[2]/option[193]").click()
    # sleep(1)
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[1]/div[5]/div[1]/input").click()
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[1]/div[6]/div[1]/input")
    # zz.clear()
    # zz.send_keys(keysl)
    # zz.send_keys(Keys.ENTER)
    # zz=brow.find_element(By.XPATH, "//*[@id=\"firm-postal\"]")
    # zz.clear()
    # zz.send_keys(ind)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[2]/div[3]/input")
    # zz.clear()
    # zz.send_keys(street)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[2]/div[4]/input")
    # zz.clear()
    # zz.send_keys(home)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[3]/div[1]/input[1]")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[3]/div[2]/input[1]")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[3]/div[3]/input[1]")
    # zz.clear()
    # zz.send_keys(mail)
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[4]/div[1]/div/div[2]/div[1]/div/div[2]/input[1]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[4]/div[1]/div/div[2]/div[2]/div/div[2]/input[1]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[4]/div[1]/div/div[2]/div[3]/div/div[2]/input[1]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[4]/div[1]/div/div[2]/div[4]/div/div[2]/input[1]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[4]/div[1]/div/div[2]/div[5]/div/div[2]/input[1]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[4]/div[1]/div/div[2]/div[6]/div/div[2]/input[1]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[4]/div[1]/div/div[2]/div[7]/div/div[2]/input[1]").click()
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[5]/div[2]/input")
    # zz.clear()
    # zz.send_keys(mail)
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[6]/input[2]").click()
    