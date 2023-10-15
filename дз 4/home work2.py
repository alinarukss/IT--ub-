a = int(input())
if a == 0:
    print('зеленый')

if 1<= a <= 10 and a % 2== 0:
    print('черный')
else:
    print('красный')

if 11<= a <= 18 and a % 2== 0:
   print('красный')
else:
    print('черный')

if 19<= a <= 28 and a % 2== 0:
    print('черный')
else:
    print('красный')

if 29<= a <= 36 and a % 2== 0:
    print('красный')
else:
    print('черный')

if a> 36 and a < 0:
    print('Ошибка вввода')
