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
        if "flado" in q or "47" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://my.flado.ru/registration"
            
            
    #--------------------------------------------
    # brow.get(url="https://my.flado.ru/profile/ads#")
    # zz=brow.find_element(By.XPATH, "//*[@id=\"InputStringEmail_39046\"]")
    # zz.clear()
    # zz.send_keys("grmonia-stacionar@yandex.ru")
    # zz=brow.find_element(By.XPATH, "//*[@id=\"InputPassword_85286\"]")
    # zz.clear()
    # zz.send_keys("LW9Tx44d")
    # brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/form/div[3]/div/div/label/span").click()
    # brow.find_element(By.XPATH, "//*[@id=\"InputButton_96796\"]").click()
    # sleep(2)
    # #--------------------------------------------
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/form/div[1]/div/div/input")
        zz.clear()
        zz.send_keys(i)
    except Exception:
        print("Ошибка: i /www.flado.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/form/div[2]/div/div/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /www.flado.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/form/div[3]/div/div/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw1 /www.flado.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/form/div[4]/div/div/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw2 /www.flado.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/form/div[5]/div/div/label/span").click()
    except Exception:
        print("Ошибка: правила /www.flado.ru")
        pass
    # http://yndx.ru/company/registration   ---
    # try:
    #     brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div/form/div[5]/div[2]/div[1]/label[6]/span").click()
    #     brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div/form/div[5]/div[2]/div[2]/label[2]/span").click()
    # except Exception:
    #     print("Ошибка: категории /www.flado.ru")
    #     pass
    # try:
    #     zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div/form/div[6]/div[1]/div/div/input")
    #     zz.clear()
    #     zz.send_keys(namecl)
    # except Exception:
    #     print("Ошибка: namecl /www.flado.ru")
    #     pass
    # try:
    #     zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div/form/div[6]/div[2]/div/div/textarea")
    #     zz.clear()
    #     zz.send_keys(desc)
    # except Exception:
    #     print("Ошибка: desc /www.flado.ru")
    #     pass
    # try:
    #     brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div/form/div[6]/div[4]/div[2]/div/div/span[3]").click()
    #     brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div/form/div[6]/div[4]/div[3]/div/div/span[3]").click()
    #     brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div/form/div[6]/div[4]/div[4]/div/div/span[3]").click()
    #     brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div/form/div[6]/div[4]/div[5]/div/div/span[3]").click()
    #     brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div/form/div[6]/div[4]/div[6]/div/div/span[3]").click()
    #     brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div/form/div[6]/div[4]/div[7]/div/div/span[3]").click()
    #     brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div/form/div[6]/div[4]/div[8]/div/div/span[3]").click()
    # except Exception:
    #     print("Ошибка: timework /www.flado.ru")
    #     pass
    # try:
    #     zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div/form/div[6]/div[5]/div/div/input")
    #     zz.clear()
    #     zz.send_keys(fio)
    # except Exception:
    #     print("Ошибка: fio /www.flado.ru")
    #     pass
    # try:
    #     zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div/form/div[6]/div[6]/div[1]/div/input")
    #     zz.clear()
    #     zz.send_keys(mail)
    # except Exception:
    #     print("Ошибка: mail /www.flado.ru")
    #     pass
    # try:
    #     zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div/form/div[6]/div[8]/div[1]/div/span/span[2]/input")
    #     zz.clear()
    #     zz.send_keys(numcodcity)
    # except Exception:
    #     print("Ошибка: numcodcity /www.flado.ru")
    #     pass
    # try:
    #     zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div/form/div[6]/div[8]/div[1]/div/span/span[3]/input")
    #     zz.clear()
    #     zz.send_keys(numclshot)
    # except Exception:
    #     print("Ошибка: numclshot /www.flado.ru")
    #     pass
    # try:
    #     zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div/form/div[6]/div[7]/div[1]/div/input")
    #     zz.clear()
    #     zz.send_keys(url)
    # except Exception:
    #     print("Ошибка: url /www.flado.ru")
    #     pass
    # try:
    #     zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div/form/div[6]/div[13]/div/div/input")
    #     zz.clear()
    #     zz.send_keys(adress)
    # except Exception:
    #     print("Ошибка: adress /www.flado.ru")
    #     pass
    
    