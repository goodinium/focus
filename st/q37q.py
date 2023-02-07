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
        if "moyaspravka" in q or "37" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w="https://moyaspravka.ru/"
    brow.get(url=w)
#https://saratov.moyaspravka.ru/ -------------------
    try:
        if "Архангельск" in city:
            brow.get(url="https://arhangelsk.moyaspravka.ru/add-company")
        elif "Астрахань" in city:
            brow.get(url="https://astrahan.moyaspravka.ru/add-company")
        elif "Барнаул" in city:
            brow.get(url="https://barnaul.moyaspravka.ru/add-company")
        elif "Брянск" in city:
            brow.get(url="https://bryansk.moyaspravka.ru/add-company")
        elif "Владивосток" in city:
            brow.get(url="https://vladivostok.moyaspravka.ru/add-company")
        elif "Волгоград" in city:
            brow.get(url="https://volgograd.moyaspravka.ru/add-company")
        elif "Воронеж" in city:
            brow.get(url="https://voronezh.moyaspravka.ru/add-company")
        elif "Екатеринбург" in city:
            brow.get(url="https://ekaterinburg.moyaspravka.ru/add-company")
        elif "Иваново" in city:
            brow.get(url="https://ivanovo.moyaspravka.ru/add-company")
        elif "Ижевск" in city:
            brow.get(url="https://izhevsk.moyaspravka.ru/add-company")
        elif "Иркутск" in city:
            brow.get(url="https://irkutsk.moyaspravka.ru/add-company")
        elif "Казань" in city:
            brow.get(url="https://kazan.moyaspravka.ru/add-company")
        elif "Калининград" in city:
            brow.get(url="https://kaliningrad.moyaspravka.ru/add-company")
        elif "Кемерово" in city:
            brow.get(url="https://kemerovo.moyaspravka.ru/add-company")
        elif "Киров" in city:
            brow.get(url="https://kirov.moyaspravka.ru/add-company")
        elif "Краснодар" in city:
            brow.get(url="https://krasnodar.moyaspravka.ru/add-company")
        elif "Красноярск" in city:
            brow.get(url="https://krasnoyarsk.moyaspravka.ru/add-company")
        elif "Курск" in city:
            brow.get(url="https://kursk.moyaspravka.ru/add-company")
        elif "Липецк" in city:
            brow.get(url="https://lipetsk.moyaspravka.ru/add-company")
        elif "Михайловск" in city:
            brow.get(url="https://mihaylovsk.moyaspravka.ru/add-company")
        elif "Москва" in city:
            brow.get(url="https://moscow.moyaspravka.ru/add-company")
        elif "Набережные Челны" in city:
            brow.get(url="https://naberezhnie-chelny.moyaspravka.ru/add-company")
        elif "Нижний Новгород" in city:
            brow.get(url="https://nizhniy-novgorod.moyaspravka.ru/add-company")
        elif "Новокузнецк" in city:
            brow.get(url="https://novokuznetsk.moyaspravka.ru/add-company")
        elif "Новосибирск" in city:
            brow.get(url="https://novosibirsk.moyaspravka.ru/add-company")
        elif "Омск" in city:
            brow.get(url="https://omsk.moyaspravka.ru/add-company")
        elif "Оренбург" in city:
            brow.get(url="https://orenburg.moyaspravka.ru/add-company")
        elif "Пермь" in city:
            brow.get(url="https://perm.moyaspravka.ru/add-company")
        elif "Ростов-на-Дону" in city:
            brow.get(url="https://rostov.moyaspravka.ru/add-company")
        elif "Рязань" in city:
            brow.get(url="https://ryazan.moyaspravka.ru/add-company")
        elif "Самара" in city:
            brow.get(url="https://samara.moyaspravka.ru/add-company")
        elif "Санкт-Петербург" in city:
            brow.get(url="https://sankt-peterburg.moyaspravka.ru/add-company")
        elif "Саратов" in city:
            brow.get(url="https://saratov.moyaspravka.ru/add-company")
        elif "Сочи" in city:
            brow.get(url="https://sochi.moyaspravka.ru/add-company")
        elif "Ставрополь" in city:
            brow.get(url="https://stavropol.moyaspravka.ru/add-company")
        elif "Сургут" in city:
            brow.get(url="https://surgut.moyaspravka.ru/add-company")
        elif "Тольятти" in city:
            brow.get(url="https://tolyatti.moyaspravka.ru/add-company")
        elif "Томск" in city:
            brow.get(url="https://tomsk.moyaspravka.ru/add-company")
        elif "Тула" in city:
            brow.get(url="https://tula.moyaspravka.ru/add-company")
        elif "Тюмень" in city:
            brow.get(url="https://tumen.moyaspravka.ru/add-company")
        elif "Улан-Удэ" in city:
            brow.get(url="https://ulan-ude.moyaspravka.ru/add-company")
        elif "Ульяновск" in city:
            brow.get(url="https://ulyanovsk.moyaspravka.ru/add-company")
        elif "Уфа" in city:
            brow.get(url="https://ufa.moyaspravka.ru/add-company")
        elif "Хабаровск" in city:
            brow.get(url="https://khabarovsk.moyaspravka.ru/add-company")
        elif "Чебоксары" in city:
            brow.get(url="https://cheboksary.moyaspravka.ru/add-company")
        elif "Челябинск" in city:
            brow.get(url="https://chelyabinsk.moyaspravka.ru/add-company")
        elif "Чита" in city:
            brow.get(url="https://chita.moyaspravka.ru/add-company")
        elif "Ярославль" in city:
            brow.get(url="https://yaroslavl.moyaspravka.ru/add-company")
        else:
            brow.get(url="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg")
                       
            
            
    except Exception:
        print("Ошибка: переход /moyaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "name")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /moyaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "subtitle")
        zz.clear()
        zz.send_keys("Клиника")
    except Exception:
        print("Ошибка: сфера /moyaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "description")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /moyaspravka.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/form/div/div/div/div[6]/div[1]/select[1]/option[7]").click()
        brow.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/form/div/div/div/div[6]/div[1]/select[2]/option[25]").click()
        brow.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/form/div/div/div/div[6]/div[1]/button").click()
    except Exception:
        print("Ошибка: категории /moyaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.ID, "edit-relation")
        zz.send_keys(keysl)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: keysl /moyaspravka.ru")
        pass
    sleep(1)
    try:
        zz=brow.find_element(By.NAME, "postal")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /moyaspravka.ru")
        pass
    
    try:
        zz=brow.find_element(By.NAME, "home")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /moyaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "street")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /moyaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "email[]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /moyaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "phone[]")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /moyaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "site[]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /moyaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "worktime[0][]")
        zz.clear()
        zz.send_keys("00:00-23:59")
        zz=brow.find_element(By.NAME, "worktime[1][]")
        zz.clear()
        zz.send_keys("00:00-23:59")
        zz=brow.find_element(By.NAME, "worktime[2][]")
        zz.clear()
        zz.send_keys("00:00-23:59")
        zz=brow.find_element(By.NAME, "worktime[3][]")
        zz.clear()
        zz.send_keys("00:00-23:59")
        zz=brow.find_element(By.NAME, "worktime[4][]")
        zz.clear()
        zz.send_keys("00:00-23:59")
        zz=brow.find_element(By.NAME, "worktime[5][]")
        zz.clear()
        zz.send_keys("00:00-23:59")
        zz=brow.find_element(By.NAME, "worktime[6][]")
        zz.clear()
        zz.send_keys("00:00-23:59")
    except Exception:
        print("Ошибка: timework /moyaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "ur_name")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /moyaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.ID, "edit-user-email")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /moyaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "user_pass")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw1 /moyaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.NAME, "user_pass2")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw2 /moyaspravka.ru")
        pass
    try:
        brow.find_element(By.ID, "edit-terms").click()
        brow.find_element(By.NAME, "personal-info").click()
    except Exception:
        print("Ошибка: правила /moyaspravka.ru")
        pass
    # try:
    #     sleep(1)
    #     brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[2]/form/div/div/div/div[9]/select/option[contains(text(),'{cityr}')]").click()
    #     sleep(1)
    #     brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[2]/form/div/div/div/div[10]/select/option[contains(text(),'{cityr}')]").click()
    # except Exception:
    #     print("Ошибка: xp /moyaspravka.ru")
    #     pass
    
    
    
    
    
    # zz=brow.find_element(By.NAME, "name")
    # #zz.click()
    # zz.clear()
    # zz.send_keys(namecl)
    # zz=brow.find_element(By.NAME, "subtitle")
    # zz.clear()
    # zz.send_keys("Клиника")
    # zz=brow.find_element(By.NAME, "description")
    # zz.clear()
    # zz.send_keys(desc)
    # brow.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/form/div/div/div/div[6]/div[1]/select[1]/option[7]").click()
    # brow.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/form/div/div/div/div[6]/div[1]/select[2]/option[25]").click()
    # brow.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/form/div/div/div/div[6]/div[1]/button").click()
    # zz=brow.find_element(By.ID, "edit-relation")
    # zz.send_keys(keysl)
    # zz.send_keys(Keys.ENTER)
    # sleep(1)
    # zz=brow.find_element(By.NAME, "postal")
    # zz.clear()
    # zz.send_keys(ind)
    # zz=brow.find_element(By.NAME, "home")
    # zz.clear()
    # zz.send_keys(home)
    # zz=brow.find_element(By.NAME, "street")
    # zz.clear()
    # zz.send_keys(street)
    # zz=brow.find_element(By.NAME, "email[]")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "phone[]")
    # zz.clear()
    # zz.send_keys(numclinic)
    # zz=brow.find_element(By.NAME, "site[]")
    # zz.clear()
    # zz.send_keys(url)
    # zz=brow.find_element(By.NAME, "worktime[0][]")
    # zz.clear()
    # zz.send_keys("00:00-23:59")
    # zz=brow.find_element(By.NAME, "worktime[1][]")
    # zz.clear()
    # zz.send_keys("00:00-23:59")
    # zz=brow.find_element(By.NAME, "worktime[2][]")
    # zz.clear()
    # zz.send_keys("00:00-23:59")
    # zz=brow.find_element(By.NAME, "worktime[3][]")
    # zz.clear()
    # zz.send_keys("00:00-23:59")
    # zz=brow.find_element(By.NAME, "worktime[4][]")
    # zz.clear()
    # zz.send_keys("00:00-23:59")
    # zz=brow.find_element(By.NAME, "worktime[5][]")
    # zz.clear()
    # zz.send_keys("00:00-23:59")
    # zz=brow.find_element(By.NAME, "worktime[6][]")
    # zz.clear()
    # zz.send_keys("00:00-23:59")
    # zz=brow.find_element(By.NAME, "ur_name")
    # zz.clear()
    # zz.send_keys(unamecl)
    # zz=brow.find_element(By.ID, "edit-user-email")
    # zz.clear()
    # zz.send_keys(mail)
    # zz=brow.find_element(By.NAME, "user_pass")
    # zz.clear()
    # zz.send_keys(passw)
    # zz=brow.find_element(By.NAME, "user_pass2")
    # zz.clear()
    # zz.send_keys(passw)
    # brow.find_element(By.ID, "edit-terms").click()
    # brow.find_element(By.NAME, "personal-info").click()