# SİPARİŞ ALMA UYGULAMASI

sys_kullanici = "halil"
sys_sifre = "12345"
girisHakki = 3
masa1 = 0
masa2 = 0
masa3 = 0

pilav = 13
yogurt = 5
pirzola = 42


while True:

    kullaniciAdi = input("Kullanıcı Adını Gir: ")
    parola = input("Parolanı Gir: ")


    if girisHakki == 0:
        print("Çıkış Yapılıyor...")
        break


    elif kullaniciAdi == sys_kullanici and parola != sys_sifre:
        print("Hatalı Şifre!")

        girisHakki -= 1

    elif kullaniciAdi != sys_kullanici and parola == sys_sifre:
        print("Hatalı Kullanıcı Adı!")
        girisHakki -= 1

    elif kullaniciAdi != sys_kullanici and parola != sys_sifre:
        print("Kullanıcı Adı ve Parola Hatalı")
        girisHakki -= 1

    else:
        print("Giriş Yapılıyor...")


        while True:
            print("*******************\n"
                      "------MASALAR------\n"
                      "MASA = 1 \n"
                      "MASA = 2 \n"
                      "MASA = 3\n"
                      "Geri Dönmek için A'ya Basın.\n"
                      "Çıkmak İçin Q'ya basın.  ")

            masaSeç = input("MASAYI SEÇİN: ")

            # -----------------------------------------------------

            if masaSeç.upper() == "A":
                break

            elif masaSeç == "1":

                while True:
                    siparis = input("Ne İstersiniz?\n"
                                "1 -- Pilav\n"
                                "2 -- Yoğurt\n"
                                "3 -- Pirzola\n"
                                "Üst Menüye Dönmek İçin a Harfine Bas.")

                    if siparis.upper() == "A":
                        break


                    elif siparis == "1" :
                        masa1 += pilav
                        print(f"Güncel Tutar = {masa1}")

                    elif siparis == "2":
                        masa1 += yogurt
                        print(f"Güncel Tutar = {masa1}")

                    elif siparis == "3":
                        masa1 += pirzola
                        print(f"Güncel Tutar = {masa1}")
                        continue

            elif masaSeç.upper() == "Q":
                exit()

            # -------------------------------------------------------

            elif masaSeç == "2":

                while True:
                    siparis = input("Ne İstersiniz?\n"
                                "1 -- Pilav\n"
                                "2 -- Yoğurt\n"
                                "3 -- Pirzola\n"
                                "Üst Menüye Dönmek İçin a Harfine Bas.")

                    if siparis.upper() == "A":
                        break


                    elif siparis == "1" :
                        masa2 += pilav
                        print(f"Güncel Tutar = {masa2}")

                    elif siparis == "2":
                        masa2 += yogurt
                        print(f"Güncel Tutar = {masa2}")

                    elif siparis == "3":
                        masa2 += pirzola
                        print(f"Güncel Tutar = {masa2}")
                        continue


            elif masaSeç == "3":

                while True:
                    siparis = input("Ne İstersiniz?\n"
                                "1 -- Pilav\n"
                                "2 -- Yoğurt\n"
                                "3 -- Pirzola\n"
                                "Üst Menüye Dönmek İçin a Harfine Bas.")

                    if siparis.upper() == "A":
                        break


                    elif siparis == "1" :
                        masa3 += pilav
                        print(f"Güncel Tutar = {masa3}")

                    elif siparis == "2":
                        masa3 += yogurt
                        print(f"Güncel Tutar = {masa3}")

                    elif siparis == "3":
                        masa3 += pirzola
                        print(f"Güncel Tutar = {masa3}")
                        continue