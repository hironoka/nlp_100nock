f = open('test.txt', 'w')
lines = f.readlines
for line in lines:
   print(line.replace('\t', ' '), end ='')

# f = open('test.txt', 'w')
# lines = f.readlines()
# print(lines.join(' '))

# 改行コード
# Linux	    \n
# Mac	    \r
# Windows	\r\n
