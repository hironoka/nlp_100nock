# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

# a = []
# for line in lines:
#     a.append(line.split('\t')[0])
# words = collections.Counter(''.join(map(lambda line: line.split('\t')[0], lines)))
# print(c)

from collections import Counter

with open('hightemp.txt') as f: lines = f.readlines()
words = Counter(map(lambda line: line.split('\t')[0], lines))
for word, count in words.most_common(): 
    print(word)


# test ちょっとよくわからない
# $ cut -f1 hightemp.txt | sort | uniq -c | sort -r | cut -c 6-
