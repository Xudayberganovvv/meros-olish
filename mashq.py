# 11
# class uchuvchi:
#     def __init__(self , samolyot , forma):
#         self.samalyot = samolyot
#         self.forma = forma

# class harbiy_uchuvchi(uchuvchi):
#     def __init__(self, samolyot, forma , shlem , qurol):
#         super().__init__(samolyot, forma)
#         self.shlem = shlem
#         self.qurol = qurol

#     def get_info(self):
#         return f"samolyot modeli : {self.forma}\nshlemi :{self.shlem}\nquroli :{self.qurol}"
    

# samolyot=harbiy_uchuvchi("F-22", "f-22","3 lik shlem","AK-47")
# print(samolyot.get_info())    


# 12
# class kitob:
#     def __init__(self , nomi , muallif , yili ):
#         self.nomi = nomi
#         self.muallif = muallif
#         self.yili = yili

#     def get_info(self):
#         return f"Kitob nomi : {self.nomi}\nKitob muallifi : {self.muallif}\nKitob yili : {self.yili}"
    
# class darslik(kitob):
#     def __init__(self, nomi, muallif, yili,kitob_beti):
#         super().__init__(nomi, muallif, yili)
#         self.kitob_beti = self.kitob_beti
#     def get_info(self):
#         return f"Darslik nomi : {self.nomi}\nDarslik muallifi : {self.muallif}\nishlab chiqarish yili : {self.yili}"
    
# kitob = kitob("Ikki eshik orasi", "Alisher Navoiy","1875")
# print(kitob.get_info())


# 13
# class Hayvon:
#     def __init__(self,nomi):
#         self.nomi=nomi
#     def info(self):
#         return f"Hayvon nomi :{self.nomi}"
# class mushuk(Hayvon):
#     def __init__(self, nomi,ovoz):
#         super().__init__(nomi)
#         self.ovoz=ovoz
#     def cat_info(self):
#         return f"{self.info()}\nHayvon ovozi :{self.ovoz}"
    
# class Hayvon:
#     def ovoz():
#         return "Hayvonlar turlicha ovoz chiqaradi"

# class Mushuk(Hayvon):
#     def ovoz(self):
#         return "Mushuk miyov-miyov deydi"
    
# class It(Hayvon):
#     def ovoz(self):
#         return "It vov-vov deydi"
    

# cat = Mushuk()
# print(cat.ovoz())
# simba = It()
# print(simba.ovoz())


# 14
# class Qurilma:
#     def __init__(self ,ekran ,nomi ,narx): 
#         self.ekran = ekran
#         self.nomi = nomi
#         self.narx = narx    

#     def get_info(self):
#         return f"Qurilma ekrani : {self.ekran}\nQurilma nomi : {self.nomi}\nQurilma narxi : {self.narx}"

# class Telefon(Qurilma):
#     def __init__(self, ekran, nomi, narx,zaryadi,xotirasi):
#         super().__init__(ekran, nomi, narx)
#         self.zaryadi = zaryadi
#         self.xotirasi = xotirasi

#     def get_info(self):
#         return f"Telefon ekrani : {self.ekran}\nTelefon nomi : {self.nomi}\nTelefon narxi : {self.narx}\nTelefon zaryadi :{self.zaryadi}\nTelefon xotirasi :{self.xotirasi}"

# class Noutbuk(Qurilma):
#     def __init__(self, ekran, nomi, narx,xotirasi):
#         super().__init__(ekran, nomi, narx)
#         self.xotirasi = xotirasi

#     def get_info(self):
#         return f"Noutbuk ekrani : {self.ekran}\nNoutbuk nomi : {self.nomi}\nNoutbuk xotirasi : {self.xotirasi} Noutbuk narxi :{self.narx}"  

# Qurilma = Qurilma("artel", "700$","Haladelnik")
# Telefon = Telefon("Iphone","1500$","1 gb","100%")   
# Noutbuk = Noutbuk(15.6,"Viktus","550$","2 terabayt",)
# print(Qurilma.get_info())
# print(Telefon.get_info())
# print(Noutbuk.get_info())



# 15
# class kompaniya:
#     def __init__(self,xodim,ish_orni,daromadi):
#         self.xodim = xodim
#         self.ish_orni = ish_orni
#         self.daromadi = daromadi
    
#     def get_info(self):
#         return f"Kompaniya hodimi : {self.xodim}\nKompaniyada ish orni : {self.ish_orni}\nKompaniya daromadi : {self.daromadi}"
    
