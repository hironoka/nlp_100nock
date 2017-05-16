# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

# with open('hightemp.txt', 'r') as f: line = f.readline()
# with open('col1.txt','w')      as f: f.write(line)

for i in [1, 2]:
    with open('hightemp.txt', 'r') as f: line = f.readlines()[i - 1]
    with open('col%s.txt' % i,'w') as f: f.write(line)

# test
# $ cut hightemp.txt ????
