var _reload = require('require-reload')(require),
    path = require('path')

global.reload = function(p) {
    p = path.join(path.dirname(require.main.filename), p)
    _reload(p)
}

global.assert = require('assert')

global.input
global.readline = function () {
    return input
}

global.output
global.print = function (data) {
    output = data
}
