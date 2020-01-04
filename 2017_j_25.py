#b := 0;
#za i := 1 do 5 činiti
#  za j := 1 do 2 činiti
#    ako je j mod 2 = 1 onda b := b + 1;
#izlaz(b);
##############################################

b = 0
for i in range (1, 6) :
  for j in range (1, 3) :
    if j % 2 == 1 :
         b = b + 1
         print("i = " + str(i)+ ", j = " + str(j))
print("b = " + str(b))

