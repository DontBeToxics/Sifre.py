import random 
Kelime = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Şifre ne kadar uzun girin : ")) 

Sifre =  ""

for i in range(uzunluk):
    Sifre += random.choice(Kelime)

print(Sifre)
