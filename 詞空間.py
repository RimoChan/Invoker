import pickle
import copy

import numpy as np
# import sklearn.decomposition
# import sklearn.preprocessing


class 詞空間:
    def __init__(self):
        with open('./詞典資料/考研5500詞彙.pkl', 'rb')as f:
            self.單詞表 = pickle.load(f)
        # self.PCA化()

    # def PCA化(self):
    #     單詞列 = []
    #     向量列 = []
    #     for 單詞, 信息 in self.單詞表.items():
    #         單詞列.append(單詞)
    #         向量列.append(信息['向量'])
    #     pca = sklearn.decomposition.PCA(n_components=2, whiten=True).fit(向量列)
    #     X = pca.transform(向量列)
    #     min_max_scaler = sklearn.preprocessing.MinMaxScaler()
    #     X = min_max_scaler.fit_transform(X)
    #     for 單詞, 二維向量 in zip(單詞列, X):
    #         self.單詞表[單詞]['二維向量'] = tuple(二維向量)

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


if __name__ == '__main__':
    t = 詞空間()

    t.交叉測試('science', 'none', 'mortal', 'electrical')
