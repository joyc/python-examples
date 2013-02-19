mystring = 'hello'

char_count = dict()
for char in mystring:
    count = char_count.get(char, 0)
    count += 1
    char_count[char] = count

print char_count
