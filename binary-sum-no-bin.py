def add_binary(a, b):
    num = a + b
    res = []
    def inner(num):
        if num >= 1:
            inner(num // 2)
            res.append(num % 2)
    inner(num)
    return ''.join(str(i) for i in res)


a_ = int(input('A: '))
b_ = int(input('B: '))
print(add_binary(a_, b_))
