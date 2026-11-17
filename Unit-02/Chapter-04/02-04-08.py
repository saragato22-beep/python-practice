s_1 = int(input())
s_2 = int(input())
s_3 = int(input())

if s_1 + s_2 <= s_3 or s_1 + s_3 <= s_2 or s_2 + s_3 <= s_1:
    print('not a triangle')
elif s_1 == s_2 == s_3:
    print('equilateral')
elif s_1 == s_2 or s_2 == s_3 or s_3 == s_1:
    print('isosceles')
elif (s_1 != s_2 != s_3):
        print('scalene')
else:
    print('not a triangle')