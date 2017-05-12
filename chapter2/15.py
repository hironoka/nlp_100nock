# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

import sys

N = int(sys.argv[1])
with open('hightemp.txt', 'r') as f: lines = f.readlines()
for i in range(len(lines) - N, len(lines)): print(lines[i], end='')


# test
# $ cat hightemp.txt | tail -3
