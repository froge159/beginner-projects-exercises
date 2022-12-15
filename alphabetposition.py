def alphabet_pos(text):
    ans = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
    for i in text.lower():
        if i.isalpha() == True:
            for k in alphabet:
                if i == k:
                     ans.append(alphabet.index(k) + 1)
        else:
            pass
    res = ' '.join(str(x) for x in ans)
    return res

input = input('')
print(alphabet_pos(input))



