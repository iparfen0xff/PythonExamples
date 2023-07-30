a = int(input())
b = 'программист'
if a%10==1 and not a%100==11:
    print(a, b)
elif 1<a%10<5 and not 10<a%100<15:
    print(a, b + 'а')
else:
    print(a, b + 'ов')
