import re

MAX_NUMBER = 26

countInBitArray = [1]


# how many string in w-len
def countInBit(w):
    if w >= len(countInBitArray):
        count = countInBit(w - 1) * MAX_NUMBER
        countInBitArray.append(count)
    return countInBitArray[w]


countBeforeBitArray = [0]


# how many string before and in w-len, w >= 1
def countBeforeBit(w):
    if w >= len(countBeforeBitArray):
        count = countBeforeBit(w - 1) + countInBit(w)
        countBeforeBitArray.append(count)
    return countBeforeBitArray[w]


# 10 to 26
def convert10To26(x, w):
    s = ''
    for i in range(0, w):
        s = chr(x % MAX_NUMBER + 65) + s
        x //= MAX_NUMBER
    return s


def rcToExcel(column, row):
    w = 1
    while True:
        if column <= countBeforeBit(w):
            break
        w += 1  # w is len of columnStr
    column -= countBeforeBit(w - 1)

    s = convert10To26(column - 1, w)  # AAA is 0-th
    return s + str(row)


def excelToRC(columnStr, row):
    column = 0
    for i in range(0, len(columnStr)):
        column = column * MAX_NUMBER + ord(columnStr[i]) - 65
    column += countBeforeBit(len(columnStr) - 1) + 1
    return 'R' + str(row) + 'C' + str(column)


def solve(coord):
    if isExcel(coord):
        match = re.match('([A-Z]+)(\d+)', coord)
        column = match.group(1)
        row = int(match.group(2))
        return excelToRC(column, row)
    else:  # RC
        match = re.match('R(\d+)C(\d+)', coord)
        row = int(match.group(1))
        column = int(match.group(2))
        return rcToExcel(column, row)


def isExcel(coord):
    match = re.match('^[A-Z]+\d+$', coord)
    return match


def read():
    n = int(input())
    l = []
    for i in range(0, n):
        coord = input()
        l.append(solve(coord))
    return l


def write(l):
    for i in range(0, len(l)):
        print(l[i])


if __name__ == '__main__':
    a = read()
    write(a)
