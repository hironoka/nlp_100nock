# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

# print('\t'.join([line1, line2]).replace('\n', ''))

with open('col1.txt', 'r') as f1, open('col2.txt') as f2:
    content = ((f1.readline() + f2.readline()).replace('\n', '\t'))
with open('merge.txt', 'w') as f: f.write(content)

# with open('merge.txt', 'w') as f:
#     with open('col1.txt', 'r') as f1, open('col2.txt') as f2:
#         content = ((f1.readline() + f2.readline()).replace('\n', '\t'))
#     f.write(content)

# withはネストしない方が良いのでしょうか？

# test
# $ paste col1.txt col2.txt
