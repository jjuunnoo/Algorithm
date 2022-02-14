# 크로아티아 알파벳
cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
word_count = 0
word_len = len(word)

for i in cro_list:
    if word.count(i) != 0:
        if i=='dz=':
            word_len -= (word.count(i))*3
            word_count += word.count(i)
        elif i=='z=':
            word_len -= (word.count(i)-word.count('dz='))*2
            word_count += (word.count(i)-word.count('dz='))
        else:
            word_len -= (word.count(i))*2
            word_count += word.count(i)
    else:
        pass
word_count += word_len
print(word_count)



# cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = input()
# for i in cro_list:
#     if i in word:
#         word = word.replace(i, '*')
# print(len(word))

# word = input()
# changes = ['=', '-', 'lj', 'nj', 'dz=']
# total = len(word)

# for change in changes:
#     total -= word.count(change)
# print(total)