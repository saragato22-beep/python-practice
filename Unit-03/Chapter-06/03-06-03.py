P = int(input())

for i in range(1, P+1):
    for j in range(P+1, 1, -1):
        print(f'{j-1} ', end= '')
    P -= 1
    print()