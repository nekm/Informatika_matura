#Napišite program koji prvo učitava prirodan broj N, a zatim učitava N prirodnih
#brojeva. Program treba ispisati broj učitanih brojeva kojima je zadnja znamenka
#jednaka predzadnjoj znamenki.
#Napomena: Svi upisani brojevi bit će veći od 9.
#--------------------------------------------------------------------------------
#ulaz(N)
#b = 0
#za i = 1 do N činiti {
#ulaz(t)
#z = t mod 10
#p = t div 10 mod 10
#ako je z == p onda
#b = b + 1
#}
#izlaz(b)
###############################
print("--+ Program koji ispisuje koliko među n upisanih brojeva imaju zadnju i predzanju znamenku istu +--")
n = int(input("Upiši broj: "))
b = 0
m = n + 1
for i in range (1, (n+1)) :
    t = int(input("Upiši broj veći od 9: "))
    z = t % 10
    p = t // 10 % 10
    if z == p :
        b = b + 1
print (str(b)+ " broja imaju istu predzadnju i zadnju znamenku")