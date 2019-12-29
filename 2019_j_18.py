#zbroj znamenaka prirodnog broja
#ulaz(n)
#s = 0
#dok je n > 0 činiti
#{
#    s = s + n mod 10
#    n = n div 10
#}
#############################

n = int(input ("Upiši broj : "))
n0 = n
s = 0
while n > 0 :
    s = s + n % 10
    n = n // 10
print("Zbroj znamenaka broja " +str(n0)+ " je " +str(s))
