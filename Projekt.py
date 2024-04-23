from abc import ABC, abstractmethod
from datetime import datetime

#Osztályok Létrehozása, 1. feladat:
class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def osszesites(self):
        pass

#Osztályok Létrehozása, 2. feladat:
class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, reggeli):
        super().__init__(ar, szobaszam)
        self.reggeli = reggeli

    def osszesites(self):
        return f"Egyágyas {self.szobaszam}. szoba, Ár: {self.ar} , Reggeli: {'Van' if self.reggeli else 'Nincs'}"

class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, ebed):
        super().__init__(ar, szobaszam)
        self.ebed = ebed

    def osszesites(self):
        return f"Kétágyas {self.szobaszam}. szoba, Ár: {self.ar} , Ebéd: {'Van' if self.ebed else 'Nincs'}"

#Osztályok Létrehozása, 3. feladat:
class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaadasa(self, szoba):
        self.szobak.append(szoba)

    def szobak_listazasa(self):
        for szoba in self.szobak:
            print(szoba.osszesites())

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas_datum = datum
                foglalas = Foglalas(szoba, foglalas_datum)
                self.foglalasok.append(foglalas)
                return f"A {szobaszam}. szoba sikeresen foglalva {datum} dátumra. Ár: {szoba.ar} Ft"
        return "Nincs ilyen szoba a szállodában."

    def foglalas_lemondasa(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            return "Foglalás sikeresen lemondva."
        else:
            return "Nincs ilyen foglalás."

     #Foglalások Kezelése: 3. feladat:
    def osszes_foglalas_listazasa(self):
        if self.foglalasok:
            for foglalas in self.foglalasok:
                print(foglalas.foglalas_osszesites())
        else:
            print("Nincs aktuális foglalás a szállodában.")

#Osztályok Létrehozása, 4. feladat:
class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def foglalas_osszesites(self):
        return f"A {self.szoba.szobaszam}. szoba foglalva {self.datum} dátumra."

# Példa adatok 
#Felhasználói Interfész és adatvalidáció: 4. feladat
def pelda_adatok_feltoltese(szalloda):

    egyagyas_szoba1 = EgyagyasSzoba(56500, 150, True)
    ketagyas_szoba1 = KetagyasSzoba(97000, 321, False)
    ketagyas_szoba2 = KetagyasSzoba(85000, 100, True)

    szalloda.szoba_hozzaadasa(egyagyas_szoba1)
    szalloda.szoba_hozzaadasa(ketagyas_szoba1)
    szalloda.szoba_hozzaadasa(ketagyas_szoba2)

    foglalas1 = Foglalas(egyagyas_szoba1, "2024-05-01")
    foglalas2 = Foglalas(ketagyas_szoba1, "2024-05-03")
    foglalas3 = Foglalas(ketagyas_szoba2, "2024-05-05")
    foglalas4 = Foglalas(egyagyas_szoba1, "2024-05-07")
    foglalas5 = Foglalas(ketagyas_szoba1, "2024-05-10")

    szalloda.foglalasok.extend([foglalas1, foglalas2, foglalas3, foglalas4, foglalas5])

def main():
    #Szálloda neve
    szalloda = Szalloda("Balaton szálloda")
    pelda_adatok_feltoltese(szalloda)

    #Felhasználói Interfész és adatvalidáció: 1. feladat
    while True:
        print("\nVálasszon műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Kérem válasszon(A sorszámot adja meg): ")

        #Foglalások Kezelése: 1. feladat:
        if valasztas == "1":
            szobaszam = input("Kérem adja meg a szoba számát: ")
            datum = input("Kérem adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")

            foglalas_datum = datetime.date(datetime.strptime(datum, "%Y-%m-%d"))
            jelenlegi_datum = datetime.date(datetime.now())

            #Felhasználói Interfész és adatvalidáció: 2. feladat
            if foglalas_datum < jelenlegi_datum:
                print("Hibás dátum, a foglalásnak a jövőben kell lennie.")
                continue
            
            szoba_foglalt = False
            for foglalas in szalloda.foglalasok:
                if foglalas.szoba.szobaszam == int(szobaszam) and datetime.date(datetime.strptime(foglalas.datum, "%Y-%m-%d")) == foglalas_datum:
                    szoba_foglalt = True
                    break

            if szoba_foglalt:
                print("A megadott szoba ezen a dátumon már foglalt.")
            else:
                print(szalloda.foglalas(int(szobaszam), datetime.date(datetime.strptime(datum, "%Y-%m-%d"))))
        
        #Foglalások Kezelése: 2. feladat:
        elif valasztas == "2":
            if szalloda.foglalasok:
                print("Válasszon a lemondandó foglalások közül:")
                for i, foglalas in enumerate(szalloda.foglalasok):
                    print(f"{i+1}. {foglalas.foglalas_osszesites()}")

                valasztott_index = input("Kérem adja meg a lemondandó foglalás sorszámát: ")

                #Felhasználói Interfész és adatvalidáció: 3. feladat
                try:
                    valasztott_index = int(valasztott_index)
                    if 1 <= valasztott_index <= len(szalloda.foglalasok):
                        foglalas = szalloda.foglalasok[valasztott_index - 1]
                        print(szalloda.foglalas_lemondasa(foglalas))
                    else:
                        print("Hibás sorszám.")
                except ValueError:
                    print("Hibás bemenet, válasszon egy sorszámot.")
            else:
                print("Nincs aktuális foglalás a szállodában.")

        #Foglalások Kezelése: 3. feladat: 
        elif valasztas == "3":
            szalloda.osszes_foglalas_listazasa()

        elif valasztas == "4":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás. Kérem válasszon újra.")

main()