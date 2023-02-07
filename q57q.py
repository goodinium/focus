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
        if "morefirm.ru" in q or "57" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"https://morefirm.ru/add/"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/div/form/div[1]/div/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /mediapure.ru")
        pass
    try:
        brow.find_element(By.XPATH, "//*[@id=\"select2-inputCity-container\"]").click()
        zz=brow.find_element(By.XPATH, "/html/body/span[3]/span/span[1]/input")
        zz.clear()
        zz.send_keys(city)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: city /mediapure.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/div/form/div[7]/div/input")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /mediapure.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/div/form/div[12]/div/span/span[1]/span/ul/li/input")
        # zz.clear()
        # zz.click()
        zz.send_keys("Медицинская помощь на дому")
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: tupecl /mediapure.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/div/form/div[15]/div/textarea")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /mediapure.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/div/form/div[18]/div/textarea")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /mediapure.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"inputSites\"]")
        zz.clear()
        # zz.click()
        zz.send_keys(url)
        print(url)
    except Exception:
        print("Ошибка: url /mediapure.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"inputEmail\"]")
        zz.clear()
        # zz.click()
        zz.send_keys(mail)
        print(mail)
    except Exception:
        print("Ошибка: mail /mediapure.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/div/form/div[27]/div/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /mediapure.ru")
        pass
    
    # http://yndx.ru/company/registration   ---
    
        
        # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/form/fieldset[1]/div[1]/input")
        # zz.clear()
        # zz.send_keys(namecl)
        # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/form/fieldset[1]/div[2]/input")
        # zz.clear()
        # zz.send_keys(tupecl)
        # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/form/fieldset[1]/div[3]/input")
        # zz.clear()
        # zz.send_keys(unamecl)
        # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/form/fieldset[1]/div[5]/textarea")
        # zz.clear()
        # zz.send_keys(desc)
        # brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/form/fieldset[1]/div[6]/select[1]/option[11]").click()
        # sleep(1)
        # brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/form/fieldset[1]/div[6]/select[2]/option[23]").click()
        # sleep(1)
        # brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/form/fieldset[1]/div[6]/button").click()
        # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/form/fieldset[1]/div[8]/div/div[1]/div")
        # zz.clear()
        # zz.send_keys(keysl)
        # zz.send_keys(Keys.ENTER)
        # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/form/fieldset[2]/div[2]/input")
        # zz.clear()
        # zz.send_keys(street)
        # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/form/fieldset[2]/div[3]/input")
        # zz.clear()
        # zz.send_keys(home)
        # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/form/fieldset[3]/div[1]/input")
        # zz.clear()
        # zz.send_keys(fio)
        # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/form/fieldset[3]/div[2]/input")
        # zz.clear()
        # zz.send_keys("Менеджер")
        # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/form/fieldset[4]/div[1]/input[1]")
        # zz.clear()
        # zz.send_keys(numclinic)
        # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/form/fieldset[4]/div[2]/input[1]")
        # zz.clear()
        # zz.send_keys(url)
        # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/form/fieldset[4]/div[3]/input")
        # zz.clear()
        # zz.send_keys(mail)
        # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/form/fieldset[4]/div[5]/input")
        # zz.clear()
        # zz.send_keys(timework)
        # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/form/div[1]/input")
        # zz.clear()
        # zz.send_keys(mail)
        # brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/form/div[2]/input").click()
        # brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/form/div[3]/input").click()
        