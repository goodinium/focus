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
        if "mediapure.ru" in q or "82" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"http://www.invictory.com/sites/add.phtml"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[2]/form/input[1]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: namecl /ruscatalog.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[2]/form/input[2]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /ruscatalog.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[2]/form/textarea[1]")
        zz.clear()
        zz.send_keys("Медицинское учреждение, в котором можно получить профессиональную помощь. Правильное лечение освобождает больного от тяжелой разрушающей жизнь патологии.")
    except Exception:
        print("Ошибка: namecl /ruscatalog.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[2]/form/textarea[2]")
        zz.clear()
        zz.send_keys(keysl)
    except Exception:
        print("Ошибка: namecl /ruscatalog.org")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[2]/form/select[1]/option[24]").click()
    except Exception:
        print("Ошибка: namecl /ruscatalog.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[2]/form/input[4]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: namecl /ruscatalog.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[2]/form/input[5]")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: namecl /ruscatalog.org")
        pass
    