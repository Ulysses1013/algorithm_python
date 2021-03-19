#素数判定
def prime_number(max):
    numbers = []

    for i in range(2, max + 1):
        flag = True
        for j in numbers:
            if i % j == 0:
                flag = False
                break

        if flag == True:
            numbers.append(i)

    numbers.insert(0, 1)
    return numbers

prime = prime_number(100)
print(prime)
print('-'*10)
# 横に1を足して、縦に２を足して表示するやり方
n=1
num=1
for i in range(5):
    for j in range(5):
        print(n , end=' ')
        n += 1
    print()
    num += 2
    n = num