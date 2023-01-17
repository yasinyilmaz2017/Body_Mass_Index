#bunu uygulama yap ve askeri gruplarda paylas
height = float(input("Boyunuzu cm olarak yazınız. "))

weight = float(input("Kilonuzu yazınız "))

height = height / 100

BMI = weight / (height ** 2)

print("Vucüt Kitle Endeksiniz ",BMI)

if BMI > 0:
    if BMI <= 16:
        print("Aşırı Zayıfsınız")

    elif BMI < 18:
        print("Zayıfsınız")

    elif (BMI >= 18) & (BMI <= 25):
        print("Sağlıklısınız")

    elif BMI <= 30:
        print("Kilolusunuz")

    else:
        print("Aşırı Kilolusunuz")

else:
    print("Geçerli bir değer giriniz.") 