def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Sıfıra bölünemez!"
    return x / y

def hesap_makinesi():
    print("Basit Hesap Makinesi")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

    secim = input("İşlem seçin (1/2/3/4): ")
    sayi1 = float(input("İlk sayı: "))
    sayi2 = float(input("İkinci sayı: "))

    if secim == '1':
        print(f"{sayi1} + {sayi2} = {toplama(sayi1, sayi2)}")
    elif secim == '2':
        print(f"{sayi1} - {sayi2} = {cikarma(sayi1, sayi2)}")
    elif secim == '3':
        print(f"{sayi1} * {sayi2} = {carpma(sayi1, sayi2)}")
    elif secim == '4':
        print(f"{sayi1} / {sayi2} = {bolme(sayi1, sayi2)}")
    else:
        print("Geçersiz giriş!")

if __name__ == "__main__":
    hesap_makinesi()