# class ishchi(kompaniya):
#     def __init__(self, ish_orni, daromadi,ish_vaqti):
#         super().__init__(ish_orni, daromadi)
#         self.ish_vaqti = ish_vaqti

#     def get_info(self):
#         return f"ishchining ish orni : {self.ish_orni}\nIshchining daromadi : {self.daromadi}\nIshchining ish vaxti : {self.ish_vaqti}"

# Kompaniya = kompaniya("MMM", "biznesmen","1000$")
# Ishchi = ishchi("biznesmen","1000$","ozongi 7 dan kechki 8 gacha")
# print(kompaniya.get_info(),ishchi.get_info())

# 16
# class 

# 17
# class Transport:
#     def __init__(self,narxi,probegi,tezligi):
#         self.narxi = narxi
#         self.probegi = probegi 
#         self.tezligi = tezligi
    
#     def get_info(self):
#         return f"Transport narxi : {self.narxi}\nTransport probegi : {self.probegi}\nTransport tezligi : {self.tezligi}"
    
# class Avtobus(Transport):
#     def __init__(self, narxi, probegi, tezligi,yolovchilar_soni):
#         super().__init__(narxi, probegi, tezligi)
#         self.yolovchilar_soni = yolovchilar_soni

#     def get_info1(self):
#         return f"Avtobus narxi : {self.narxi}\nAvtobus probegi :{self.probegi}\nAvtobus tezligi :{self.tezligi}\nAvtobusdagi yolovchilar soni:{self.yolovchilar_soni}"
    
# class Poyezd(Transport):
#     def __init__(self, narxi, probegi, tezligi,yurish_vaqti):
#         super().__init__(narxi, probegi, tezligi)
#         self.yurish_vaqti = yurish_vaqti
    
#     def get_info2(self):
#         return f"Poyezd narxi : {self.narxi}\nPoyezd probegi :{self.probegi}\nPoyezd tezligi :{self.tezligi}\nPoyezd yurish vaqti:{self.yurish_vaqti}"
        
# 18
# class Shaxs:
#     def __init__(self,ismi,familyasi):
#         self.ismi = ismi
#         self.familyasi = familyasi

#     def get_info(self):
#         return f"Shaxs ismi :{self.ismi}\nShaxs familyasi :{self.familyasi}"

# class Talaba(Shaxs):
#     def __init__(self, ismi, familyasi,yoshi):
#         super().__init__(ismi, familyasi)
#         self.yoshi = yoshi
    
#     def get_info(self):
#         return f"Talaba ismi :{self.ismi}\nTalaba familyasi :{self.familyasi}\nTalaba yoshi :{self.yoshi}"
    
# class Oqituvchi(Shaxs):
#     def __init__(self, ismi, familyasi,yoshi):
#         super().__init__(ismi, familyasi)
#         self.yoshi = yoshi
#     def get_info(self):
#         return f"Oqituvchi ismi : {self.ismi}\nOqituvchi familyasi :{self.familyasi}\nOqituvchi yoshi :{self.yoshi}"
    
# 19
# class Mahsulot:
#     def __init__(self,nomi,sifati,muddati):
#         self.nomi = nomi
#         self.sifati = sifati
#         self.muddati = muddati
    
#     def get_info(self):
#         return f"Mahsulot nomi : {self.nomi}\nMahsulot sifati :{self.sifati}\nMahsulot muddati :{self.muddati}"
    
# class Meva(Mahsulot):
#     def __init__(self, nomi,sifati,muddati,soni):
#         super().__init__(nomi,sifati, muddati)
#         self.soni = soni

#     def get_info(self):
#         return f"Meva nomi :{self.nomi}\nMeva sifati :{self.sifati}\nMeva muddati :{self.muddati}\nMeva soni :{self.soni}"
    
# mahsulot = Mahsulot("Marojni" ,"Zo'r" ,"2026 5 martgacha")
# meva = Meva("Olma", "Zo'r" , "2026 1-dekabrgacha" ,"20 ta")
# print(mahsulot.get_info(),meva.get_info())

# 20
# class Bino:
#     def __init__(self,qavat,xona):
#         self.qavat = qavat
#         self.xona = xona
    
#     def get_info(self):
#         return f"Bino qavati :{self.qavat}\nBino xonasi :{self.xona}"
    
# class Uy(Bino):
#     def __init__(self, qavat, xona,nomi):
#         super().__init__(qavat, xona)
#         self.nomi = nomi
    
#     def get_info(self):
#         return f"Uy qavati :{self.qavat }\nUy xonasi :{self.xona}\nUy nomi :{self.nomi}"
    
