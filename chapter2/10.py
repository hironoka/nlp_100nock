# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

# with open('hightemp.txt', 'r') as f:
#     lines = f.readlines()
#     print(len(lines))

with open('hightemp.txt', 'r') as f:
    line = f.readline()
    i = 0
    while line:
        i = i + 1
        line = f.readline()
print(i)


# test
# $ wc hightemp.txt
