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

def ct1(brow,ur,otr1,otr2,urli,www,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind):
    wwww=www.split("\n")
    for q in wwww:
        if "saratov.tvoyaspravka" in q or "1" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://saratov.tvoyaspravka.ru/company/klinika_pandora_pl_lenina_47"
    brow.get(url=w)
    brow.find_element(By.LINK_TEXT, "Добавить компанию").click()
    try:
        zz=brow.find_element(By.NAME, "title")
        zz.clear()
        zz.send_keys(namecl)    
    except Exception:
        print("Ошибка: namecl /tvoyaspravka")
        pass
    try:
        zz=brow.find_element(By.NAME, "offical_name")
        zz.clear()
        zz.send_keys(unamecl)   
    except Exception:
        print("Ошибка: unamecl /tvoyaspravka")
        pass
    try:
        zz=brow.find_element(By.NAME, "body")
        zz.clear()
        zz.send_keys(desc)   
    except Exception:
        print("Ошибка: desc /tvoyaspravka")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[5]/div/div[1]/div[1]/div/select[1]/option[7]").click()
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[5]/div/div[1]/div[1]/div/select[2]/option[17]").click()
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[5]/div/div[1]/div[1]/input").click()   
    except Exception:
        print("Ошибка: Категории /tvoyaspravka")
        pass
    try:
        zz=brow.find_element(By.CLASS_NAME, "tag-edit")
        zz.send_keys(keysl)
        sleep(2)
        zz.send_keys(Keys.ENTER)   
    except Exception:
        print("Ошибка: keysl /tvoyaspravka")
        pass
    try:
        sleep(2)
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[2]/form/div[2]/div[1]/div/div/div/div/select[1]/option[contains(text(),'{cityr}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[2]/form/div[2]/div[1]/div/div/div/div/select[2]/option[contains(text(),'{city}')]").click()
    
    except Exception:
        print("Ошибка: xp /tvoyaspravka")
        pass
    # /html/body/div[1]/main/div/div[2]/form/div[2]/div[1]/div/div/div/div/select[1]/option[contains(text(),'Краснодарский край')]
    # /html/body/div[1]/main/div/div[2]/form/div[2]/div[1]/div/div/div/div/select[2]/option[contains(text(),'Краснодар')]        '{}']".format(str(city))
    # print(cityr)
    # brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[2]/form/div[2]/div[1]/div/div/div/div/select[1]/option[contains(text()='{}']".format(str(cityr))).click()
    # brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[2]/form/div[2]/div[1]/div/div/div/div/select[2]/option[contains(text()='{}']".format(str(city))).click()
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[2]/div[2]/div/input")
        zz.clear()
        zz.send_keys(ind)   
    except Exception:
        print("Ошибка: ind /tvoyaspravka")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[2]/div[4]/div/input")
        zz.clear()
        zz.send_keys(street)    
    except Exception:
        print("Ошибка: street /tvoyaspravka")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[2]/div[5]/div/input")
        zz.clear()
        zz.send_keys(home)   
    except Exception:
        print("Ошибка: home /tvoyaspravka")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[3]/div[1]/div[1]/input")
        zz.send_keys(numn)   
    except Exception:
        print("Ошибка: numn /tvoyaspravka")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[3]/div[2]/div[1]/input")
        zz.send_keys(url)   
    except Exception:
        print("Ошибка: url /tvoyaspravka")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[3]/div[4]/div[1]/input")
        zz.send_keys(mail)    
    except Exception:
        print("Ошибка: mail /tvoyaspravka")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[4]/div/input")
        zz.send_keys(timework)   
    except Exception:
        print("Ошибка: timework /tvoyaspravka")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/fieldset/div[1]/div[2]/div[1]/input")
        zz.send_keys(fio)   
    except Exception:
        print("Ошибка: fio /tvoyaspravka")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/fieldset/div[1]/div[2]/div[2]/input")
        zz.clear()
        zz.send_keys("Менеджер")           
    except Exception:
        print("Ошибка: Менеджер /tvoyaspravka")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/fieldset/div[1]/div[2]/div[3]/input")
        zz.clear()
        zz.send_keys(mail)   
    except Exception:
        print("Ошибка: mail /tvoyaspravka")
        pass
    sleep(2)
    try:
        brow.find_element(By.ID, "persinfo").click()
        brow.find_element(By.ID, "edit-field-terms-value").click()   
    except Exception:
        print("Ошибка: правила /tvoyaspravka")
        pass