import jieba
import jieba.posseg as pseg

# 默认模式
seg_list = pseg.cut("今天哪里都没去，在家里睡了一天")
for word, flag in seg_list:
    print(word + " " + flag)
   
"""
使用 jieba 默认模式的输出结果是：
我 r
Prefix dict has been built successfully.
今天 t
吃 v
早饭 n
了 ul
"""

# paddle 模式
words = pseg.cut("我今天吃早饭了",use_paddle=True)
"""
使用 paddle 模式的输出结果是：
我 r
今天 TIME
吃 v
早饭 n
了 xc
"""
