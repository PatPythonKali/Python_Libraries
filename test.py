from collections import Counter

# my_list = ['a', 'a', 'a', 'b', ]
#
# x = Counter(my_list)
# print(x)

word_list = 'aaaaaaaabbbbbbbbccc'

for x in word_list:
    print(Counter(x))
