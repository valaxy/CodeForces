from b import *


assert countInBit(1) == MAX_NUMBER
assert countInBit(2) == MAX_NUMBER * MAX_NUMBER

assert countBeforeBit(1) == MAX_NUMBER
assert countBeforeBit(2) == MAX_NUMBER + MAX_NUMBER * MAX_NUMBER

assert convert10To26(0, 1) == 'A'
assert convert10To26(25, 2) == 'AZ'
assert convert10To26(26, 2) == 'BA'

assert rcToExcel(55, 23) == 'BC23'

assert excelToRC('BC', 23) == 'R23C55'

assert isExcel('BC23')
assert not isExcel('R23C55')

assert solve('R23C55') == 'BC23'
assert solve('BC23') == 'R23C55'
assert solve('R1C1') == 'A1'
assert solve('A1') == 'R1C1'

print('ok')