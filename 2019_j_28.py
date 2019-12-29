#t = 2
#s = 0
#za i = 12 do 28 činiti
#    ako je i div 10 mod t == 0 onda
#       s = s + 1
#########################################

#t = 2 # za a)
t = 1  # za b)
s = 0
for i in range (12,29) :
    if (i // 10) % t == 0 :
       s = s + 1
       print ("i = " +str(i)+ " koji zadovoljava uvjet")
print ("s = " +str(s))