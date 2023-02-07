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
        if "https://xn--80adsqinks2h.xn--p1ai" in q or "52" in q or "твояфирма.рф" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://xn--80adsqinks2h.xn--p1ai/%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%8E"
    brow.get(url=w)
    # https://xn--80adsqinks2h.xn--p1ai/   ---
    try:
        zz=brow.find_element(By.NAME, "firm[name]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /твояфирма.рф")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/div[1]/div/main/div/div/div/div/form/div[2]/div[1]/select[1]/option[contains(text(),'{cityr}')]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/div[1]/div/main/div/div/div/div/form/div[2]/div[1]/select[2]/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /твояфирма.рф")
        pass
    try:
        brow.find_element(By.XPATH, "//*[@id=\"monday_nonstop\"]").click()
        brow.find_element(By.XPATH, "//*[@id=\"tuesday_nonstop\"]").click()
        brow.find_element(By.XPATH, "//*[@id=\"wednesday_nonstop\"]").click()
        brow.find_element(By.XPATH, "//*[@id=\"thursday_nonstop\"]").click()
        brow.find_element(By.XPATH, "//*[@id=\"friday_nonstop\"]").click()
        brow.find_element(By.XPATH, "//*[@id=\"saturday_nonstop\"]").click()
        brow.find_element(By.XPATH, "//*[@id=\"sunday_nonstop\"]").click()
    except Exception:
        print("Ошибка: timework /твояфирма.рф")
        pass
    try:
        zz=brow.find_element(By.NAME, "user-email")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /твояфирма.рф")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/form/input[2]").click()
    except Exception:
        print("Ошибка: правила /твояфирма.рф")
        pass
    try:
        zz=brow.find_element(By.NAME, "firm[subtitle]")
        zz.clear()
        zz.send_keys("Наркологическая клиника")
    except Exception:
        print("Ошибка: сфера /твояфирма.рф")
        pass
    try:
        zz=brow.find_element(By.NAME, "firm[officialname]")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /твояфирма.рф")
        pass
    try:
        zz=brow.find_element(By.NAME, "firm[description]")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /твояфирма.рф")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/form/div[1]/div[6]/div[1]/select[1]/option[13]").click()
        brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/form/div[1]/div[6]/div[1]/select[2]/option[18]").click()
        brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/form/div[1]/div[6]/div[1]/input").click()
    except Exception:
        print("Ошибка: категории /твояфирма.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "//*[@id=\"firm-keywords\"]")
        zz.clear()
        zz.send_keys(keysl)
        zz.send_keys(Keys.ENTER)
        zz.send_keys(Keys.DOWN)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: keysl /твояфирма.рф")
        pass
    
    try:
        zz=brow.find_element(By.NAME, "firm[postal]")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /твояфирма.рф")
        pass
    try:
        zz=brow.find_element(By.NAME, "firm[street]")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /твояфирма.рф")
        pass
    try:
        zz=brow.find_element(By.NAME, "firm[home]")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /твояфирма.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/form/div[3]/div[1]/input[1]")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /твояфирма.рф")
        pass
    try:
        zz=brow.find_element(By.NAME, "firm[sites][]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /твояфирма.рф")
        pass
    try:
        zz=brow.find_element(By.NAME, "firm[emails][]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /твояфирма.рф")
        pass
    # sleep(15)
    
    
    
    # zz=brow.find_element(By.NAME, "firm[name]")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "firm[subtitle]")
    # zz.clear()
    # zz.send_keys("Наркологическая клиника")
    # zz=brow.find_element(By.NAME, "firm[officialname]")
    # zz.clear()
    # zz.send_keys(unamecl)
    # zz=brow.find_element(By.NAME, "firm[description]")
    # zz.clear()
    # zz.send_keys(desc)
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/form/div[1]/div[6]/div[1]/select[1]/option[13]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/form/div[1]/div[6]/div[1]/select[2]/option[18]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/form/div[1]/div[6]/div[1]/input").click()
    # zz=brow.find_element(By.XPATH, "//*[@id=\"firm-keywords\"]")
    # zz.clear()
    # zz.send_keys(keysl)
    # zz.send_keys(Keys.ENTER)
    # zz.send_keys(Keys.DOWN)
    # zz.send_keys(Keys.ENTER)
    # zz=brow.find_element(By.NAME, "firm[postal]")
    # zz.clear()
    # zz.send_keys(ind)
    # zz=brow.find_element(By.NAME, "firm[street]")
    # zz.clear()
    # zz.send_keys(street)
    # zz=brow.find_element(By.NAME, "firm[home]")
    # zz.clear()
    # zz.send_keys(home)
    # zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/form/div[3]/div[1]/input[1]")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "firm[sites][]")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "firm[emails][]")
    # zz.clear()
    # zz.send_keys(mail)
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/form/div[4]/div[1]/div[1]/div/div[2]/input[1]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/form/div[4]/div[1]/div[2]/div/div[2]/input[1]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/form/div[4]/div[1]/div[3]/div/div[2]/input[1]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/form/div[4]/div[1]/div[4]/div/div[2]/input[1]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/form/div[4]/div[1]/div[5]/div/div[2]/input[1]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/form/div[4]/div[1]/div[6]/div/div[2]/input[1]").click()
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/form/div[4]/div[1]/div[7]/div/div[2]/input[1]").click()
    # zz=brow.find_element(By.NAME, "user-email")
    # zz.clear()
    # zz.send_keys(mail)
    # brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/form/input[2]").click()