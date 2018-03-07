# -*- coding: utf-8 -*-

#此处test.items()包含测试集中的用户和其购买的商品
class test(object):
    def __init__(self, name, items = []):
        self.name = name
        self.items = items

    def add(self,item):
        self.items.append(item)
    def items(self):
        return (self.name,self.items)
    
class user(object):
    def __init__(self, username, chosen = []):
        self.name = username
        self.chosen = chosen
    def add(self,item):
        self.chosen.append(item)



#TopN推荐
#评分预测的预测准确度
#n_recall为召回率，n_precision为准确率
#rank为推荐列表，test.item为用户在测试集上的行为列表
def PrecisionRecall(test, N):
    hit = 0
    n_recall = 0
    n_precision = 0
    for user, items in test.items():
        rank = Recommend(user, N)
        hit += len(rank & items)
        n_recall += len(items)
        n_precision += N
    return [hit / (1.0 * n_recall), hit / (1.0 * n_precision)]
#通过基尼系数计算覆盖率
def GiniIndex(p):
    j = 1
    n = len(p)
    G = 0
    for item, weight in sorted(p.items(), key=itemgetter(1)):
        G += (2 * j - n - 1) * weight
    return G / float(n - 1)

def Recommend(user, N):
   return 'Harry Potter'
    
#t = test(1,('Harry Potter','A Farewell to Arms','A Midsummer Night','A Tale of Two Cities'))
l = ('Harry Potter','A Farewell to Arms','A Midsummer Night','A Tale of Two Cities')


#print(PrecisionRecall(t,3))
u = user('gaoyutong')
u.add('HarryPotter')

t = test(u.name)
for item in l:
    t.add(item)

print(PrecisionRecall(t, 1))



