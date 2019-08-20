import numpy as np
import pickle


import gluonnlp.embedding
import json

w = gluonnlp.embedding.Word2Vec()

with open('./資料/原始資料/考研5500詞彙.json', encoding='utf8') as f:
    單詞表 = json.load(f)

# for 單詞, 意思 in 單詞表.items():
#     單詞表[單詞] = {'意思':意思, '向量': w.idx_to_vec[w.token_to_idx[單詞]].asnumpy().tolist()}
# with open('CET4向量表.json', 'w', encoding='utf8') as f:
#     json.dump(單詞表, f, ensure_ascii=False)

for 單詞, 意思 in 單詞表.items():
    單詞表[單詞] = {'意思': 意思, '向量': w.idx_to_vec[w.token_to_idx[單詞]].asnumpy()}
with open('./資料/考研5500詞彙.pkl', 'wb') as f:
    pickle.dump(單詞表, f)

# a=單詞表
# while True:
#     try:
#         print(eval(input('>>>')))
#     except Exception as e:
#         print(e)
