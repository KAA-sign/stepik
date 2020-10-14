original_alphabet = list(input('Enter original alphadet: '))
# original_alphabet = list('abcd')
finite_alphabet = list(input('Enter finite alphabet: '))
# finite_alphabet = list('*d%#')
not_encrypted = list(input('Enter not_encrypted string: '))
# not_encrypted = list('abacabadaba')
not_encrypted = list(input('Enter encrypted string: '))
# encrypted = list('#*%*d*%')


def encoder_decoder(original_alphabet, finite_alphabet):
    decoding_mask = dict(zip(original_alphabet, finite_alphabet))
    return decoding_mask

def sub_encoding(dm, not_encrypted):
    for i in not_encrypted:
        if i in dm.keys():
            print(dm.get(i), end='')

def sub_decoding(dm, encrypted):
    for i in encrypted:
        for key, value in dm.items():
            if i == value:
                print(key, end='')
        

dm = encoder_decoder(original_alphabet, finite_alphabet)
sub_encoding(dm, not_encrypted)
print()
sub_decoding(dm, encrypted)
 
 
 
 
 


