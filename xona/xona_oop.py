from main import mehmon
from main import raqam_inp

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
