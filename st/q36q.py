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
        if "promportal" in q or "36" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://promportal.su/reg/firm/"
    brow.get(url=w)
    # https://promportal.su/reg/firm/   ---
    try:
        zz=brow.find_element(By.NAME, "firm_reg[name]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /promportal.su")
        pass
    try:
        zz=brow.find_element(By.NAME, "firm_reg[face]")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /promportal.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/form/div/div/div/div/div[3]/div[1]/input[1]")
        zz.clear()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: city /promportal.su")
        pass
    try:
        zz=brow.find_element(By.NAME, "firm_reg[user_contacts][value]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /promportal.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"firm_reg_user_phones_value\"]")
        zz.click()
        zz.clear()
        zz.send_keys(numn)
    except Exception:
        print("Ошибка: numn /promportal.su")
        pass
    try:
        zz=brow.find_element(By.NAME, "firm_reg[password]")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw1 /promportal.su")
        pass
    try:
        zz=brow.find_element(By.NAME, "firm_reg[password_repeat]")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw2 /promportal.su")
        pass
    
    # zz=brow.find_element(By.NAME, "firm_reg[name]")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "firm_reg[face]")
    # zz.clear()
    # zz.send_keys(fio)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/form/div/div/div/div/div[3]/div[1]/input[1]")
    # zz.clear()
    # zz.send_keys(city)
    # zz=brow.find_element(By.NAME, "firm_reg[user_contacts][value]")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "//*[@id=\"firm_reg_user_phones_value\"]")
    # zz.click()
    # zz.clear()
    # zz.send_keys(numn)
    # zz=brow.find_element(By.NAME, "firm_reg[password]")
    # zz.clear()
    # zz.send_keys(passw)
    # zz=brow.find_element(By.NAME, "firm_reg[password_repeat]")
    # zz.clear()
    # zz.send_keys(passw)