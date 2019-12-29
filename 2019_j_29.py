#n = 0
#m = 0
#za i = 22 do 29 činiti {
#  k = 0
#  za j = 2 do i – 1 činiti
#    ako je i mod j == 0 onda
#      k = k + 1
#  ako je k <> 0 onda {
#    n = i
#    m = m + 1
#  }
#}
#######################################

n = 0
m = 0
for i in range (22, 30) :
  k = 0
  l = i
  for j in range (2, l) :
    if i % j == 0 :
      k = k + 1
      print ("i = " + str(i)+ ", j = " + str(j))
  if k != 0 :
    n = i
    m = m + 1
print ("n = " +str(n))
print ("m = " +str(m))