# bino = Bino("2 qavat" ,"6 xona bor")
# uy = Uy("3 qavat" ,"10 xona" ,"Lazizbek house")
# print(bino.get_info(),uy.get_info())



# 21
# class Bank:
#     def __init__(self,bank_hisobi):
#         self.bank_hisobi = bank_hisobi

#     def windraw(self,pul_miqdori):
#         return f"{self.bank} cha pul bor va yechildi{pul_miqdori}"
    
# class Xalq_Bank():

# 22
# class Kitob:
#     def __init__(self,nomi,muallifi):
#         self.nomi = nomi
#         self.muallifi = muallifi

#     def get_info(self):
#         return f"Kitob nomi :{self.nomi}\nKitob muallifi :{self.muallifi}"
    
# class ElektronKitob(Kitob):
#     def __init__(self, nomi, muallifi,sahifasi,yili):
#         super().__init__(nomi, muallifi)
#         self.sahifasi = sahifasi
#         self.yili = yili
    
#     def get_info(self):
#         return f"ElektronKitob nomi :{self.nomi}\nElektronKitob muallifi :{self.muallifi}\nElektronKitob sahifasi :{self.sahifasi}\nElektronKitob yili :{self.yili}"



# kitob = Kitob("Ikki eshik orasi" , "O'tkir Hoshimov")
# elektronKitob = ElektronKitob("Matematika Master" , "Bagandikov Yoqubboy" , "500 bet" , "2012")
# print(kitob.get_info())
# print(elektronKitob.get_info())



# 23
# class Mashina:
#     def __init__(self,nomi,tezligi,yurgani):
#         self.nomi = nomi
#         self.tezligi = tezligi
#         self.yurgani = yurgani

#     def get_info(self):
#         return f"Mashina nomi :{self.nomi}\nMashina tezligi :{self.tezligi}\nMashina yurgani :{self.yurgani}"
    
# class ElektroAvto(Mashina):
#     def __init__(self, nomi, tezligi, yurgani,rangi):
#         super().__init__(nomi, tezligi, yurgani)
#         self.rangi = rangi

#     def get_info(self):
#         return f"ElektroAvto nomi :{self.nomi}\nElektroAvto tezligi :{self.tezligi}\nElektroAuto yurgani :{self.yurgani}\nElektroAvto rangi :{self.rangi}"
    
# mashina = Mashina("Malibu" , "260" , "30 000")
# elektroAvto = ElektroAvto("BYD" , "300" , "20 000" , "qora")
# print(mashina.get_info())
# print(elektroAvto.get_info())


# 24
# class Ingliz :
#     def __init__(self,kurs_nomi,kurs_vaxti):
#         self.kurs_nomi = kurs_nomi
#         self.kurs_vaxti = kurs_vaxti
    
#     def Hisobla:



# 25
# class Hayvon:
#     def __init__(self,nomi,turi):
#         self.nomi = nomi
#         self.turi = turi

#     def get_info(self):
#         return f"Hayvon nomi :{self.nomi}\nHayvon turi :{self.turi}"
    
# class Qush(Hayvon):
#     def __init__(self, nomi, turi,uchishi):
#         super().__init__(nomi, turi)
#         self.uchish = uchishi

#     def get_info(self):
#         return f"Qush nomi :{self.nomi}\nQush turi :{self.turi}\nQush uchishi :{self.uchish}"
 
# hayvon = Hayvon("sher" ,"Hayvon")
# qush = Qush("Toti" ,"qush" ,"tez")
# print(hayvon.get_info())
# print(qush.get_info())


# 26
# class Maktab:
#     def __init__(self,maktab_nomi):
#         self.maktab_nomi = maktab_nomi

#     def get_info(self):
#         return f"Maktab nomi :{self.maktab_nomi}"
    
# class Sinf(Maktab):
#     def __init__(self, maktab_nomi,sinf_nomi,sinf_davomadi):
#         super().__init__(maktab_nomi)
#         self.sinf_nomi = sinf_nomi
#         self.sinf_davomadi = sinf_davomadi

#     def get_info(self):
#         return f"Sinf nomi :{self.sinf_nomi}\nSinf davomadi :{self.sinf_davomadi}"
    

# maktab = Maktab("10-maktab")
# sinf = Sinf("Kimyo xonasi" ,"30/30")
# print(Maktab.get_info())
# print(Sinf.get_info())

# 27

# class Avto:
#     def __init__(self,nomi,):
#         self.nomi = nomi

#     def get_info(self):
#         return f"Avto nomi :{self.nomi}\n"
    
