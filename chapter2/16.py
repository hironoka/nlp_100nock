# [wip]
# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

import sys

input = int(sys.argv[1])
with open('hightemp.txt') as f: lines = f.readlines()
count = int(len(lines)/input)
amari = len(lines) % input

print(count)

a = [x for x in range(len(lines) + amari) if x % count == 0]
print(a)
for i in a:
    if i != len(lines):
        print(lines[i:i+count])
    else:


# test
# $ split -l 3 hightemp.txt
