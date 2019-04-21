import os
import json
import random

import 詞空間

class 詞源(詞空間.詞空間):
    def __init__(self,):
        if os.path.isfile('./程序資料/切詞.json'):
            with open('./程序資料/切詞.json') as f:
                self.切詞表 = json.load(f)
        else:
            self.切詞表 = []
            
        super().__init__()
        
        for 單詞 in self.切詞表: 
            del self.單詞表[單詞]        
        
    def 切(self, 單詞):
        self.切詞表.append(單詞)
        self.存檔()
        
    def 存檔(self):
        with open('./程序資料/切詞.json', 'w') as f:
            json.dump(list(set(self.切詞表)), f)
        
    def 產生混淆組(self):
        l = list(self.單詞表)
        return [self.意思(random.choice(l)) for i in range(3)]
        