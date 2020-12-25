import  random
import time

print("""
***********************************
Sayı Tahmin Oyunu

1 ile 40 arasında sayı tahmin etme
***********************************
""")

rastgele_sayı = random.randint(1,100)
tahmin_hakkı = 7

isim = input("İsminizi giriniz: ")
print("Hoşgeldin", isim)

while True:

    tahmin = int(input("Tahmininiz:"))

    if (tahmin < rastgele_sayı):
        print("Bilgiler Sorgulanıyor ...")
        time.sleep(1)

        print("Daha yüksek bir sayı söyleyin.")

        tahmin_hakkı -= 1

    elif ( tahmin > rastgele_sayı):
        print("Bilgiler Sorgulanıyor ...")
        time.sleep(1)

        print("Daha düşük bir sayı söyleyin.")
        tahmin_hakkı -= 1

    else:
        print("Bilgiler Sorgulanıyor ...")
        time.sleep(1)

        print("Tebrikler!", rastgele_sayı)
        break

    if (tahmin_hakkı == 0):
        print("Tahmin hakkınız bitti.")
        print(rastgele_sayı)
