stroc1,stroc2,stroc3 = len(input()),len(input()),len(input())
if (2 * stroc1 - stroc2 - stroc3)*(2 * stroc2 - stroc3 - stroc1)*(2 * stroc3 - stroc2 - stroc1):
    print('да')
else:
    print('нет')