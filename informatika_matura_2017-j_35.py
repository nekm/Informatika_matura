#Napišite program koji će učitati broj učenika, a zatim za svakoga od tih učenika
#broj opravdanih izostanaka. Program na kraju treba ispisati najmanji od učitanih
#opravdanih izostanaka
########################################################
#minop := 0;
#ulaz (n);
#za i := 1 do n činiti {
#    ulaz (op);
#    ako je i = 1 onda
#          minop := op;
#    ako je op < minop onda
#            minop := op;
#}
#izlaz (minop);

########################################################

n = int(input("Upiši broj učenika: "))
i = 1
nv = 0
ni = 0
while i <= n:
    m = int(input("Upiši broj izostanaka za "+str(i)+"-ov učenika: "))
    if i == 1 :
        nv = m
        ni = i
    if m < nv :
        nv = m
        ni = i
    i = i + 1
print("Najviše izostanaka ima ", ni, "učenik, ", nv)