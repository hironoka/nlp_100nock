# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

# f = open('hightemp.txt', 'r')
# lines = f.readlines()
# print(len(lines))
# f.close()

with open('hightemp.txt', 'r') as f: print(len(f.readlines()))


# test
# $ wc
