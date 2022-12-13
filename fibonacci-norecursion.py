def fib(range):
    num = [0, 1]
    while len(num) < range:
        num.append(num[-1] + num[-2])

    print(num)




