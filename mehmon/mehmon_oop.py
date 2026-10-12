class Mehmon:
    def __init__(self,ism,tel):
        self.ism = ism
        self.tel = tel

    def __str__(self):
        return f"{self.ism} ({self.tel})"