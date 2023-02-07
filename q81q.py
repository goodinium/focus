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
        if "dmaps.ru" in q or "81" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"httpdmagdd"
    brow.get(url="http://translit-online.ru/")
    
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[3]/form/textarea[1]")
        # zz.clear()
        zz.click()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: переход1 /dmaps.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div/div[3]/form/div[2]/div/input[1]").click()
    except Exception:
        print("Ошибка: переход2 /dmaps.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[3]/form/textarea[2]").text
        # zz.click()
        # zz=zz.text()
        zz=zz.lower()
        print(zz)
        brow.get(url=f"https://{zz}.dmaps.ru/add")
        # brow.find_element(By.XPATH, "/html/body/div[1]/header/div[3]/div[2]/nav/ul/li[2]/a").click()
    except Exception:
        print("Ошибка: переход3 /dmaps.ru")
        pass
    sleep(2)
    
    
    
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/form/table/tbody/tr[1]/td[2]/div[1]/input")
        zz.clear()
        zz.send_keys("Наркологические клиники")
    except Exception:
        print("Ошибка: typecl /dmaps.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/form/table/tbody/tr[3]/td[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /dmaps.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/form/table/tbody/tr[4]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /dmaps.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/form/table/tbody/tr[5]/td[2]/input")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /dmaps.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/form/table/tbody/tr[6]/td[2]/input")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /dmaps.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/form/table/tbody/tr[7]/td[2]/input[2]")
        zz.clear()
        zz.send_keys(numn)
    except Exception:
        print("Ошибка: numn /dmaps.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/form/table/tbody/tr[9]/td[2]/input")
        zz.clear()
        zz.send_keys(timework)
        brow.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/form/table/tbody/tr[7]/td[2]/span").click()
    except Exception:
        print("Ошибка: timework /dmaps.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/form/table/tbody/tr[10]/td[2]/input")
        zz.clear()
        zz.send_keys(url)
        brow.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/form/table/tbody/tr[10]/td[2]/span").click()
    except Exception:
        print("Ошибка: url /dmaps.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/form/table/tbody/tr[12]/td[2]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /dmaps.ru")
        pass