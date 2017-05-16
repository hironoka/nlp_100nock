# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

with open('hightemp.txt') as f: lines = f.readlines()
print(set(map(lambda line: line.split('\t')[0], lines)))


# test
# $ cut -f 1 hightemp.txt | sort | uniq