# class Mersedes(Avto):
#     def __init__(self, nomi,probegi,rangi):
#         super().__init__(nomi)
#         self.probegi = probegi
#         self.rangi = rangi

#     def get_info(self):
#         return f"Mersedes probegi :{self.probegi}\n Mersedes rangi :{self.rangi}"

# class Chevrolet(Avto):
#     def __init__(self, nomi,rangi):
#         super().__init__(nomi)
#         self.rangi = rangi

#     def get_info(self):
#         return f"Chevrolet nomi :{self.nomi}\nChevrolet rangi :{self.rangi}"
    
# avto = Avto("Cobalt")
# mersedes = Mersedes("Mersedes benz" , "20 000" , "qora")
# chevrolet = Chevrolet("Gentra" , "oq")
# print(avto.get_info())
# print(mersedes.get_info())
# print(chevrolet.get_info())

# 28
# class Texnika:
#     def __init__(self,texnika_rangi,narxi,nomi ):
#         self.texnika_rangi = texnika_rangi
#         self.narxi = narxi
#         self.nomi = nomi

#     def get_info(self):
#         return f"Texnika rangi :{self.texnika_rangi}\nTexnika narxi :{self.narxi}\nTexnika nomi :{self.nomi}"
    
# class Printer(Texnika):
#     def __init__(self, texnika_rangi, narxi,nomi,yili):
#         super().__init__(texnika_rangi, narxi,nomi)
#         self.yili = yili
     
#     def get_info(self):
#         return f"Printer rangi :{self.texnika_rangi}\nPrinter narxi :{self.narxi}\nPrinter yili :{self.yili}"
    
# class Skanner(Texnika):
#     def __init__(self, texnika_rangi, narxi,nomi,yili):
#         super().__init__(texnika_rangi, narxi,nomi)
#         self.yili = yili

#     def get_info(self):
#         return f"Skanner rangi :{self.texnika_rangi}\nSkannner narxi :{self.narxi}\nSkanner yili :{self.yili}"
    

# texnika = Texnika("oq" , "300$" , "Muzlatkich")
# printer = Printer("qora" , "200$" , "2024")
# skanner = Skanner("qora" , "400$")
# print(texnika.get_info())
# print(printer.get_info())
# print(skanner.get_info())

# 29
# class Sportchi:
#     def __init__(self,ismi,familyasi,yili):
#         self.ismi = ismi
#         self.familyasi = familyasi
#         self.yili = yili
    
#     def get_info(self):
#         return f"Sportchi ismi :{self.ismi}\nSportchi familyasi :{self.familyasi}\nSportchi yili :{self.yili}"
     
# class Futbolchi(Sportchi):
#     def __init__(self, ismi, familyasi, yili,yoshi):
#         super().__init__(ismi, familyasi, yili)
#         self.yoshi = yoshi

#     def get_info(self):
#         return f"Futbolchi ismi :{self.ismi}\nFutbolchi familyasi :{self.familyasi}\nFutbolchi yili :{self.yili}\nFutbolchi yoshi :{self.yoshi}"
    
# sportchi = Sportchi("Sulaymon" , "Axmedov" , "2010")
# futbolchi = Futbolchi("Elbek" , "Jongirov" , "2010" , "16")
# print(sportchi.get_info())
# print(futbolchi.get_info())

# 30
# class Student:
#     def __init__(self,ismi,familyasi,yoshi):
#         self.ismi = ismi
#         self.familyasi = familyasi
#         self.yoshi = yoshi
    
#     def get_info(self):
#         return f"Student ismi :{self.ismi}\nStudent familyasi :{self.familyasi}\nStudent yili :{self.yoshi}"
 
# class Talaba(Student):
#     def __init__(self, ismi, familyasi, yoshi,yili):
#         super().__init__(ismi, familyasi, yoshi)
#         self.yili = yili

#     def get_info(self):
#         return f"Talaba ismi :{self.ismi}\nTalaba familyasi :{self.familyasi}\nTalaba yoshi :{self.yoshi}\nTalaba yili :{self.yili}"
    
# student = Student("Sulaymon" , "Axmedov" , "22")
# talaba = Talaba("Elbek" , "Jongirov" , "23" , "2003")
# print(student.get_info())
# print(talaba.get_info)

# 31
# class Avto:
#     def __init__(self,nomi,):
#         self.nomi = nomi

#     def get_info(self):
#         return f"Avto nomi :{self.nomi}\n"
    
