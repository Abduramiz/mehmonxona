class Xona:
    jami = 0
    def __init__(self,raqam, narx, sigim=2):
        self.raqam = raqam
        self.narx = narx
        self.sigim = sigim
        self.__band = False
        Xona.jami = +1

    def __str__(self):
        if self.__band is False:
            return f"{self.raqam}-xona | {self.turi()} | {self.narx} so'm | {self.sigim} kishi | bo'sh"
        else:
            return f"{self.raqam}-xona | {self.turi()} | {self.narx} so'm | {self.sigim} kishi | BAND ({self.__mehmon.ism})"

    def band_mi(self):
        if self.__band is False:
            return True
        else:
            return False

    def band_qil(self,mehmon):
        if not self.__band:
            self.__band = True
            self.__mehmon = mehmon
            return "BAND"
        return "Bu xona allaqachon band"

    def boshat(self):
        if self.__band is not False:
            self.__band = False
            return "endi bo'shadi"
        else:
            return "bo'sh",self.__band

    def turi(self):
        return "oddiy"

    @classmethod
    def get_jami(cls):
        return cls.jami
