#Napišite program koji će učitavati tri prirodna broja a, b i c. Ti brojevi
#predstavljaju ukupan broj glasova koji je osvojila osoba A, ukupan broj glasova koji
#je osvojila osoba B i ukupan broj glasova koji je osvojila osoba C.
#Program treba ispisati osobu (A, B ili C) koja je osvojila najmanji broj glasova.
#Napomena: Samo će jedna osoba dobiti najmanji broj glasova. 

#ulaz(a, b, c)
#ako je a < b i a < c onda
#  izlaz('A')
#inače ako je b < c onda
#  izlaz('B')
#inače
#  izlaz('C')
####################################

a = input("upiši broj glasova za A: ")
b = input("upiši broj glasova za B: ")
c = input("upiši broj glasova za C: ")
if a < b and a < c :
    print('A')
elif b < c :
    print('B')
else:
    print('C')

