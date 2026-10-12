from xona.xona_oop import Xona
from lyuks_xona.lyuks_xona_oop import Lyuks
from mehmon.mehmon_oop import Mehmon
from mehmonxona.mehmonxona_oop import Mehmonxona


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
            print("Xayer ✋")
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


