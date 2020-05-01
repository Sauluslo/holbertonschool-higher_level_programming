#!/usr/bin/python3
str_tot = ""
for n in range(0, 100):
    str1 = str(n)
    if n < 10:
        str1 = "0" + str1
    if str1[0] != str1[1]:
        if n < int(str1[1] + str1[0]):
            str_tot += str1 + ", "
print(str_tot[0:len(str_tot) - 2])
