
board = [
    # ['C', 'A', 'T', 'F', 'Z', 'K', 'L'],
    # ['B', 'G', 'E', 'S', 'E', 'A', 'U'],
    # ['I', 'T', 'A', 'E', 'P', 'F', 'M'],
    # ['S', 'E', 'A', 'T', 'N', 'Q', 'H'],
    ['T', 'F', 'Z', 'E', 'L', 'E', 'J'],
    ['A', 'I', 'W', 'O', 'D', 'J', 'A']
]

word = 'AJ'

def search_char_index(board, word):
    char_num = 0
    for char in list(word):
        char_num += 1
        for i, _ in enumerate(board):
            char_index = 0
            for search_char in board[i]:
                if char == search_char:
                    index = [i, char_index]
                    search_next_char(index, char_num)
                char_index += 1

def search_next_char(index, char_num):
    i, j = index
    next_char_indexes = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
    for i, j in next_char_indexes:
        if word[char_num + 1] == board[i][j]:
            correct_index = [i, j]
            char_num += 1
            return search_next_char(correct_index, char_num)
# def search_word(indexes):
#     char_num = 0
#     char_pos_list = indexes[char_num]
#     for char_num in range(len(indexes)):
#         i, j = char_pos_list[0]
#         next_chars = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
#         char_pos_list.clear()
#         for next_char in next_chars:
#             for char in indexes[char_num + 1]:
#                 if next_char == char:
#                     char_pos_list.append(next_char)
#         char_num += 1
#         # if char_pos_list:
#         #     char_num += 1
#         # else:
#         #     print(False)
#         #     break
#     if char_pos_list:   
#         print(True)


search_char_index(board, word)

# assert function(board_, word='BEC') is False
# assert function(board_, word='SEAT')
# assert function(board_, word='TEA')
# assert function(board_, word='AGTAI') is False
# assert function(board_, word='AJEQNTEAEGBC')
# assert function(board_, word='KAFQEJ')
# assert function(board_, word='EASTE') is False
# assert function(board_, word='CAGTAI') is False