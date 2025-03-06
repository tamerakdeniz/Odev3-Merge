import math

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

def karekok(x):
    return math.sqrt(x)

def us_alma(x, y):
    return math.pow(x, y)

def hesap_makinesi():
    print("Gelişmiş Hesap Makinesi")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Karekök")
    print("6. Üs Alma")

    secim = input("İşlem seçin (1/2/3/4/5/6): ")
    
    if secim in ['1', '2', '3', '4', '6']:
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
        elif secim == '6':
            print(f"{sayi1}^{sayi2} = {us_alma(sayi1, sayi2)}")
    
    elif secim == '5':
        sayi1 = float(input("Sayı: "))
        print(f"√{sayi1} = {karekok(sayi1)}")
    
    else:
        print("Geçersiz işlem!")

if __name__ == "__main__":
    hesap_makinesi()