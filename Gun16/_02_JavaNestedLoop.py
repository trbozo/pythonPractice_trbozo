# Aşağıdaki görüntüyü veren programı yazınız(yanlızca 1 yıldız ile yapınız)
# *        1.Satırda 1 yıldız
# **       2.satırda 2 yıldız
# ***      3.satırda 3 yıldız
# ****     4.satırda 4 yıldız
# *****    5.satırda 5 yıldız

for j in range(1, 6):  # 5 kez çalıştırılacak döngü
    for i in range(1, j+1):  # satır numarasına kadar yıldızları yazdırmak için döngü
        print("*", end="")  # yıldız yazdır
    print()  # yeni satıra geç
