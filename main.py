import json

class Xona:
    jami = 0
    def __init__(self,raqam, narx, sigim=2):
        self.raqam = raqam
        self.narx = narx
        self.sigim = sigim
        self.__band = False
        self.__xona_raqam_list = []
        Xona.jami = +1

    def __str__(self):
        if self.__band is False:
            return f"{self.raqam}-xona | {self.turi()} | {self.narx} so'm | {self.sigim} kishi | bo'sh"
        else:
            return f"{self.raqam}-xona | {self.turi()} | {self.narx} so'm | {self.sigim} kishi | BAND ({mehmon.ism})"

    def band_mi(self):
        if self.__band is False:
            return True
        else:
            return False

    def band_qil(self,mehmon):
        if self.__band is False:
            self.__band = True
            return "BAND",self.__band
        else:
            return "bo'sh"

    def boshat(self):
        if self.__band is not False:
            self.__band = False
            return "endi bo'shadi"
        else:
            return "bo'sh",self.__band

    def xona_raqam(self):
        for i in self.__xona_raqam_list:
            if i == raqam_inp:
                return "❌ Bu raqamli xona bor!"
            else:
                self.__xona_raqam_list.append(raqam_inp)

    def turi(self):
        return "oddiy"

    @classmethod
    def get_jami(cls):
        return cls.jami


class Lyuks(Xona):
    def __init__(self,raqam, narx, sigim=4, nonushta=True):
        super().__init__(raqam, narx, sigim)
        self.nonushta = nonushta

    def __str__(self):
        qoshimcha = " + nonushta" if self.nonushta else ""
        return super().__str__() + qoshimcha


    def turi(self):
        return "Lyuks"

class Mehmon:
    def __init__(self,ism,tel):
        self.ism = ism
        self.tel = tel

    def __str__(self):
        return f"{self.ism} ({self.tel})"


class Mehmonxona:
    def __init__(self,nom):
        self.nom = nom
        self.__xonalar = []

    def xona_qosh(self,xona):
        if xona is x1:
            with open("jurnal.txt" , 'w') as j:
                j.write(f"{x1.raqam}-xona qo'shildi ({x1.turi()})\n")
            self.__xonalar.append(xona)
            return f"✅ {x1.raqam}-xona qo'shildi ({x1.turi()})"

    def get_info(self):
        for i in self.__xonalar:
            print(i)

    def top(self, raqam):
        for i in self.__xonalar:
            if i.raqam == raqam:
                return i
        return None

    def joylash(self,raqam,mehmon):
        if raqam is x1.raqam and x1.band_qil(mehmon):
            with open("jurnal.txt",'w') as j:
                j.write(f"{mehmon} {raqam}-xonaga joylashdi\n")
            return f"🔑 {mehmon} {raqam}-xonaga joylashdi"
        else:
            return f"❌ {raqam}-xona allaqachon band!"

    def boshat(self,raqam):
        if raqam is x1.raqam and x1.boshat():
            with open("jurnal.txt",'w') as j:
                j.write(f"{mehmon.ism} {raqam}-xonadan chiqdi\n")
            return f"👋 {mehmon.ism} {raqam}-xonadan chiqdi"
        else:
            return "❌ Bu xona allaqachon bo'sh"

    def boshlar(self):
        if x1.band_mi():
            with open("jurnal.txt",'a') as j:
                j.write(f"{x1} boshlar\n")
            return x1
        else:
            return ""

    def eng_qimmat(self):
        return max(self.__xonalar)

    def daromad(self):
        if x1.band_mi():
            daromad1 = x1.narx =+ x1.narx
            return daromad1
        else:
            return ""

    def saqla(self):
        mehmonxona_json = {
            create_xona.nom:[]
        }

        mehmonxona_json[create_xona.nom].append({"raqam": x1.raqam, "narx": x1.narx, "sigim": x1.sigim, "turi": x1.turi()})
        with open("mehmonxona.json" , 'a',encoding="utf-8") as m:
            json.dump(mehmonxona_json,m,indent=4,ensure_ascii=False)
        return f"💾 {len(self.__xonalar)} ta xona saqlandi → mehmonxona.json\n[jami xonalar: {len(self.__xonalar)}]"



    @classmethod
    def yukla(cls,nom):
        mehmonxona = cls(nom)
        try:
            with open("mehmonxona.json") as m:
                data = json.load(m)
                print(data)
            print(f"📂 {len(mehmonxona["Ustudy Hotel"])} ta xona yuklandi")
            with open("jurnal.txt",'w') as j:
                j.write(f"[LOG] {len(mehmonxona["Ustudy Hotel"])} ta xona fayldan yuklandi\n")
        except FileNotFoundError:
            print("ℹ️ Saqlangan fayl topilmadi — bo'sh mehmonxona ochildi")

        return mehmonxona


    def __len__(self):
        return len(self.__xonalar)

    def __getitem__(self, item):
        return item[0]


m = Mehmonxona.yukla("Ustudy Hotel")
create_xona = m

while True:
    try:
        menyu_mehmonxona = int(input("""=== 🏨 MEHMONXONA ===
1. Xona qo'shish
2. Barcha xonalar
3. Mehmon joylash
4. Xonani bo'shatish
5. Bo'sh xonalar
6. Eng qimmat xona
7. Bugungi daromad
8. Saqlash
9. Jurnalni ko'rish
0. Chiqish
Tanlang: """))

        if menyu_mehmonxona == 0:
            create_xona.saqla()
            break
        elif menyu_mehmonxona == 1:
            raqam_inp = int(input("Xona raqam kiriting: "))
            narx_inp = int(input("Xona narx kiriting: "))
            sigim_inp = int(input("Xona sigim kiriting: "))
            turi_inp = input("Turi (oddiy/lyuks): ")

            if create_xona.top(raqam_inp):
                print("❌ Bu raqamli xona bor!")
            else:
                if turi_inp == "lyuks":
                    x1 = Lyuks(raqam_inp, narx_inp, sigim_inp)
                else:
                    x1 = Xona(raqam_inp, narx_inp, sigim_inp)

                print(create_xona.xona_qosh(x1))
        elif menyu_mehmonxona == 2:
            print(create_xona.get_info())
        elif menyu_mehmonxona == 3:
            xona_raqam = int(input("Xona raqami:"))
            ism_inp = input("Mehmon ismi:")
            tel_inp = input("Telefon:")
            mehmon = Mehmon(ism_inp, tel_inp)
            print(create_xona.joylash(xona_raqam,mehmon.ism))
        elif menyu_mehmonxona == 4:
            xona_raqam = int(input("Xona raqami:"))
            print(create_xona.boshat(xona_raqam))
        elif menyu_mehmonxona == 5:
            print(create_xona.boshlar())
        elif menyu_mehmonxona == 6:
            print(create_xona.eng_qimmat())
        elif menyu_mehmonxona == 7:
            print(create_xona.daromad())
        elif menyu_mehmonxona == 8:
            print(create_xona.saqla())
        elif menyu_mehmonxona == 9:
            with open("jurnal.txt", 'r') as j:
                jurnal = j.read()
                print(jurnal)
    except ValueError:
        print("ValueError")


