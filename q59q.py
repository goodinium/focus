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
        if "asktel.ru" in q or "59" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"https://asktel.ru/addfirm/"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/input[2]")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /asktel.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/input[3]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: namecl /asktel.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/input[4]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /asktel.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/input[5]")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /asktel.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/input[6]")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /asktel.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/input[7]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /asktel.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /asktel.ru")
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
        