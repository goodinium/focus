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
        if "bpages.ru" in q or "64" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"https://bpages.ru/add.php"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[1]/td[2]/input")
        zz.clear()
        zz.send_keys(namecl)
        brow.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[1]/td[2]/select/option[111]").click()
    except Exception:
        print("Ошибка: namecl /bpages.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[3]/td[2]/input[1]")
        zz.clear()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: city /bpages.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[3]/td[2]/input[2]")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /bpages.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[4]/td[2]/input[1]")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /bpages.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[4]/td[2]/input[2]")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /bpages.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[5]/td[2]/input[2]")
        zz.clear()
        zz.send_keys(numcodcity)
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[5]/td[2]/input[3]")
        zz.clear()
        zz.send_keys(numclshot)
    except Exception:
        print("Ошибка: num /bpages.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[8]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail1 /bpages.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[9]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /bpages.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[10]/td[2]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /bpages.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[11]/td[2]/select/option[23]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[12]/td[2]/select/option[35]").click()        
    except Exception:
        print("Ошибка: категории /bpages.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[14]/td/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /bpages.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[15]/td[2]/table/tbody/tr[1]/td[2]/input")
        zz.clear()
        zz.send_keys("Руководитель")
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[15]/td[2]/table/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio1 /bpages.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[16]/td[2]/table/tbody/tr[1]/td[2]/input")
        zz.clear()
        zz.send_keys("Менеджер")
        zz=brow.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[16]/td[2]/table/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio2 /bpages.ru")
        pass
    