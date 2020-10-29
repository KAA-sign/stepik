with open ('in.txt') as file_in, open("out.txt", 'w') as file_out:
    for line in file_in:
        result = ''
        for i in range(len(line)):
            if i > (len(line) - 3):
                result += line[i] * int(line[i+1])
                break
            if line[i].isalpha() and line[i+1].isdigit() and line[i+2].isalpha():
                result += line[i] * int(line[i+1])
            if line[i].isalpha() and line[i+1].isdigit() and line[i+2].isdigit():
                result += line[i] * int(line[i+1] + line[i+2])
        file_out.write(result)    