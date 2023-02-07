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
        if "spravkarf.ru" in q or "66" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"https://spravkarf.ru/"
    brow.get(url="http://translit-online.ru/")
    
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[3]/form/textarea[1]")
        # zz.clear()
        zz.click()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: переход1 /spravkarf.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div/div[3]/form/div[2]/div/input[1]").click()
    except Exception:
        print("Ошибка: переход2 /spravkarf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div[3]/form/textarea[2]").text
        # zz.click()
        # zz=zz.text()
        zz=zz.lower()
        print(zz)
        brow.get(url=f"https://{zz}.spravkarf.ru/")
        brow.find_element(By.XPATH, "/html/body/div[1]/header/div[3]/div[2]/nav/ul/li[2]/a").click()
    except Exception:
        print("Ошибка: переход3 /spravkarf.ru")
        pass
    sleep(1)
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/div/div[3]/form/fieldset[2]/div[1]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /spravkarf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"title\"]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /spravkarf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"field_subtitle\"]")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: tupecl /spravkarf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"field_j_name\"]")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /spravkarf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"field_spec\"]")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /spravkarf.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[3]/form/fieldset[1]/div[6]/select[1]/option[11]").click()
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[3]/form/fieldset[1]/div[6]/select[2]/option[34]").click()
    except Exception:
        print("Ошибка: категории /spravkarf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[3]/form/fieldset[1]/div[8]/div/div[1]/div")
        zz.clear()
        zz.send_keys(keysl)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: keysl /spravkarf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"field_street\"]")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /spravkarf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"field_building\"]")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /spravkarf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"field_index\"]")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /spravkarf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"field_fio\"]")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /spravkarf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"field_post\"]")
        zz.clear()
        zz.send_keys("Менеджер")
    except Exception:
        print("Ошибка: Менеджер /spravkarf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"field_phones\"]")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /spravkarf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"field_site\"]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /spravkarf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"field_mail\"]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail1 /spravkarf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"field_sheldule\"]")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /spravkarf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"register\"]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /spravkarf.ru")
        pass
    
    
    
    # zz=brow.find_element(By.XPATH, "/html/body/div/div[3]/form/textarea[2]").text
        # zz.click()
        # zz=zz.text()
    # zz=str(zz)
    # zz=zz.lower()
    # print(zz)
    
    sleep(1)
    try:
        brow.find_element(By.XPATH, "//*[@id=\"agree\"]").click()
        brow.find_element(By.XPATH, "//*[@id=\"pesinfo\"]").click()
    except Exception:
        print("Ошибка: правила /spravkarf.ru")
        pass
    
    