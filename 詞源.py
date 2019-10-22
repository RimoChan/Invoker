import os
import json
import random
import logging
import threading
import time
import copy

import 詞空間
import 牛津英漢


class 詞源(詞空間.詞空間):
    def __init__(self):
        if os.path.isfile('./程序資料/切詞.json'):
            with open('./程序資料/切詞.json') as f:
                self.切詞表 = set(json.load(f))
        else:
            self.切詞表 = set()

        self.權重懲罰表 = {}
        self.權重懲罰 = {'初始': -1, '回復': 1 / 16}

        super().__init__()

    def 切(self, 單詞):
        self.切詞表.add(單詞)
        self.存檔()

    def 存檔(self):
        with open('./程序資料/切詞.json', 'w') as f:
            json.dump(list(self.切詞表), f)

    def 產生混淆組(self):
        l = list(self.單詞表)
        return [self.意思(random.choice(l)) for i in range(3)]

    def 單詞信息(self, 單詞):
        t = super().單詞信息(單詞)
        t['例句'] = 牛津英漢.選取例句(單詞)
        return t

    def 造鏈(self, 起始):
        單詞假表 = copy.copy(self.單詞表)
        del 單詞假表[起始]
        x = 起始
        while True:
            這個 = max(單詞假表, key=lambda i:
                     -(i in self.切詞表) or
                     self.比對(i, x) + self.權重懲罰表.get(i, 0) + random.random()/32)

            for 單詞, 權重 in tuple(self.權重懲罰表.items()):
                self.權重懲罰表[單詞] += self.權重懲罰['回復']
                if 權重 > 0:
                    del self.權重懲罰表[單詞]
            self.權重懲罰表[這個] = self.權重懲罰['初始']

            yield {'單詞': 這個, '信息': self.單詞信息(這個), '轉移相似': self.比對(x, 這個)}
            x = 這個

    def 線程造鏈(self, x):
        緩衝區 = []

        def _線程():
            f = self.造鏈(x)
            while True:
                if len(緩衝區) < 3:
                    緩衝區.append(next(f))
                else:
                    time.sleep(0.1)

        t = threading.Thread(target=_線程)
        t.setDaemon(True)
        t.start()
        while True:
            if 緩衝區:
                yield 緩衝區.pop(0)
            else:
                time.sleep(0.1)


if __name__ == '__main__':
    t = 詞源()

    鏈 = t.造鏈('yield')
    d = {}
    for i in range(500):
        詞 = next(鏈)
        print(i, 詞['單詞'])
        if 詞['單詞'] in d:
            print(d[詞['單詞']])
        else:
            d[詞['單詞']] = i
