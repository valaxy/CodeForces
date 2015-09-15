require('../../base/mock')

var data = [
    ['1', 'YES'],
    ['2', 'NO'],
    ['3', 'YES'],
    ['500', 'NO']
]

data.forEach(function(point) {
    input = point[0]
    reload('./a')
    assert.equal(point[1], output)
})
