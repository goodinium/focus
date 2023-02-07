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
        if "russiabase" in q or "49" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://russiabase.ru/registration.php"

    # brow.get(url="https://russiabase.ru/org/orgadd.php")
    # try:
    #     brow.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[1]/div/ul[1]/li[1]/a").click()
    #     zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[2]/div/div/form/div[1]/div/p[1]/input")
    #     zz.clear()
    #     zz.send_keys("grmonia-stacionar@yandex.ru")
    #     zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[2]/div/div/form/div[1]/div/p[2]/input")
    #     zz.clear()
    #     zz.send_keys("LW9Tx44d")
    #     brow.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[2]/div/div/form/div[2]/input").click()
    # except Exception:
    #     print("Ошибка: login /russiabase.ru")
    #     pass
    # sleep(1)
    # brow.get(url="https://russiabase.ru/org/orgadd.php")
    # try:
    #     zz=brow.find_element(By.NAME, "orgname")

    #     zz.clear()
    #     zz.send_keys(ind)
    # except Exception:
    #     print("Ошибка: ind /russiabase.ru")
    #     pass
    # try:
    #     zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[9]/div/div/form/p[4]/input")
    #     zz.clear()
    #     zz.send_keys(adress)
    # except Exception:
    #     print("Ошибка: adress /russiabase.ru")
    #     pass
    # try:
    #     brow.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[9]/div/div/form/p[5]/select[1]/option[14]").click()
    #     brow.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[9]/div/div/form/p[5]/select[2]/option[12]").click()
    #     brow.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[9]/div/div/form/div[1]/table/tbody/tr[18]/td[1]/input").click()
    
    # except Exception:
    #     print("Ошибка: категории /russiabase.ru")
    #     pass
    # try:
    #     zz=brow.find_element(By.NAME, "orgpostal")
    #     zz.clear()
    #     zz.send_keys(numn)
    # except Exception:
    #     print("Ошибка: numn1 /russiabase.ru")
    #     pass
    # try:
    #     zz=brow.find_element(By.NAME, "orgtel[]")
    #     zz.clear()
    #     zz.send_keys(numn)
    # except Exception:
    #     print("Ошибка: numn2 /russiabase.ru")
    #     pass
    # try:
    #     zz=brow.find_element(By.NAME, "orgemail")
    #     zz.clear()
    #     zz.send_keys(mail)
    # except Exception:
    #     print("Ошибка: mail /russiabase.ru")
    #     pass
    # try:
    #     zz=brow.find_element(By.NAME, "orgsite")
    #     zz.clear()
    #     zz.send_keys(url)
    # except Exception:
    #     print("Ошибка: url /russiabase.ru")
    #     pass
    # try:
    #     zz=brow.find_element(By.NAME, "orgdescr")
    #     zz.clear()
    #     zz.send_keys(desc)
    # except Exception:
    #     print("Ошибка: desc /russiabase.ru")
    #     pass
    # try:
    #     zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[9]/div/div/form/p[18]/input")
    #     zz.clear()
    #     zz.send_keys(mail)
    # except Exception:
    #     print("Ошибка: mail /russiabase.ru")
    #     pass
    # try:
    #     k=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[9]/div/div/form/p[21]")
    #     print(k.text)
    #     k=k.text
    #     res=k.partition('т')[2]
    #     print(res)
    #     res=eval(res.partition('=')[0])
    #     print(res)
    #     zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[9]/div/div/form/p[21]/input")
    #     zz.clear()
    #     zz.send_keys(res)
    # except Exception:
    #     print("Ошибка: res /russiabase.ru")
    #     pass
    
    
    
    
    brow.get(url=w)
    
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[6]/div/div/div/form/p[1]/input")
        zz.clear()
        zz.send_keys(login)
    except Exception:
        print("Ошибка: login /russiabase.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[6]/div/div/div/form/p[2]/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw /russiabase.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[6]/div/div/div/form/p[3]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /russiabase.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[6]/div/div/div/form/p[4]/input")
        zz.clear()
        zz.send_keys(i)
    except Exception:
        print("Ошибка: i /russiabase.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[6]/div/div/div/form/p[6]/input")
        zz.clear()
        zz.send_keys("6")
    except Exception:
        print("Ошибка: капча /russiabase.ru")
        pass
   