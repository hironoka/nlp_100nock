# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

# a = []
# for line in lines:
#     b = line.split('\t')
#     a.append(b)
# a.sort(key=lambda line:line.split()[2], reverse=True)
# print(a)

with open('hightemp.txt') as f: lines = f.readlines()
for line in sorted(lines, key=lambda line:line.split('\t')[2], reverse=True):
    print(line, end='')


# test
# $ cat hightemp.txt | sort -r -k3
