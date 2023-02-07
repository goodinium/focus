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
        if "centr.bizspravka.org" in q or "39" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"https://centr.bizspravka.org/add/firm"
    brow.get(url=w)
    try:
        if "Камчатский край" in cityr or "Амурская область" in cityr or "Хабаровский край" in cityr or "Приморский край" in cityr or "Республика Саха" in cityr or "Сахалинская область" in cityr:
            brow.find_element(By.XPATH, "/html/body/section/form/fieldset[3]/div[3]/div[1]/select[1]/option[2]").click()
        elif "Марий Эл" in cityr or "Приволжский федеральный округ" in cityr or "Чувашская" in cityr or "Удмуртская" in cityr or "Татарстан" in cityr or "Кировская область" in cityr  or "Самарская область" in cityr  or "Башкортостан" in cityr or "Нижегородская область" in cityr or "Мордовия" in cityr or "Саратовская область" in cityr or "Пензенская область" in cityr or "Оренбургская область" in cityr or "Ульяновская область" in cityr:
            brow.find_element(By.XPATH, "/html/body/section/form/fieldset[3]/div[3]/div[1]/select[1]/option[3]").click()
        elif "Архангельская область" in cityr or "Калининградская область" in cityr or "Псковская область" in cityr or "Новгородская область" in cityr or "Коми" in cityr or "Карелия" in cityr or "Вологодская область" in cityr or "Ленинградская область" in cityr or "Мурманская область" in cityr:
            brow.find_element(By.XPATH, "/html/body/section/form/fieldset[3]/div[3]/div[1]/select[1]/option[4]").click()
        elif "Северная Осетия" in cityr or "Дагестан" in cityr or "Ингушетия" in cityr or "Кабардино-Балкарская" in cityr or "Кабардино-Балкарская" in cityr:
            brow.find_element(By.XPATH, "/html/body/section/form/fieldset[3]/div[3]/div[1]/select[1]/option[5]").click()
        elif "Томская область" in cityr or "Хакасия" in cityr or "Красноярский край" in cityr or "Алтайский край" in cityr or "Новосибирская область" in cityr or "Иркутская область" in cityr or "Забайкальский край" in cityr or "Алтай" in cityr or "Кемеровская область" in cityr or "Омская область" in cityr or "Бурятия" in cityr:
            brow.find_element(By.XPATH, "/html/body/section/form/fieldset[3]/div[3]/div[1]/select[1]/option[6]").click()
        elif "Ямало-Ненецкий автономный округ" in cityr or "Свердловская область" in cityr or "Уральский федеральный округ" in cityr or "Челябинская область" in cityr or "Пермский край" in cityr or "Курганская область" in cityr or "Тюменская область" in cityr or "ХМАО" in cityr:
            brow.find_element(By.XPATH, "/html/body/section/form/fieldset[3]/div[3]/div[1]/select[1]/option[7]").click()
        elif "Белгородская область" in cityr or "Московская область" in cityr or "Брянская область" in cityr or "Ивановская область" in cityr or "Калужская область" in cityr or "Ярославская область" in cityr or "Владимирская область" in cityr or "Рязанская область" in cityr or "Воронежская область" in cityr or "Тульская область" in cityr or "Костромская область" in cityr or "Тамбовская область" in cityr or "Орловская область" in cityr or "Смоленская область" in cityr or "Липецкая область" in cityr or "Тверская область" in cityr or "Курская область" in cityr:
            brow.find_element(By.XPATH, "/html/body/section/form/fieldset[3]/div[3]/div[1]/select[1]/option[8]").click()
        else:
            brow.find_element(By.XPATH, "/html/body/section/form/fieldset[3]/div[3]/div[1]/select[1]/option[9]").click()
        
        brow.find_element(By.XPATH, f"/html/body/section/form/fieldset[3]/div[3]/div[1]/select[2]/option[contains(text(),'{cityr}')]").click()
        brow.find_element(By.XPATH, f"/html/body/section/form/fieldset[3]/div[3]/div[1]/select[3]/option[contains(text(),'{city}')]").click()
        # brow.find_element(By.XPATH, "/html/body/section/form/div/input[3]").click()
    except Exception:
        print("Ошибка: xp /centr.bizspravka.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/fieldset[1]/div[2]/div/input")
        zz.clear()
        zz.send_keys(i)
    except Exception:
        print("Ошибка: i /centr.bizspravka.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/fieldset[1]/div[3]/div[1]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /centr.bizspravka.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/fieldset[2]/div[2]/div/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /centr.bizspravka.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/fieldset[2]/div[3]/div[1]/input")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: tupecl /centr.bizspravka.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/fieldset[2]/div[4]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /centr.bizspravka.org")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/section/form/fieldset[2]/div[6]/select/option[390]").click()
    except Exception:
        print("Ошибка: категории /centr.bizspravka.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/fieldset[2]/div[8]/div/div[1]/div")
        zz.click()
        zz.send_keys(keysl)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: keysl /centr.bizspravka.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/fieldset[3]/div[2]/div/input")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /centr.bizspravka.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/fieldset[3]/div[5]/div/input")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /centr.bizspravka.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/fieldset[3]/div[6]/div/input")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /centr.bizspravka.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/fieldset[4]/div[2]/div/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /centr.bizspravka.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/fieldset[4]/div[4]/div/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /centr.bizspravka.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/fieldset[4]/div[5]/div/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /centr.bizspravka.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/fieldset[5]/div[2]/div/input")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /centr.bizspravka.org")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/div/input[2]")
        zz.clear()
        zz.send_keys("2")
    except Exception:
        print("Ошибка: капча /centr.bizspravka.org")
        pass
    sleep(2)
    try:
        brow.find_element(By.XPATH, "/html/body/section/form/div/input[3]").click()
    except Exception:
        print("Ошибка: правила /centr.bizspravka.org")
        pass
    
    
    
    
    