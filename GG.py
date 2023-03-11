while True:
    import random
    import string

    uzunligi = int(input('Necha xonalik parol generatsiya qilsin?'))

    kichik = string.ascii_lowercase
    kotta = string.ascii_uppercase
    sonlar = string.digits
    belgilar = string.punctuation

    xammasi = kichik + kotta + sonlar + belgilar

    parol = random.sample(xammasi, uzunligi)

    pasword = ''.join(parol)

    print(pasword)