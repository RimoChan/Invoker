import pickle
import copy

import numpy as np


class 詞空間:
    def __init__(self):
        with open('./詞典資料/考研5500詞彙.pkl', 'rb')as f:
            self.單詞表 = pickle.load(f)

    def 比對(self, x, y):
        x = self.單詞表[x]['向量']
        y = self.單詞表[y]['向量']
        return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y) + 0.000001)

    def 意思(self, x):
        return self.單詞表[x]['意思']

    def 交叉測試(self, *l):
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                print('%12s %12s  %.2f' % (l[i], l[j], self.比對(l[i], l[j])))

    def 最近鄰(self, x):
        單詞假表 = copy.copy(self.單詞表)
        del 單詞假表[x]
        return max(單詞假表,
                   key=lambda i: self.比對(i, x))

    def 最遠(self, x):
        單詞假表 = copy.copy(self.單詞表)
        del 單詞假表[x]
        return min(單詞假表,
                   key=lambda i: self.比對(i, x))

    def 單詞信息(self, 單詞):
        t = copy.copy(self.單詞表[單詞])
        del t['向量']
        return t

    def 造鏈(self, x):
        單詞假表 = copy.copy(self.單詞表)
        del 單詞假表[x]
        while True:
            這個 = max(單詞假表,
                     key=lambda i: self.比對(i, x))
            del 單詞假表[這個]
            yield {'單詞': 這個, '信息': self.單詞信息(這個), '轉移相似': self.比對(x, 這個)}
            x = 這個


if __name__ == '__main__':
    t = 詞空間()

    # t.交叉測試('science', 'philosophy', 'chemical', 'electrical', 'clever')
    #
    # for i in range(10):
    #     import random
    #     l = list(t.單詞表)
    #     r = random.randint(0,len(l))
    #     c = l[r]
    #     print(c,t.意思(c))

    鏈 = t.造鏈('abandon')
    for i in range(50):
        詞 = next(鏈)
        print('')
        print(詞['單詞'], 詞['信息'])

    # import tqdm
    # with open('鏈1000.txt','w',encoding='utf8') as f:
    #     鏈 = t.造鏈('abandon')
    #     for i in tqdm.tqdm(range(1000),ncols=50):
    #         單詞, _ = next(鏈)
    #         f.write('\n')
    #         f.write(單詞+'\n')
    #         f.write(t.意思(單詞)+'\n')
