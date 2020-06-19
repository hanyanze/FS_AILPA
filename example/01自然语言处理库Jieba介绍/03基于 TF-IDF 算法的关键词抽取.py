import jieba.analyse

file = "03.txt"
topK = 12
content = open(file, 'rb').read()

tags = jieba.analyse.extract_tags(content, topK=topK)
print(tags)


# withWeight=True：将权重值一起返回
tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=True)
print(tags)

