
# coding: utf-8

# In[1]:

# 00
print "stressed"[::-1]


# In[2]:

# 01
print u'パタトクカシーー'[::2].encode('utf-8')


# In[3]:

# 02
a=u'パトカー'+u'タクシー'
a=a[::4]+a[1::4]+a[2::4]+a[3::4]
print a


# In[4]:

# 03
a="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

a=a.translate(None, ".").split(" ")
print map(lambda x: len(x), a)


# In[43]:

# 04
a="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
b={}

a=a.translate(None, ".").split(" ")
for i, j in enumerate(a):
    n=i+1
    if n in (1, 5, 6, 7, 8, 9, 15, 16, 19):
        b[n]=j[0]
    else:
        b[n]=j[0:2]
print b


# What is splitSource? It is sourceCode.split. Here comes the answer. 
# You should call a method by using (), without which you will get the method itself. 
# The method str.split is obviously not iterable!
# http://stackoverflow.com/questions/30145926/main-loop-builtin-function-or-method-object-is-not-iterable


# In[31]:

#05
a="I am an NLPer"

# def sample(sentence, n):
#     ary=sentence.sprit("")
#     l=ary.len - 1
#     for i, j in enumerate(ary):
#         if i in(0, l):
            
def sample(a, n):
    last = len(a) - n + 1
    ary = []
    for i in range(0, last):
        ary.append(a[i:i+n])
    return ary

sample(a, 2) 


# In[11]:

sample(a.split(), 2)


# In[32]:

#06
a="paraparaparadise"
b="paragraph"


def sample(input, n):
    last = len(input) - n + 1
    ret = []
    for i in range(last):
        ret.append(input[i:i+n])
    return ret

X=set(sample(a, 2))
Y=set(sample(b, 2))

# 和集合　
print X|Y 
# 積集合
print X&Y
# 差集合
print X.difference(Y) 
print Y.difference(X)


# In[51]:

#07
def sample(x, y, z):
    return unicode(x) + u'時の' + unicode(y) + u'は' + unicode(z)
    
x=12
y=u"気温"
z=22.4
print sample(x,y,z)


# In[ ]:

#08
a="testtest"
def cipher(a):


# In[54]:

#09
import random

a="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
b=a.translate(None, ".").split(" ")
first=b[0]
last=b[len(b)-1]
c=b[1:-1]

d=[]
h={}
n=[]

for i, j in enumerate(c):
    if len(j)<4:
        h[i]=j
        n.append(i+1)
    else:
         d.append(j)

random.shuffle(d)
print ", ".join(map(str,n))

for i, j in enumerate(a):
    n=i+1
    if n in (1, 5, 6, 7, 8, 9, 15, 16, 19):
        b[n]=j[0]
    else:
        b[n]=j[0:2]
print b



# e.insert(0, first)
# e.append(last)
# print ' '.join(c)


# In[ ]:




# In[ ]:



