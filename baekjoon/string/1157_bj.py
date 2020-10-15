# 백준 1157 - 단어 공부
import operator


word = input()
chr_dict = {}

for char in word:
    try:
        if 65 <= ord(char) <= 90:
            chr_dict[char] += 1
        else:
            chr_dict[chr(ord(char)-32)] += 1
    except:
        if 65 <= ord(char) <= 90:
            chr_dict[char] = 1
        else:
            chr_dict[chr(ord(char)-32)] = 1

chr_dict = sorted(chr_dict.items(), key=operator.itemgetter(1), reverse=True)

if len(chr_dict) == 1:
    print(chr_dict[0][0])
elif chr_dict[0][1] == chr_dict[1][1]:
    print('?')
else:
    print(chr_dict[0][0])