# class BMW(Avto):
#     def __init__(self, nomi,probegi,rangi):
#         super().__init__(nomi)
#         self.probegi = probegi
#         self.rangi = rangi

#     def get_info(self):
#         return f"BMW probegi :{self.probegi}\n BMW rangi :{self.rangi}"

# class Chevrolet(Avto):
#     def __init__(self, nomi,rangi):
#         super().__init__(nomi)
#         self.rangi = rangi

#     def get_info(self):
#         return f"Chevrolet nomi :{self.nomi}\nChevrolet rangi :{self.rangi}"
    
# avto = Avto("Cobalt")
# BMW = BMW("Mersedes benz" , "20 000" , "qora")
# chevrolet = Chevrolet("Gentra" , "oq")
# print(avto.get_info())
# print(BMW.get_info())
# print(chevrolet.get_info())

# 32
# class kitob:
#     def __init__(self , nomi , muallif , yili ):
#         self.nomi = nomi
#         self.muallif = muallif
#         self.yili = yili

#     def get_info(self):
#         return f"Kitob nomi : {self.nomi}\nKitob muallifi : {self.muallif}\nKitob yili : {self.yili}"
    
# class darslik(kitob):
#     def __init__(self, nomi, muallif, yili,kitob_beti):
#         super().__init__(nomi, muallif, yili)
#         self.kitob_beti = self.kitob_beti
#     def get_info(self):
#         return f"Darslik nomi : {self.nomi}\nDarslik muallifi : {self.muallif}\nishlab chiqarish yili : {self.yili}"
    
# kitob = kitob("Ikki eshik orasi", "Alisher Navoiy","1875")
# print(kitob.get_info())


# 35
# class Hayvon:
#     def __init__(self,nomi,turi):
#         self.nomi = nomi
#         self.turi = turi

#     def get_info(self):
#         return f"Hayvon nomi :{self.nomi}\nHayvon turi :{self.turi}"
    
# class Mushuk(Hayvon):
#     def __init__(self, nomi, turi,ismi):
#         super().__init__(nomi, turi)
#         self.ismi = ismi

#     def get_info(self):
#         return f"Mushuk nomi :{self.nomi}\nMushuk turi :{self.turi}\nMushuk ismi :{self.turi}"
    
# class Baliq(Hayvon):
#     def __init__(self, nomi, turi,soni):
#         super().__init__(nomi, turi)
#         self.soni = soni

#     def get_info(self):
#         return f"Baliq nomi :{self.nomi}\nBaliq turi :{self.turi}\nBaliq soni :{self.soni}"
    
# hayvon = Hayvon("sher" , "itsimon")
# mushuk = Mushuk("Mushuk" , "uy mushugi" , "tom")
# baliq = Baliq("Sazan" , "chortan" , "7")
# print(hayvon.get_info())
# print(mushuk.get_info())
# print(baliq.get_info)


# 36
# class Kompaniya:
#     def __init__(self,nomi):
#         self.nomi = nomi
    
#     def get_info(self):
#         return f"Kompaniya nomi :{self.nomi}"
    
# class ITKompaniya(Kompaniya):
#     def __init__(self, nomi,manzili):
#         super().__init__(nomi)
#         self.manzili = manzili
    
#     def get_info(self):
#         return f"ITKompaniya nomi :{self.nomi}\nITKompaniya manzili :{self.manzili}"
    
# kompaniya = Kompaniya("Agrobank")
# itkompaniya = ITKompaniya("Al-Xorazmiy" , "durjba")
# print(kompaniya.get_info())
# print(itkompaniya.get_info())

# 37
# class Maxsulot:
#     def __init__(self,nomi,muddati):
#         self.nomi = nomi
#         self.muddati = muddati

#     def get_info(self):
#         return f"Maxsulot nomi :{self.nomi}\nMaxsulot muddati :{self.muddati}"   

# class Ichimlik(Maxsulot):
#     def __init__(self, nomi, muddati,soni, narxi):
#         super().__init__(nomi, muddati) 
#         self.soni = soni
#         self.narxi = narxi
    
#     def get_info(self):
#         return f"Ichimlik nomi :{self.nomi}\nIchimlik muddati :{self.muddati}\nIchimlik soni :{self.soni}\nIchimlik narxi :{self.narxi}"
    
# maxsulot = Maxsulot("sut" , "2026.03.01")
# ichimlik = Ichimlik("cola" , "2026.05.02" , "6" , "15")
# print(maxsulot.get_info())
# print(ichimlik.get_info())


# 38
# class Uskuna:
#     def __init__(self,nomi):
#         self.nomi = nomi
    
