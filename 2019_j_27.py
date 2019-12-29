#a = 12
#b = 18
#t = 0
#p = a + b
#k = 0
#dok je t == 0 činiti {
#    ako je p mod a == 0 I p mod b == 0 onda
#          t = t + 1
#    inače
#          p = p + 1
#     k = k + 1
#}
##################################################

a = 12
b = 18
t = 0
p = a + b
k = 0
while t == 0 :
    if p % a == 0 and p % b == 0 :
        t = t + 1
        print("t = " +str(t))
    else :
        print("p = " +str(p))
        p = p + 1
        print("p % a = " +str(p % a))
        print("p % b = " + str(p % b))
    k = k + 1
print ("k = " +str(k))
print ("p = " +str(p))


