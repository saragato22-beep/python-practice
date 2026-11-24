word = input()
num_of_spaces = 0
str_length = len(word)
num_of_current_spaces = 0

for char in word:
    if char == ' ':
        num_of_spaces += 1

for index in range(str_length):
    char_at_index = word[index]
    if char_at_index == ' ':
        num_of_current_spaces += 1
        
        if num_of_current_spaces == num_of_spaces:
            print(index)
        else:
            print('{index}, ', end= '')

if num_of_spaces == 0:
    print('no spaces found')


    