#     def get_info(self):
#         return f"Uskuna nomi :{self.nomi}"
    
# class Televizor(Uskuna):
#     def __init__(self, nomi,ekran):
#         super().__init__(nomi)
#         self.ekran = ekran
    
#     def get_info(self):
#         return f"Televizor nomi :{self.nomi}\nTelevizor ekrani :{self.ekran}"
    
# uskuna = Uskuna("temir qo'l")
# televizor = Televizor("Artel", "resurs")
# print(uskuna.get_info())
# print(televizor.get_info())


# 39
# class Avto:
#     def __init__(self,nomi,probegi):
#         self.nomi = nomi
#         self.probegi = probegi

#     def get_info(self):
#         return f"Avto nomi :{self.nomi}\nAvto probegi :{self.probegi}"
    
# class Elektromobil(Avto):
#     def __init__(self, nomi, probegi,narxi):
#         super().__init__(nomi, probegi)
#         self.narxi = narxi
    
#     def get_info(self):
#         return f"Elektromobil nomi :{self.nomi}\nElektromobil probegi :{self.probegi}\nElektomobil narxi :{self.narxi}"
    
# avto = Avto("KIA" , "20 000")
# elektromobil = Elektromobil("BYD" , "24 884" , "400 000$")
# print(avto.get_info())
# print(elektromobil.get_info())

# 40
# class Shaxs:
#     def __init__(self, ismi, familyasi):
#         self.ismi = ismi
#         self.familyasi = familyasi

#     def get_info(self):
#         return f"Shaxs ismi :{self.ismi}\nShaxs familyasi :{self.familyasi}"
    
# class Talaba(Shaxs):
#     def __init__(self, ismi, familyasi,yili):
#         super().__init__(ismi, familyasi)
#         self.yili = yili
    
#     def get_info(self):
#         return f"Talaba ismi :{self.ismi}\nTalaba familyasi :{self.familyasi}\nTalaba yili :{self.yili}"

# class Oqituvchi(Shaxs):
#     def __init__(self, ismi, familyasi,yili,):
#         super().__init__(ismi, familyasi)
#         self.yili = yili

#     def get_info(self):
#         return f"Oqituvchi ismi :{self.ismi}\nOqituvchi familyasi :{self.familyasi}\nOqituvchi yili :{self.yili}"

# shaxs = Shaxs("Sulaymon" , "Axmedov")
# talaba = Talaba("Elbek" , "Jongirov" , "2010")
# oqituvchi = Oqituvchi("Munisbek" , "Xudayberganov" , "2009")
# print(shaxs.get_info())
# print(talaba.get_info())
# print(oqituvchi.get_info())


# 41
# class Inson:
#     def __init__(self,ismi,yili):
#         self.ismi = ismi
#         self.yili = yili

#     def get_info(self):
#         return f"Inson ismi :{self.ismi}\nInson yili :{self.yili}"
    
# class Shifokor(Inson):
#     def __init__(self, ismi, yili,ish_joyi):
#         super().__init__(ismi, yili)
#         self.ish_joyi = ish_joyi

#     def get_info(self):
#         return f"Shifokor ismi :{self.ismi}\nShifokor yili :{self.yili}\nShifokor ish_joyi :{self.ish_joyi}"
    
# inson = Inson("laziz" , "2001")
# shifokor = Shifokor("Yoqubboy" , "2000" , "shifokor")
# print(inson.get_info())
# print(shifokor.get_info())

# 42
# class Kitob:
#     def __init__(self,yili,muallifi,nomi):
#         self.yili = yili
#         self.muallifi = muallifi
#         self.nomi = nomi

#     def get_info(self):
#         return f"Kitob yili :{self.yili}\nKitob muallifi :{self.muallifi}\nKitob nomi :{self.nomi}"
    
# class AudioKitob(Kitob):
#     def __init__(self, yili, muallifi, nomi,sifati):
#         super().__init__(yili, muallifi, nomi)
#         self.sifati = sifati

#     def get_info(self):
#         return f"AudioKitob yili :{self.yili}\nAudioKitob muallifi :{self.muallifi}\nAudioKitob nomi :{self.nomi}\nAudioKitob sifati :{self.sifati}"
    
    
# kitob = Kitob("2022" , "B.Yoqubboy" , "Ikki eshik orasi")
# audiokitob = AudioKitob("2020" , "A.Sulaymon" , "Dunyoning ishlari" , "zor")
# print(kitob.get_info())
# print(audiokitob.get_info())

