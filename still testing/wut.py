import string

def vowel(msg):
    b = ''
    for char in msg:
        if char in 'aeiou':
            b = b + char
    return b

def consonant(msg):
    return ''.join([char for char in msg if char not in 'aeiou' \
                    and char not in string.punctuation])
    

print(vowel('lorena'))
print(consonant('parati'))
