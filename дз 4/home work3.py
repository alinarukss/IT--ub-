a1, b1, a2, b2 =int(input()),int(input()),int(input()),int(input())
if (b2 == a1):
    print(b2)
if (b1 == a2):
    print(b1)
if (b1 < a2 or b2 < a1):
    print("пустое множество")
else:
    print(a1, a2),(b1,b2)