# 43
# class Qurilma:
#     def __init__(self, nomi, hajmi):
#         self.nomi = nomi
#         self.hajmi = hajmi

#     def get_info(self):
#         return f"Qurilma nomi :{self.nomi}\nQurilma hajmi :{self.hajmi}"
    
# class SmartWatch(Qurilma):
#     def __init__(self, nomi, hajmi,yili):
#         super().__init__(nomi, hajmi)
#         self.yili = yili
    
#     def get_info(self):
#         return f"SmartWatch nomi :{self.nomi}\nSmartWatch hajmi :{self.hajmi}\nSmartWatch yili :{self.yili}"
    
# qurilma = Qurilma("Soat" , "kichik")
# smartwatch = SmartWatch("Smart soat" , "kichik" , "2025")
# print(qurilma.get_info())
# print(smartwatch.get_info())

# 44
# class Sportchi:
#     def __init__(self,ismi,familyasi):
#         self.ismi = ismi
#         self.familyasi = familyasi

#     def get_info(self):
#         return f"Sportchi ismi :{self.ismi}\nSportchi familyasi :{self.familyasi}"

    
# class Basketbolchi(Sportchi):
#     def __init__(self, ismi, familyasi,yili):
#         super().__init__(ismi, familyasi)
#         self.yili = yili
        

#     def get_info(self):
#         return f"Basketbolchi ismi :{self.ismi}\nBasketbolchi familyasi :{self.familyasi}\nBasketbolchi yili :{self.yili}"
    
# class Futbolchi(Sportchi):
#     def __init__(self, ismi, familyasi,jamoasi,raqami):
#         super().__init__(ismi, familyasi)
#         self.jamoasi = jamoasi
#         self.raqami = raqami

    
#     def get_info(self):
#         return f"Futbolchi ismi :{self.ismi}\nFutbolchi familyasi :{self.familyasi}\nFutbolchi jamoasi :{self.jamoasi}\Futbolchi raqami :{self.raqami}"
    
# sportchi = Sportchi("Elbek" , "Jongirov")
# basketbolchi = Basketbolchi("Yoqubboy" , "Bagandikov" , "2010")
# futbolchi = Futbolchi("Munisbek" , "Xudayberganov" , "Barselona futbolchisi" , "10")
# print(sportchi.get_info())
# print(basketbolchi.get_info())
# print(futbolchi.get_info())

# 45
# class Kompaniya:
#     def __init__(self,maoshi,manzili):
#         self.maoshi = maoshi
#         self.manzili = manzili

#     def get_info(self):
#         return f"Kompaniya maoshi :{self.maoshi}\nKompaniya manzili :{self.manzili}"
    
# class Rahbar(Kompaniya):
#     def __init__(self, maoshi, manzili,ismi,familyasi):
#         super().__init__(maoshi, manzili)
#         self.ismi = ismi
#         self.familyasi = familyasi

#     def get_info(self):
#         return f"Rahbar maoshi :{self.maoshi}\nRahbar manzili :{self.manzili}\nRahbar ismi :{self.ismi}\nRahbar familyasi :{self.familyasi}"
    

# kompaniya = Kompaniya("20 000$" , "Drujba center")
# rahbar = Rahbar("2000$" , "drjba" , "Munisbek" , "Xudayberganov")

# print(kompaniya.get_info())
# print(rahbar.get_info())

# 46
# class Hayvon:
#     def __init__(self,turi,nomi):
#         self.turi = turi
#         self.nomi = nomi

#     def get_info(self):
#         return f"Hayvon turi :{self.turi}\nHayvon nomi :{self.nomi}"
    
# class Ot(Hayvon):
#     def __init__(self, turi, nomi,yoshi):
#         super().__init__(turi, nomi)
#         self.yoshi = yoshi

#     def get_info(self):
#         return f"Ot turi :{self.turi}\nOt nomi :{self.nomi}\nOt yoshi :{self.yoshi}"


# hayvon = Hayvon("Mol" , "Misha")
# ot = Ot("Zotdor" , "qora bayr" , "3")
# print(hayvon.get_info())
# print(ot.get_info)



# 47
# class Mashina:
#     def __init__(self,yili,probegi):
#         self.yili = yili
#         self.probegi = probegi

#     def get_info(self):
#         return f"Mashina yili :{self.yili}\nMashina probegi :{self.probegi}"
    
# class YengilMashina(Mashina):
#     def __init__(self, yili, probegi,matori):
#         super().__init__(yili, probegi)
#         self.matori = matori

#     def get_info(self):
#         return f"YengilMashina yili :{self.yili}\nYengilMashina probegi :{self.probegi}\YengilMashina matori :{self.matori}"
    
