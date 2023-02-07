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
        if "firmika" in q or "49" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://msk.med.firmika.ru/p_firm_add"
    brow.get(url=w)
    # http://yndx.ru/company/registration   ---51
    try:
        brow.find_element(By.XPATH, f"/html/body/div[4]/div/div/section/div/form/fieldset/div/div[1]/div[1]/select/option[contains(text(),'{city}')]").click()

    except Exception:
        print("Ошибка: xp /msk.med.firmika.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[4]/div/div/section/div/form/fieldset/div/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /msk.med.firmika.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[4]/div/div/section/div/form/fieldset/div/div[1]/div[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /msk.med.firmika.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[4]/div/div/section/div/form/fieldset/div/div[2]/div[2]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /msk.med.firmika.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[4]/div/div/section/div/form/fieldset/div/div[1]/div[3]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /msk.med.firmika.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[4]/div/div/section/div/form/fieldset/div/div[2]/div[5]/div").click()
    except Exception:
        print("Ошибка: правила /msk.med.firmika.ru")
        pass
    
    # zz=brow.find_element(By.XPATH, "/html/body/div[4]/div/div/section/div/form/fieldset/div/div[2]/div[1]/input")
    # zz.clear()
    # zz.send_keys(street)
    # zz=brow.find_element(By.XPATH, "/html/body/div[4]/div/div/section/div/form/fieldset/div/div[1]/div[2]/input")
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[4]/div/div/section/div/form/fieldset/div/div[2]/div[2]/input")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.XPATH, "/html/body/div[4]/div/div/section/div/form/fieldset/div/div[1]/div[3]/input")
    # zz.clear()
    # zz.send_keys(url)
    # brow.find_element(By.XPATH, "/html/body/div[4]/div/div/section/div/form/fieldset/div/div[2]/div[5]/div").click()
    