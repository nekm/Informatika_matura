#n := 2;
#ulaz(a);
#dok je n mod 7 <> 0 činiti
#  n := n + a;
#izlaz(n);
####################################
n = 2
a = int(input("Unesi broj "))
while n % 7 != 0 :
  n = n + a
print("n = " +str(n))

