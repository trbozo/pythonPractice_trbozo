# Girilen bir sayıya(dahil) kadar olan sayıların çarpımını bulunuz
# bolum 2 : carpimin sonucu 10000 i geçtiğinde işlem sonlansın.

sinir = int(input("sayi giriniz="))

carpim = 1
for i in range(1, sinir + 1):
    carpim *= i  # 1*2*3*4*5...

    if carpim > 10000:
        print("break çalıştı")
        break

print("carpim =", carpim)
