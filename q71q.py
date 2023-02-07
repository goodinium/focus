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
        if "allrus.business" in q or "71" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"https://allrus.business/add/"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[1]/div/div[2]/div/form/div[1]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /allrus.business")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[1]/div/div[2]/div/form/div[2]/select/optgroup[15]/option[87]").click()
    except Exception:
        print("Ошибка: namecl /allrus.business")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[1]/div/div[2]/div/form/div[3]/input")
        zz.clear()
        zz.send_keys("Россия, "+cityr+", "+city+", "+street+" "+home)
    except Exception:
        print("Ошибка: adress /allrus.business")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[1]/div/div[2]/div/form/div[4]/textarea")
        zz.clear()
        zz.send_keys(numpl)
    except Exception:
        print("Ошибка: numpl /allrus.business")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[1]/div/div[2]/div/form/div[5]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /allrus.business")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[1]/div/div[2]/div/form/div[6]/textarea")
        zz.clear()
        zz.send_keys("График работы: "+timework+"\n\nО компании: "+desc)
    except Exception:
        print("Ошибка: timework+desc /allrus.business")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[1]/div/div[2]/div/form/div[8]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /allrus.business")
        pass