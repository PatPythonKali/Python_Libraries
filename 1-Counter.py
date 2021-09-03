from collections import Counter

# Integer List
int_list = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4]
# print(Counter(int_list))
# Word List
word_list = ['aaaaaaaabbbbbbbbccc']

# print(c)
# Sentence
sentence = "How many times does each word show up in this sentence with a word"
# print(Counter(sentence.lower().split()))
c = Counter(sentence.replace(' ',''))
# print(c.most_common(4))

sentence = sentence.split()
print(Counter(sentence).most_common(3))