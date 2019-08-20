import pickle
import copy
import threading
import time

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

    def 造鏈(self, x):
        單詞假表 = copy.copy(self.單詞表)
        del 單詞假表[x]
        while True:
            這個 = max(單詞假表,
                     key=lambda i: self.比對(i, x))
            del 單詞假表[這個]
            yield {'單詞': 這個, '意思': self.單詞表[這個]['意思'], '轉移相似': self.比對(x, 這個)}
            x = 這個

    def 線程造鏈(self, x):
        緩衝區 = []

        def 線程():
            f = self.造鏈(x)
            while True:
                if len(緩衝區) < 3:
                    緩衝區.append(next(f))
                else:
                    time.sleep(0.1)

        t = threading.Thread(target=線程)
        t.setDaemon(True)
        t.start()
        while True:
            if 緩衝區:
                yield 緩衝區.pop(0)
            else:
                time.sleep(0.1)


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

    鏈 = t.線程造鏈('abandon')
    for i in range(50):
        詞 = next(鏈)
        print('')
        print(詞['單詞'], 詞['意思'])

    # import tqdm
    # with open('鏈1000.txt','w',encoding='utf8') as f:
    #     鏈 = t.造鏈('abandon')
    #     for i in tqdm.tqdm(range(1000),ncols=50):
    #         單詞, _ = next(鏈)
    #         f.write('\n')
    #         f.write(單詞+'\n')
    #         f.write(t.意思(單詞)+'\n')
