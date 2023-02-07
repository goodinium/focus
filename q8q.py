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
        if "guidetorussia" in q or "11" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://guidetorussia.ru/add-firm"
    brow.get(url=w)
    #---------------------------------------------------
    # https://guidetorussia.ru/add-firm   ---   1 капча
    try:
        zz=brow.find_element(By.NAME, "name")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "official_name")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "subtitle")
        zz.clear()
        zz.send_keys("Наркологическая клиника")
    except Exception:
        print("Ошибка: сфера /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/fieldset[1]/div[4]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /guidetorussia.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/fieldset[1]/div[5]/select[1]/option[14]").click()
        sleep(2)
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/fieldset[1]/div[5]/select[2]/option[29]").click()
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/fieldset[1]/div[5]/button").click()
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/fieldset[1]/div[5]/select[1]/option[14]").click()
        sleep(2)
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/fieldset[1]/div[5]/select[2]/option[57]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/fieldset[1]/div[5]/button").click()
    # /html/body/main/div[2]/div/form/div[1]/div[5]/button
    except Exception:
        print("Ошибка: категории /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/fieldset[1]/div[7]/div/div[1]/div")
        zz.clear()
        zz.send_keys(keysl)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: keysl /guidetorussia.ru")
        pass
    try:
        sleep(2)
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div[3]/div/form/fieldset[2]/div[1]/select/option[contains(text(),'{cityr}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div[3]/div/form/fieldset[2]/div[1]/select[2]/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "postal")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "street")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "home")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/fieldset[2]/div[8]/div/div/ymaps/ymaps/ymaps/ymaps[4]/ymaps[1]/ymaps[1]/ymaps[2]/ymaps[1]/ymaps/ymaps/ymaps/ymaps/ymaps[1]/ymaps/ymaps[1]/ymaps[1]/input")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/fieldset[3]/div[1]/input[1]")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "website[0]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "email[0]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "work_week_in")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.NAME, "work_week_out")
        zz.clear()
        zz.send_keys("23:30")
    except Exception:
        print("Ошибка: timework /guidetorussia.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "register")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /guidetorussia.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/div[2]/input").click()
    except Exception:
        print("Ошибка: правила /guidetorussia.ru")
        pass
    
    
    # zz=brow.find_element(By.NAME, "name")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "official_name")
    # zz.clear()
    # zz.send_keys(unamecl)
    # zz=brow.find_element(By.NAME, "subtitle")
    # zz.clear()
    # zz.send_keys("Наркологическая клиника")
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/fieldset[1]/div[4]/textarea")
    # zz.clear()
    # zz.send_keys(desc)
    # brow.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/fieldset[1]/div[5]/select[1]/option[14]").click()
    # sleep(2)
    # brow.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/fieldset[1]/div[5]/select[2]/option[1]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/fieldset[1]/div[5]/button").click()
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/fieldset[1]/div[7]/div/div[1]/div")
    # zz.clear()
    # zz.send_keys(keysl)
    # zz.send_keys(Keys.ENTER)
    # zz=brow.find_element(By.NAME, "postal")
    # zz.clear()
    # zz.send_keys(ind)
    # zz=brow.find_element(By.NAME, "street")
    # zz.clear()
    # zz.send_keys(street)
    # zz=brow.find_element(By.NAME, "home")
    # zz.clear()
    # zz.send_keys(home)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/fieldset[2]/div[8]/div/div/ymaps/ymaps/ymaps/ymaps[4]/ymaps[1]/ymaps[1]/ymaps[2]/ymaps[1]/ymaps/ymaps/ymaps/ymaps/ymaps[1]/ymaps/ymaps[1]/ymaps[1]/input")
    # zz.clear()
    # zz.send_keys(ciadress)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/fieldset[3]/div[1]/input[1]")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "website[0]")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "email[0]")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "work_week_in")
    # zz.clear()
    # zz.send_keys("00:00")
    # zz=brow.find_element(By.NAME, "work_week_out")
    # zz.clear()
    # zz.send_keys("23:30")
    # zz=brow.find_element(By.NAME, "register")
    # zz.clear()
    # zz.send_keys(mail)
    # brow.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/div[2]/input").click()