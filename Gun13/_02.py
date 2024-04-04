# Kullanıcının girdiği gün numarasına karşılık gelen günün adını yazın

gun_no = int(input("Gün no="))

# switch-case yapıları Python'da doğrudan bulunmadığı için if-elif-else yapısı kullanılır
if gun_no == 1:
    print("Pazartesi")
elif gun_no == 2:
    print("Salı")
elif gun_no == 3:
    print("Çarşamba")
elif gun_no == 4:
    print("Perşembe")
elif gun_no == 5:
    print("Cuma")
elif gun_no == 6:
    print("Cumartesi")
elif gun_no == 7:
    print("Pazar")
else:
    print("Hatalı giriş yaptınız")
