import jieba

result = jieba.tokenize('今天哪里都没去，在家里睡了一天')
for tk in result:
    print("word:" + tk[0] +
          " start:" + str(tk[1]) +
          " end:" + str(tk[2]))
    
"""
word:华为技术有限公司 start:0 end:8
word:的 start:8 end:9
word:手机 start:9 end:11
word:品牌 start:11 end:13
"""


# 使用 search 模式
result = jieba.tokenize('华为技术有限公司的手机品牌', mode="search")
for tk in result:
    print("word:" + tk[0] +
          " start:" + str(tk[1]) +
          " end:" + str(tk[2]))
"""
输出：
word:华为 start:0 end:2
word:技术 start:2 end:4
word:有限 start:4 end:6
word:公司 start:6 end:8
word:华为技术有限公司 start:0 end:8
word:的 start:8 end:9
word:手机 start:9 end:11
word:品牌 start:11 end:13
"""
