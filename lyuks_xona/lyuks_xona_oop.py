from xona.xona_oop import Xona

class Lyuks(Xona):
    def __init__(self,raqam, narx, sigim=4, nonushta=True):
        super().__init__(raqam, narx, sigim)
        self.nonushta = nonushta

    def __str__(self):
        qoshimcha = " + nonushta" if self.nonushta else ""
        return super().__str__() + qoshimcha


    def turi(self):
        return "Lyuks"


