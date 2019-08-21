import pickle
import random
import time
import os
import re

from mdict_utils.base.readmdict import MDX


def 轉換():
    g = MDX('./詞典資料/原始資料/牛津高阶英汉双解 第7版.mdx').items()

    詞典 = {key.decode(): value.decode() for key, value in g}

    with open('./詞典資料/牛津高阶英汉双解 第7版.pkl', 'wb') as f:
        f.write(pickle.dumps(詞典))


if not os.path.isfile('./詞典資料/牛津高阶英汉双解 第7版.pkl'):
    轉換()

with open('./詞典資料/牛津高阶英汉双解 第7版.pkl', 'rb') as f:
    詞典 = pickle.load(f)


def 全部例句(單詞):
    # 似乎negligible有bug？
    if 單詞 in 詞典:
        nya = '<SPAN style="color:#008080">(?:&nbsp;)*(.*?)</SPAN><br><font style="color:grey;">(?:&nbsp;)*(.*?)</font>'
        return re.findall(nya, 詞典[單詞])
    else:
        return []


def 選取例句(單詞, 字數控制=60):
    例句組 = 全部例句(單詞)
    if not 例句組:
        return None
        
    參考長度 = lambda x: len(re.sub('<.*?>', '', x[0]))
    
    例句組.sort(key=參考長度)
    if len(例句組[0][0]) > 字數控制:
        return 例句組[0]

    有效例句組 = [例句 for 例句 in 例句組 if 參考長度(例句) <= 字數控制]
    return random.choice(有效例句組)


