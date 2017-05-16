# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

with open('hightemp.txt', 'r') as f: lines = f.readlines()
for line in lines:
    print(line.replace('\t', ' '), end = '')


# test
# $ sed s/$'\t'/' '/g hightemp.txt
# $ tr '\t' ' ' < hightemp.txt
# $ expand -t 1 sample.txt
