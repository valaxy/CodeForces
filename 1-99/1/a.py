# encoding = utf-8
# 数学 > 离散数学 > 排列组合


def read():
    s = input()
    s = s.split(' ')
    s = [int(x) for x in s]
    return s


def write(out):
    print(out)


def calc(n, a):
    if n % a == 0:
        return n // a
    else:
        return n // a + 1


def solve(n, m, a):
    return calc(n, a) * calc(m, a)


if __name__ == '__main__':
    data = read()
    data = solve(data[0], data[1], data[2])
    write(data)



