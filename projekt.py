#która godzina
# import time
# def czas_liczba():
#     start=time.time()
#     input("Wprowadź cyfrę")
#     koniec = time.time()
#     wynik = koniec - start
#     return wynik
# print(czas_liczba())

# def odwroc(napis):
#     wynik=""
#     for i in  range(len(napis)):
#         wynik+=napis[len(napis)-i-1]
#     return wynik

# print(odwroc("Ala ma kota"))
# print(odwroc("kot ma Ale"))
# print(odwroc("kamil ślimak"))

# def zakupy(produkty,lista):
#     wynik=0
#     for produkt in lista:
#         if produkt not in produkty:
#             print("nie ma takiego produktu" + produkty +  "liczenie go omija")
#         else:
#             wynik+=produkty[produkt]
#         return wynik
# lista= ["mleko","masło","szynka"]
# produkty={"masło":4.00, "mleko":2.00,"szynka":5.00,"banan":5.00,"czekolada":6.00}
# lista=list(input("jakie produkty chcesz kupić?, Podaj ze spacją kolejne artykuły: ").split())
# print(zakupy(produkty,lista))


# import time,random
# def czas_cyfra():
#     import random
#     digit = random.randint(0,9)
#     print("wpisz cyfrę",digit)
#     start=time.time()
#     liczba=input()
#     while liczba != str(digit):
#         liczba = input()
#         print("niepoprawna cyfra")
#     koniec = time.time()
#     print("poprawna cyfra")
#     wynik = koniec - start
#     return wynik
# print(czas_cyfra())

# def zmien_znaki(napis):
#     liczba=0
#     wynik=""
#     for znak in male_na_duze:
#         wynik+=male_na_duze[znak]
#     else:
#         wynik+=znak
#         liczba=1
#     else:
#         if 

# male_na_duze = {'a':"A",'b':"B", "c":"C","d":"D","e":"E", "f":"F", "g":"G","h":"H", "i":"I","j":"J","k":"K","l":"L","m":"M","n":"N","o":"O","p":"P","r":"R",:"s"}

# def zmien_znak(napis):
#     liczba=0
#     wynik=""
#     for znak in napis:
#         if liczba==0:
#             wynik+=znak.upper
#             liczba=1
#     else:
#         wynik+=znak.lower
#     return wynik

# print(zmien_znak("wlazł kotek na płotek"))
# print(zmien_znak("W Pacanowie Kozy Kują"))

#pomocy
