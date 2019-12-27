#n := 11;
#b := 0;
#dok je n > 0 činiti
#  {
#    ako je n mod 3 <> 0 onda n := n – 4
#    inače n : = n - 1;
#    b := b + 1;
#  }
#######################################################################

n = 11
b = 0
print("b","n","div")
while n > 0 :
  
    if (n % 3) != 0:
      n = n - 4
    else: 
      n  = n - 1
    b = b + 1
    print(b,n,n%3)
print("b = "+ str(b))
print("n = "+ str(n))