# class YukMashina(Mashina):
#     def __init__(self, yili, probegi,yuk_sigimi):
#         super().__init__(yili, probegi)
#         self.yuk_sigimi = yuk_sigimi

#     def get_info(self):
#         return f"YukMashina yili :{self.yili}\nYukMashina probegi :{self.probegi}\YukMashina yuk sigimi :{self.yuk_sigimi}"

# mashina = Mashina("2022" , "20 000")
# yengilmashina = YengilMashina("2020" , "20 368" , "zor")
# yukmashina = YukMashina("2026" , "1000" , "kop")
# print(mashina.get_info())
# print(yengilmashina.get_info())
# print(yukmashina.get_info())



# 48
# class Shaxs:
#     def __init__(self,ismi,familyasi):
#         self.ismi = ismi 
#         self.familyasi = familyasi
    
#     def get_info(self):
#         return f"Shaxs ismi :{self.ismi}\nShaxs familyasi :{self.familyasi}"
    
# class Dasturchi(Shaxs):
#     def __init__(self, ismi, familyasi,yili):
#         super().__init__(ismi, familyasi)
#         self.yili = yili

#     def get_info(self):
#         return f"Dasturchi ismi :{self.ismi}\nDasturchi familyasi :{self.familyasi}\nDasturchi yili :{self.yili} "
    
# shaxs = Shaxs("Munisbek" , "Xudayberganov")
# dasturchi = Dasturchi("Yoqubboy" , "Bagandikov" , "2010")
# print(shaxs.get_info())
# print(dasturchi.get_info())















































































# Polimorfizm

# class Avto:
#     def info(self):
#         print("")



# class Tesla(Avto):
#     def info(self):
#         print("Elektra carlar oilasi")

# class Malibu(Avto):
#     def info(self):
#         print("Benzinda yuruvchi carlar oilasi")


# avtolar = [Tesla(), Malibu()]
# for avto in avtolar:
#     avto.info()

# 1
# class Hayvon:
#     def info(self):
#         print("")

# class Mushuk(Hayvon):
#     def info(self):
#         print("Miyav miyav")

# class Kuchuk(Hayvon):
#     def info(self):
#         print("vov vov"
#               )
# hayvonlar = [Mushuk(), Kuchuk()]
# for hayvon in hayvonlar:
#     hayvon.info()


# 2
# class Transport:
#     def __init__(self,name,shina):
#         self.name = name
#         self.shina = shina

#     def tezlik(self):
#         return f"{self.name} tezligi mator va inson omiliga bog'liq"
    
# class Avto(Transport):
#     def __init__(self, name, shina,mator):
#         super().__init__(name, shina)
#         self.mator = mator

#     def tezlik(self):
#         return f"bu avto motor kuchiga qarab tezlashadi {self.mator} ga teng"

# class Velosiped(Transport):
#     def __init__(self, name, shina,inson):
#         super().__init__(name, shina)
#         self.inson = inson

#     def tezlik(self):
#         return f"bu transportda tezlik inson omiliga bog'liq {self.inson} tez hayday oladi"
    
# avto1 = Avto("Nexia" , "2x4", "1.6 litr")
# print(avto1.tezlik())
# velo = Velosiped("velo 26" , "1x2" , "sportchi")
# print(velo.tezlik())


# 3
# class Meva:
#     def info(self):
#         print("")

# class Olma(Meva):
#     def info(self):
#         print("rang") 

# class Banan(Meva):
#     def info(self):
#         print("rang")  

# mevalar = [Olma(),Banan()]
# for meva in mevalar:
#     meva.info()


# 4
# class Xodim:
#     def __init__(self,ismi ,familyasi):
#         self.ismi = ismi
#         self.familyasi = familyasi

#     def 



# Inkopsulatsiya
# class Bank:
#     def __init__(self,mijoz_name , mijoz_balans):
#         self.name = mijoz_name
#         self.__balans = mijoz_balans

#     def add_summa(self,miqdori):
#         self.__balans = self.__balans + miqdori
#         print("Pul muvaffaqiyatli qo'shildi")
#     def withdraw(self,miqdori):
#         self.__balans -=miqdori
#         print(f"hisobingizdan {miqdori} cha pul yechildi")

#     def info(self):
#         print(f"Hurmatli {self.name} sizning hisobingizda hozirda {self.balans} ch pul bor")

# mijoz1 = Bank("Sulaymon" , 12000000)
# mijoz1.add_summa(5000000)
# mijoz1.info()