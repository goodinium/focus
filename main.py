import array as arr
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import importlib.util
import sys
import eel
import os
z=0
ci=0
service = Service(executable_path="/geckodriver")
cii=ci
eel.init("web")
@eel.expose
def conti(status,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind):
    numclinic="8"+numclinic
    numpl="+7"+numpl
    numcodcity=numcodcity[:-7]
    numclshot=numclshot[3:]
    numtrue=numn
    if fio.count(" ") == 2:
        fiom=fio.split(" ")
        f=fiom[0]
        i=fiom[1]
        o=fiom[2]
    else:
        f="Дронов"
        i="Михаил"
        o="Иванович"
    unamecl="ООО"+" \""+namecl+"\""
    print(unamecl)
    namepers=i+" "+f
    if fio.count("@") == 1:
        mmail=mail.split("@")
        login=mmail[0]
    if tupecl == "":
        tupecl="Клиника наркологической помощи"
    if keysl == "":
        keysl="нарколог на дом, вывод из запоя, лечение от алкоголизма, кодирование от алкоголизма, наркологическая помощь, лечение наркомании"
    if timework == "":
        timework="Круглосуточно, ежедневно"
    if passw == "":
        passw="LW9Tx44d"
    if ind=="":
        service = Service(executable_path="/geckodriver")
        brow=webdriver.Firefox(service=service)
        brow.get(url="https://www.pochta.ru/RU/post-index")
        sleep(2)
        try:
            zz=brow.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/input")
            zz.click()
            zz.clear()
            zz.send_keys(ciadress)
            sleep(1)
            zz.send_keys(Keys.DOWN)
            sleep(1)
            zz.send_keys(Keys.ENTER)
            sleep(2)
            ind=brow.find_element(By.CLASS_NAME, "index-card__postal-code").text
        except Exception:
            print("Ошибка: найти индекс")
            pass
        brow.quit()
        print(ind)
        
    print(tupecl)
    if "\n" in status:
        statuss=status.split("\n")
        for stat in statuss:
            print(stat[:-1])
            popit(stat,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
    else:
        popit(status,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)

def popit(izzi,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind):
    print("popit()")
    izzi=izzi+"\n"
    urr = os.path.abspath('')
    urr=urr.replace("\\", "/")
    urr=str(urr)
    ur=urr
    
    if cii==ci:
        if izzi=="Все\n" or izzi=="все\n" or izzi=="all\n" or izzi=="All\n":
            print("if(all)")
            zz=1
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            for iz in range(1,83):
                if iz==19 or iz==38 or iz==57 or iz==76:
                    service = Service(executable_path="/geckodriver")
                    brow=webdriver.Firefox(service=service)
                    zz=1
                spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
                foo1 = importlib.util.module_from_spec(spec)
                sys.modules[f"module.q{iz}q"] = foo1
                spec.loader.exec_module(foo1)
                foo1.goo(brow,zz-1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
                zz=zz+1
        elif izzi=="Отрезок\n" or izzi=="Интервал\n" or izzi=="интервал\n" or izzi=="отрезок\n" or izzi=="отр\n":
            print("if(Интервал)")
            otr1=int(otr1)
            otr2=int(otr2)
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            izi=zz=1
            for iz in range(otr1,otr2+1):
                if zz==19 or zz==39 or zz==57 or iz==76:
                    service = Service(executable_path="/geckodriver")
                    brow=webdriver.Firefox(service=service)
                    zz=1
                izi=izi+1
                spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{urr}/st/q{iz}q.py")
                foo1 = importlib.util.module_from_spec(spec)
                sys.modules[f"module.q{iz}q"] = foo1
                spec.loader.exec_module(foo1)
                foo1.goo(brow,zz-1,urr,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
                zz=zz+1
        elif izzi=="Кол-во\n" or izzi=="кол-во\n" or izzi=="количество\n" or izzi=="Количество\n":
            print("if(Кол-во)")
            otr1=int(otr1)
            zz=1
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            for iz in range(1,otr1+1):
                if zz==19 or zz==39 or zz==59:
                    service = Service(executable_path="/geckodriver")
                    brow=webdriver.Firefox(service=service)
                    zz=1
                spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{urr}/st/q{iz}q.py")
                foo1 = importlib.util.module_from_spec(spec)
                sys.modules[f"module.q{iz}q"] = foo1
                spec.loader.exec_module(foo1)
                foo1.goo(brow,zz,urr,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
                zz=zz+1
        elif izzi=="spravochnik\n" or izzi=="1\n" or izzi=="https://spravochnik.city/add\n" or izzi=="https://spravochnik.city/\n":
            iz=1  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="https://xn--80aqafkhejn4b.xn--p1ai/\n" or izzi=="2\n" or izzi=="компаниирф.рф\n" or izzi=="https://xn--80aqafkhejn4b.xn--p1ai/%D0%BD%D0%BE%D0%B2%D0%B0%D1%8F-%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%8F\n":
            iz=2
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="россия.бесплатныеобъявления\n" or izzi=="3\n" or izzi=="https://xn--h1alffa9f.xn--80abbembcyvesfij3at4loa4ff.xn--p1ai/podat\n" or izzi=="https://xn--h1alffa9f.xn--80abbembcyvesfij3at4loa4ff.xn--p1ai/\n":
            iz=3  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="spravkainform\n" or izzi=="4\n" or izzi=="https://spravkainform.ru/add\n" or izzi=="https://spravkainform.ru/\n":
            iz=4 
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service) 
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="otzyvgid\n" or izzi=="5\n" or izzi=="http://otzyvgid.ru/dobavit-kompaniju.html\n" or izzi=="http://otzyvgid.ru/omsk.html\n":
            iz=5  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="baza\n" or izzi=="6\n" or izzi=="http://baza-r.ru/join/registration/\n" or izzi=="http://baza-r.ru/\n":
            iz=6  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="companyinform\n" or izzi=="7\n" or izzi=="https://companyinform.ru/add-company\n" or izzi=="https://companyinform.ru/\n":
            iz=7  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="guidetorussia\n" or izzi=="8\n" or izzi=="https://guidetorussia.ru/add-firm\n" or izzi=="https://guidetorussia.ru/\n":
            iz=8  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="spravkarf24\n" or izzi=="9\n" or izzi=="https://spravkarf24.ru/new-firm\n" or izzi=="https://spravkarf24.ru/\n":
            iz=9  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="123ru\n" or izzi=="10\n" or izzi=="https://123ru.market/blok/add.php\n" or izzi=="https://123ru.market/\n":
            iz=10  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="topserver\n" or izzi=="11\n" or izzi=="https://topserver.ru/post_info.php?category_id=200&sel_city_id=124\n" or izzi=="https://topserver.ru/\n":
            iz=11  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="flado\n" or izzi=="12\n" or izzi=="https://www.flado.ru/org/add\n" or izzi=="https://www.flado.ru/\n":
            iz=12  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="medfirms\n" or izzi=="13\n" or izzi=="http://medfirms.ru/companies/?add\n" or izzi=="http://medfirms.ru/\n":
            iz=13  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="med.firmika\n" or izzi=="14\n" or izzi=="https://msk.med.firmika.ru/p_firm_add\n" or izzi=="https://msk.med.firmika.ru/\n":
            iz=14  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="infomesto\n" or izzi=="15\n" or izzi=="https://www.infomesto.com/business/add\n" or izzi=="https://www.infomesto.com/\n":
            iz=15  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="feech\n" or izzi=="16\n" or izzi=="https://feech.org/new-company\n" or izzi=="https://feech.org/\n":
            iz=16  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="korden" or izzi=="17\n" or izzi=="https://korden.org/companies/new\n" or izzi=="https://korden.org/\n":
            iz=17  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="dorus\n" or izzi=="18\n" or izzi=="http://www.dorus.ru/add.html\n" or izzi=="http://www.dorus.ru/\n":
            iz=18  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="rydo\n" or izzi=="19\n" or izzi=="https://rydo.ru/podat-obyavlenie/\n" or izzi=="https://rydo.ru/\n":
            iz=19  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="llike\n" or izzi=="20\n" or izzi=="https://llike.ru/add_company\n" or izzi=="https://llike.ru/\n":
            iz=20  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="firmexpert.ru\n" or izzi=="21\n" or izzi=="https://firmexpert.ru/\n" or izzi=="https://firmexpert.ru\n":
            iz=21  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="narkologicheskie\n" or izzi=="22\n" or izzi=="https://narkologicheskie-kliniki.com/dobavit-uchrezhdenie\n" or izzi=="https://narkologicheskie-kliniki.com/\n":
            iz=22  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="prostoboss.com\n" or izzi=="23\n" or izzi=="https://prostoboss.com/company/add\n" or izzi=="https://prostoboss.com\n":
            iz=23  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="tvoyaspravka\n" or izzi=="24\n"or izzi=="1" or izzi=="https://saratov.tvoyaspravka.ru/company/klinika_pandora_pl_lenina_47\n" or izzi=="https://saratov.tvoyaspravka.ru/\n":
            iz=24
            print("tvoyaspravka")
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{urr}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,urr,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="dbo\n" or izzi=="25\n" or izzi=="https://dbo.ru/add.html\n" or izzi=="https://dbo.ru/\n":
            iz=25  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="mycompany\n" or izzi=="26\n" or izzi=="https://mycompany.su/add\n" or izzi=="https://mycompany.su/\n":
            iz=26  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="wikiotzyv.org\n" or izzi=="27\n" or izzi=="https://rstv.wikiotzyv.org/addfirm\n" or izzi=="https://rstv.wikiotzyv.org/\n":
            iz=27  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="spravkaru\n" or izzi=="28\n" or izzi=="https://spravkaru.info/create/company\n" or izzi=="https://spravkaru.info/\n":
            iz=28  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="doski\n" or izzi=="29\n" or izzi=="https://www.doski.ru/post.php#\n" or izzi=="https://www.doski.ru/\n":
            iz=29  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="fis\n" or izzi=="30\n" or izzi=="https://fis.ru/reg?linkid=topgreen\n" or izzi=="https://fis.ru/\n":
            iz=30  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="orgpage\n" or izzi=="31\n" or izzi=="https://www.orgpage.ru/Cabinet/Create/\n" or izzi=="https://www.orgpage.ru/\n":
            iz=31  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="opt-union\n" or izzi=="32\n" or izzi=="https://www.opt-union.ru/registration/\n" or izzi=="https://www.opt-union.ru/\n":
            iz=32  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="firmlist.ru\n" or izzi=="33\n" or izzi=="https://firmlist.ru/registration\n" or izzi=="https://firmlist.ru/\n":
            iz=33
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="веб-службы\n" or izzi=="34\n" or izzi=="https://xn----9sbbbpi8a9bt6f.xn--p1ai/?p=person&event=entity.create&entityName=User\n" or izzi=="https://xn----9sbbbpi8a9bt6f.xn--p1ai/\n":
            iz=34  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="телефонырф.рф\n" or izzi=="35\n" or izzi=="https://телефонырф.рф/\n":
            iz=35  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="promportal\n" or izzi=="36\n" or izzi=="https://promportal.su/reg/firm/\n" or izzi=="https://promportal.su/\n":
            iz=36  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="moyaspravka.ru\n" or izzi=="37\n" or izzi=="https://omsk.moyaspravka.ru/add-company\n" or izzi=="https://omsk.moyaspravka.ru/\n":
            iz=37  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="regtorg\n" or izzi=="38\n" or izzi=="https://user.regtorg.ru/users/\n" or izzi=="http://www.regtorg.ru/\n":
            iz=38  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="centr.bizspravka.org\n" or izzi=="39\n" or izzi=="https://centr.bizspravka.org/add/firm\n" or izzi=="https://centr.bizspravka.org\n":
            iz=39  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="spravochnikov\n" or izzi=="40\n" or izzi=="https://spravochnikov.ru/\n" or izzi=="https://spravochnikov.ru/user/registration\n":
            iz=40  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="damspravku\n" or izzi=="41\n" or izzi=="https://msk.damspravku.ru/companies/new\n" or izzi=="https://msk.damspravku.ru/\n":
            iz=41  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="1000dosok\n" or izzi=="42\n" or izzi=="https://1000dosok.ru/doski.php?r=2\n" or izzi=="https://1000dosok.ru/index.php\n":
            iz=42  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="tradedir\n" or izzi=="43\n" or izzi=="https://cabinet.tradedir.ru/users/goods/\n" or izzi=="http://www.tradedir.ru/\n":
            iz=43  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="yndx\n" or izzi=="44\n" or izzi=="http://yndx.ru/company/registration\n" or izzi=="http://yndx.ru/\n":
            iz=44  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="kazan.spravka-region\n" or izzi=="45\n" or izzi=="https://kazan.spravka-region.ru/new_organization\n" or izzi=="https://kazan.spravka-region.ru/\n":
            iz=45  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="catalog-777\n" or izzi=="46\n" or izzi=="https://catalog-777.com/add-company/\n" or izzi=="https://catalog-777.com/\n":
            iz=46  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="spr\n" or izzi=="47\n" or izzi=="https://www.spr.ru/checkplus.php\n" or izzi=="https://www.spr.ru/\n":
            iz=47  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="loglink\n" or izzi=="48\n" or izzi=="http://www.loglink.ru/catalog/add/\n" or izzi=="http://www.loglink.ru/\n":
            iz=48 
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="russiabase\n" or izzi=="49\n" or izzi=="https://russiabase.ru/registration.php\n" or izzi=="https://russiabase.ru/\n":
            iz=49  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="mxkr\n" or izzi=="50\n" or izzi=="http://mxkr.ru/ru/company/registration\n" or izzi=="http://mxkr.ru/\n":
            iz=50  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="orgsinfo\n" or izzi=="51\n" or izzi=="https://orgsinfo.ru/neworg\n" or izzi=="https://orgsinfo.ru/\n":
            iz=51  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="твояфирма\n" or izzi=="52\n" or izzi=="https://xn--80adsqinks2h.xn--p1ai/%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%8E\n" or izzi=="https://xn--80adsqinks2h.xn--p1ai/\n":
            iz=52  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="reginforms\n" or izzi=="53\n" or izzi=="http://moskva.reginforms.ru/spravka/add-company.html\n" or izzi=="http://moskva.reginforms.ru/\n":
            iz=53  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="otzywy\n" or izzi=="54\n" or izzi=="https://www.otzywy.com/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%8E/\n" or izzi=="https://www.otzywy.com/\n":
            iz=54  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="allinform\n" or izzi=="55\n" or izzi=="https://www.allinform.ru/page39.html\n" or izzi=="https://www.allinform.ru/\n":
            iz=55  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="spravka.me\n" or izzi=="56\n" or izzi=="https://omsk.spravka.me/add/firm\n" or izzi=="https://spravka.me/\n":
            iz=56 
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service) 
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="morefirm.ru\n" or izzi=="57\n" or izzi=="https://morefirm.ru/add\n" or izzi=="https://morefirm.ru/add/\n":
            iz=57  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="spravochnik-rf\n" or izzi=="58\n" or izzi=="https://spravochnik-rf.ru/add/\n" or izzi=="https://spravochnik-rf.ru/\n":
            iz=58  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="asktel.ru\n" or izzi=="59\n" or izzi=="https://asktel.ru/addfirm\n" or izzi=="https://asktel.ru\n":
            iz=59  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="orghost" or izzi=="60\n" or izzi=="https://orghost.ru/\n":
            iz=60  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="vibirai\n" or izzi=="61\n" or izzi=="https://vibirai.ru/submit.html\n" or izzi=="https://vibirai.ru/\n":
            iz=61  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="www.barahla.net\n" or izzi=="62\n" or izzi=="https://www.barahla.net/add\n" or izzi=="https://www.barahla.net/\n":
            iz=62
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="твоястрана\n" or izzi=="63\n" or izzi=="https://xn--80aae9bdmgfd2k.xn--p1ai/%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C\n" or izzi=="https://xn--80aae9bdmgfd2k.xn--p1ai/\n":
            iz=63  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="bpages.ru\n" or izzi=="64\n" or izzi=="https://bpages.ru/add.php\n" or izzi=="https://bpages.ru/\n":
            iz=64
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="strananaladoni.ru\n" or izzi=="65\n" or izzi=="https://strananaladoni.ru/new-firm\n" or izzi=="https://strananaladoni.ru/\n":
            iz=65
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="spravkarf.ru\n" or izzi=="66\n" or izzi=="https://spravkarf.ru/\n":
            iz=66
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="rusfirm\n" or izzi=="67\n" or izzi=="https://rusfirm.biz/add\n" or izzi=="https://rusfirm.biz/\n":
            iz=67  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="totadres.ru\n" or izzi=="68\n" or izzi=="https://totadres.ru/add\n" or izzi=="https://totadres.ru/\n":
            iz=68
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="495ru\n" or izzi=="69\n" or izzi=="http://495ru.ru/q/show_edit_adv/\n" or izzi=="http://495ru.ru/\n":
            iz=69  
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="ot-boli.ru\n" or izzi=="70\n" or izzi=="https://ot-boli.ru/%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C_%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D0%BA%D1%83\n" or izzi=="https://ot-boli.ru/\n":
            iz=70
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="allrus.business\n" or izzi=="71\n" or izzi=="https://allrus.business/add/\n" or izzi=="https://allrus.business/\n":
            iz=71
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="gmstar.ru\n" or izzi=="72\n" or izzi=="http://gmstar.ru/reg/company/\n" or izzi=="http://gmstar.ru/\n":
            iz=72
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="spravka7.ru\n" or izzi=="73\n" or izzi=="https://spravka7.ru/add/\n" or izzi=="https://spravka7.ru/\n":
            iz=73
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="bigspr.ru\n" or izzi=="74\n" or izzi=="https://bigspr.ru/add/\n" or izzi=="https://bigspr.ru/\n":
            iz=74
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="bizly.ru\n" or izzi=="75\n" or izzi=="https://bizly.ru/add/\n" or izzi=="https://bizly.ru/\n":
            iz=75
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="russiacompany.ru\n" or izzi=="76\n" or izzi=="http://www.russiacompany.ru/index.php?m=8\n" or izzi=="http://www.russiacompany.ru/\n":
            iz=76
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="russiacatalog.ru\n" or izzi=="77\n" or izzi=="https://moskva.russiacatalog.ru/add/\n" or izzi=="https://moskva.russiacatalog.ru/\n":
            iz=77
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="bigspravka.ru\n" or izzi=="78\n" or izzi=="https://bigspravka.ru/addorg/\n" or izzi=="https://bigspravka.ru/\n":
            iz=78
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="наркологические-клиники.рф\n" or izzi=="79\n" or izzi=="https://xn----7sbjiaqbcaanddceiwnhb2b3a0l.xn--p1ai/kontakty\n":
            iz=79
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="beauty-rating.ru\n" or izzi=="80\n" or izzi=="http://beauty-rating.ru/catalog/add\n" or izzi=="http://beauty-rating.ru/\n":
            iz=80
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="dmaps.ru\n" or izzi=="81\n" or izzi=="dmaps.ru/add\n" or izzi=="https://ufa.dmaps.ru/\n":
            iz=81
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="ruscatalog.org\n" or izzi=="82\n" or izzi=="https://ruscatalog.org/company/add/\n" or izzi=="https://ruscatalog.org/\n":
            iz=82
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
        elif izzi=="invictory.com\n" or izzi=="83\n" or izzi=="http://www.invictory.com/sites/add.phtml\n" or izzi=="http://www.invictory.com/\n":
            iz=83
            service = Service(executable_path="/geckodriver")
            brow=webdriver.Firefox(service=service)
            spec = importlib.util.spec_from_file_location(f"module.q{iz}q", f"{ur}/st/q{iz}q.py")
            foo1 = importlib.util.module_from_spec(spec)
            sys.modules[f"module.q{iz}q"] = foo1
            spec.loader.exec_module(foo1)
            foo1.goo(brow,1,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
       



eel.start("index.html", size=(930,700))

