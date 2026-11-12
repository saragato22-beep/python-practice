N = int(input())
word = ''

if N%3 == 0 and N%5 == 0:
    word += 'Fizz Buzz'
    print(word)
elif N%3 == 0 and N%5 != 0:
    word += 'Buzz'
    print(word)
elif N%5 == 0 and N%3 != 0:
    word += 'Fizz'
    print(word)
else:
    print(N)
