import json
from xona.xona_oop import Xona


class Mehmonxona:
    def __init__(self, nom):
        self.nom = nom
        self.__xonalar = []

    def xona_qosh(self, xona):
        if self.top(xona.raqam) is not None:
            return "❌ Bu raqamli xona mavjud!"

        self.__xonalar.append(xona)

        with open("jurnal.txt", "a", encoding="utf-8") as j:
            j.write(f"{xona.raqam}-xona qo'shildi ({xona.turi()})\n")

        return f"✅ {xona.raqam}-xona qo'shildi"

    def get_info(self):
        for xona in self.__xonalar:
            print(xona)

    def top(self, raqam):
        for xona in self.__xonalar:
            if xona.raqam == raqam:
                return xona
        return None

    def joylash(self, raqam, mehmon):
        xona = self.top(raqam)

        if xona is None:
            return "❌ Bunday xona mavjud emas!"

        if xona.band_mi():
            return f"❌ {raqam}-xona allaqachon band!"

        xona.band_qil(mehmon)

        with open("jurnal.txt", "a", encoding="utf-8") as j:
            j.write(f"{mehmon.ism} {raqam}-xonaga joylashdi\n")

        return f"🔑 {mehmon.ism} {raqam}-xonaga joylashdi"

    def boshat(self, raqam):
        xona = self.top(raqam)

        if xona is None:
            return "❌ Bunday xona mavjud emas!"

        if not xona.band_mi():
            return "❌ Bu xona allaqachon bo'sh"

        mehmon_ism = xona.mehmon_ismi()
        xona.boshat()

        with open("jurnal.txt", "a", encoding="utf-8") as j:
            j.write(f"{mehmon_ism} {raqam}-xonadan chiqdi\n")

        return f"👋 {mehmon_ism} {raqam}-xonadan chiqdi"

    def boshlar(self):
        return [
            xona for xona in self.__xonalar
            if not xona.band_mi()
        ]

    def eng_qimmat(self):
        if not self.__xonalar:
            return None

        return max(self.__xonalar, key=lambda xona: xona.narx)

    def daromad(self):
        return sum(
            xona.narx
            for xona in self.__xonalar
            if xona.band_mi()
        )

    def saqla(self):
        data = {
            self.nom: [
                {
                    "raqam": xona.raqam,
                    "narx": xona.narx,
                    "sigim": xona.sigim,
                    "turi": xona.turi()
                }
                for xona in self.__xonalar
            ]
        }

        with open("mehmonxona.json", "w", encoding="utf-8") as m:
            json.dump(data, m, indent=4, ensure_ascii=False)

        return f"💾 {len(self)} ta xona saqlandi"

    @classmethod
    def yukla(cls, nom):
        mehmonxona = cls(nom)

        try:
            with open("mehmonxona.json", "r", encoding="utf-8") as m2:
                data = json.load(m2)

            for xona_data in data.get(nom, []):
                xona = Xona(
                    xona_data["raqam"],
                    xona_data["narx"],
                    xona_data["sigim"]
                )
                mehmonxona.xona_qosh(xona)

            print(f"📂 {len(mehmonxona)} ta xona yuklandi")

        except FileNotFoundError:
            print("ℹ️ Saqlangan fayl topilmadi")

        return mehmonxona

    def __len__(self):
        return len(self.__xonalar)

    def __getitem__(self, item):
        return self.__xonalar[item]