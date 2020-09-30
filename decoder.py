'''
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.
Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Sample Input 1:

abcd
*d%#
abacabadaba
#*%*d*%


Sample Output 1:

*d*%*d*#*d*
dacabac

'''

# original_alphabet = list(input('Enter original alphadet: '))
original_alphabet = list('abcd')
# finite_alphabet = list(input('Enter finite alphabet: '))
finite_alphabet = list('*d%#')
# not_encrypted = list(input('Enter not_encrypted string: '))
not_encrypted = list('abacabadaba')
# not_encrypted = list(input('Enter encrypted string: '))
encrypted = list('#*%*d*%')

def encoder_decoder(original_alphabet, finite_alphabet):
    decoding_mask = dict(zip(original_alphabet, finite_alphabet))
    return decoding_mask

def encoding(decoding_mask, not_encrypted):
    for i in not_encrypted:
        if i in decoding_mask.keys():
            print(decoding_mask.keys()[i], end='')


    

decoding_mask = encoder_decoder(original_alphabet, finite_alphabet)
encoding(decoding_mask, not_encrypted)
 
 
 
 
 
 


