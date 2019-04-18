import logging
import json
import random
import time

import wx

import wxcef
import 詞空間


def js(x):
    真山彥.窗口.browser.ExecuteJavascript(x)


class 山彥:
    def __init__(self, 窗口):
        self.窗口 = 窗口
        self.詞空間 = 詞空間.詞空間()
        self.詞空間鏈 = self.詞空間.線程造鏈('abandon')

    def 產生混淆組(self):
        l = list(self.詞空間.單詞表)
        return [self.詞空間.意思(random.choice(l)) for i in range(3)]

    def 初始化(self):
        單詞 = next(self.詞空間鏈)
        js(f'''
        畫面.入詞({json.dumps(next(self.詞空間鏈))});
        畫面.來(
            {json.dumps(next(self.詞空間鏈))},
            {json.dumps(self.產生混淆組())}
        )'''
        )

    def 下一題(self):
        單詞 = next(self.詞空間鏈)
        js(f'''
        畫面.來(
            {json.dumps(next(self.詞空間鏈))},
            {json.dumps(self.產生混淆組())}
        )'''
        )


app, 瀏覽器 = wxcef.group(title='Invoker～祈求者～', url='file:///html/主頁.html', icon='./html/Invoke_icon.ico', size=(1366, 768))
真山彥 = 山彥(app.frame)
app.frame.set_browser_object("山彥", 真山彥)
app.MainLoop()
