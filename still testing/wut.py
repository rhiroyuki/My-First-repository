import string

def vowel(msg):
    return ''.join([char for char in msg if char in 'aeiou'])
    
def consonant(msg):
    return ''.join([char for char in msg if char not in 'aeiou' \
                    and char not in string.punctuation])
    

print(vowel('lorena'))
print(consonant('parati'))
