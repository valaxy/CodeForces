var n = Number(readline())
var i = 1
while (true) {
    if (i * (i+1) / 2 == n) {
        print('YES')
        break
    }

    if (i * (i+1) / 2 > n) {
        print('NO')
        break
    }

    i++
}
