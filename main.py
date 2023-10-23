import random 
karakterler = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre_uzunlugu = int(input("Şifreniz Kaç karakter uzunluğunda olsun: "))

sifre = ""
for i in range(sifre_uzunlugu):
    sifre += random.choice(karakterler)

print(sifre)

print("dneeme")
