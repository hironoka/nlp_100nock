# [wip]
# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

import sys

x = int(sys.argv[1])
with open('hightemp.txt') as f:
    lines = f.readlines()
    # n = len(lines) / x

# print((',').join(lines)

for n, line in enumerate(lines)
    e = (n + 1) % x
    with open('col%s.txt' % e,'w') as f: f.write(line)


# argvとは？？？何と読めばいいのか
# if __name__ == '__main__':がよくわからない


# test
# $ split -l 3 hightemp.txt
