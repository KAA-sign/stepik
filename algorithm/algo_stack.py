# check_string = '([](){([])})'
flag = True
# check_stack = list(input())
open_char = ['(', '[', '{']
close_char = [')', ']', '}']

def check(check_string):
    check_stack = list(check_string)
    open_count, count, stack, flag = 0, 0, [], True
    for char in check_stack:
        count += 1
        if char in open_char:
            open_count += 1  
            stack.append(char)
        elif char in close_char:
            if stack == []:
                flag = False
                break
            else:
                top = stack.pop()
                if (top == '[' and char != ']') or (top == '(' and char != ')') or (top == '{' and char != '}'):
                    flag = False
                    break

    return 0 if flag and stack == [] else count

def check_check(flag, stack, open_count, count):
    if flag and stack == []:
        return 0
    elif 

# print('Success' if flag and stack == [] else len(stack))

assert check("([](){([])})") == 0
assert check("()[]}") == 5
assert check("{{[()]]") == 7
# assert check("{{{[][][]") == 3
assert check("{*{{}") == 3
# assert check("[[*") == 2
assert check("{*}") == 0
assert check("{{") == 2
assert check("{}") == 0
assert check("") == 0
assert check("}") == 1
assert check("*{}") == 0
assert check("{{{**[][][]") == 3