import os
import json
import random
import logging
import threading
import time

import 詞空間
import 牛津英漢


class 詞源(詞空間.詞空間):
    def __init__(self):
        if os.path.isfile('./程序資料/切詞.json'):
            with open('./程序資料/切詞.json') as f:
                self.切詞表 = json.load(f)
        else:
            self.切詞表 = []

        super().__init__()

        for 單詞 in self.切詞表:
            if 單詞 in self.單詞表:
                del self.單詞表[單詞]
            else:
                logging.warning(f'單詞表沒有「{單詞}」')

    def 切(self, 單詞):
        self.切詞表.append(單詞)
        self.存檔()

    def 存檔(self):
        with open('./程序資料/切詞.json', 'w') as f:
            json.dump(list(set(self.切詞表)), f)

    def 產生混淆組(self):
        l = list(self.單詞表)
        return [self.意思(random.choice(l)) for i in range(3)]
        
    def 單詞信息(self, 單詞):
        t = super().單詞信息(單詞)
        t['例句'] = 牛津英漢.選取例句(單詞)
        return t
        
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
    t = 詞源()

    鏈 = t.造鏈('abandon')
    for i in range(50):
        詞 = next(鏈)
        print('')
        print(詞['單詞'], 詞['信息'])