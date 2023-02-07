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
        if "regtorg" in q  or "38" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://user.regtorg.ru/users/"
    brow.get(url=w)
    # https://user.regtorg.ru/users/   --- 1 капча ошибка
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/table/tbody/tr/td[2]/div[2]/div/form/div/div/div/table/tbody/tr[1]/td[2]/input")
        zz.click()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /user.regtorg.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/table/tbody/tr/td[2]/div[2]/div/form/div/div/div/table/tbody/tr[2]/td[2]/input[1]")
        zz.click()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /user.regtorg.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/table/tbody/tr/td[2]/div[2]/div/form/div/div/div/table/tbody/tr[3]/td[2]/input[1]")
        zz.click()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /user.regtorg.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/table/tbody/tr/td[2]/div[2]/div/form/div/div/div/table/tbody/tr[4]/td[2]/input")
        zz.click()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw1 /user.regtorg.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/table/tbody/tr/td[2]/div[2]/div/form/div/div/div/table/tbody/tr[5]/td[2]/input")
        zz.click()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw2 /user.regtorg.ru")
        pass
    
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/table/tbody/tr/td[2]/div[2]/div/form/div/div/div/table/tbody/tr[1]/td[2]/input")
    # zz.click()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/table/tbody/tr/td[2]/div[2]/div/form/div/div/div/table/tbody/tr[2]/td[2]/input[1]")
    # zz.click()
    # zz.send_keys(fio)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/table/tbody/tr/td[2]/div[2]/div/form/div/div/div/table/tbody/tr[3]/td[2]/input[1]")
    # zz.click()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/table/tbody/tr/td[2]/div[2]/div/form/div/div/div/table/tbody/tr[4]/td[2]/input")
    # zz.click()
    # zz.send_keys(passw)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/table/tbody/tr/td[2]/div[2]/div/form/div/div/div/table/tbody/tr[5]/td[2]/input")
    # zz.click()
    # zz.send_keys(passw)