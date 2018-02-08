# Script text here

import math 

def roman_number(n):
    u = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
    roman = ''
    k = n
    a = ''
    b = ''
    while k > 0:
        if math.floor(k / 1000) != 0:
            roman = roman + u[1000]
            k = k - 1000
        elif math.floor(k / 100) != 0:
            if 500 <= k < 1000:
                a = k + 100
                b = k
                if (500 <= a < 1000) and (500 <= b < 1000):
                    roman = roman + u[500]
                    k = k - 500
                else:
                    roman = roman + u[100] + u[1000]
                    k = k - 900
            elif 100 <= k < 500:
                a = k + 100
                b = k
                if (100 <= a < 500) and (100 <= b < 500):
                    roman = roman + u[100]
                    k = k - 100
                else:
                    roman = roman + u[100] + u[500]
                    k = k - 400
        else:
            if 50 <= k < 100:
                a = k + 10
                b = k
                if (50 <= a < 100) and (50 <= b < 100):
                    roman = roman + u[50]
                    k = k - 50
                else:
                    roman = roman + u[10] + u[100]
                    k = k - 90
            elif 10 <= k < 50:
                a = k + 10
                b = k
                if (10 <= a < 50) and (10 <= b < 50):
                    roman = roman + u[10]
                    k = k - 10
                else:
                    roman = roman + u[10] + u[50]
                    k = k - 40
            elif 5 <= k < 10:
                a = k + 1
                b = k
                if (5 <= a < 10) and (5 <= b < 10):
                    roman = roman + u[5]
                    k = k - 5
                else:
                    roman = roman + u[1] + u[10]
                    k = k - 9
            elif 1 <= k < 5:
                a = k + 1
                b = k
                if (1 <= a < 5) and (1 <= b < 5):
                    roman = roman + u[1]
                    k = k - 1
                else:
                    roman = roman + u[1] + u[5]
                    k = k - 4
    return roman

for i in range(100,500):
    print roman_number(i)