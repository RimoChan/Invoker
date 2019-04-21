import logging
import json

import wxcef
import 詞源


def js(x):
    真山彥.窗口.browser.ExecuteJavascript(x)


class 山彥:
    def __init__(self, 窗口):
        self.窗口 = 窗口
        self.詞源 = 詞源.詞源()
        self.詞鏈 = self.詞源.線程造鏈('abandon')

    def 初始化(self):
        單詞 = next(self.詞鏈)
        js(f'''
        畫面.入詞({json.dumps(next(self.詞鏈))});
        畫面.來(
            {json.dumps(next(self.詞鏈))},
            {json.dumps(self.詞源.產生混淆組())}
        )'''
        )

    def 下一題(self):
        單詞 = next(self.詞鏈)
        js(f'''
        畫面.來(
            {json.dumps(next(self.詞鏈))},
            {json.dumps(self.詞源.產生混淆組())}
        )'''
        )

    def 切(self, 單詞):
        self.詞源.切(單詞)
        
    def 切換全屏(self):
        self.窗口.toggleFullScreen()

app, 瀏覽器 = wxcef.group(title='Invoker～祈求者～', url='file:///html/主頁.html', icon='./html/Invoke_icon.ico', size=(1366, 768))
真山彥 = 山彥(app.frame)
app.frame.set_browser_object("山彥", 真山彥)
app.MainLoop()
