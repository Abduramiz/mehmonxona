from main import x1,create_xona
from main import mehmon
import json

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

