T = int(input())

for ts in range(1, T+1):
    print('#%d'%ts)
    words = [[] for _ in range(5)]
    word_len = [0] * 5
    for i in range(5):
        words[i] = input()
        word_len[i] = len(words[i])

    max_len = max(word_len)

    for j in range(5):
        temp = '!'*(max_len-word_len[j])
        words[j] = words[j] + temp
    
    for k in range(max_len):
        for l in range(5):
            if words[l][k] != '!':
                print(words[l][k], end='')