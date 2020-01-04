#program za ispis krajnje lijeve znamenku prirodnoga broja n
#z := 0;
#dok je n > 0 činiti
#  {
#    z := n mod 10;
#    z := n div 10;
#  }
#izlaz(z);
#program je beskonačna petlja
## za izlaz pritisni ctrl c
###############################
n = 22
z = 0
while z >= 0 :
    z = n % 10
    z = n // 10
print(z)
