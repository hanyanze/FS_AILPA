import jieba


# 全匹配
seg_list = jieba.cut("今天哪里都没去，在家里睡了一天", cut_all=True)
print(list(seg_list))  # ['今天', '哪里', '都', '没去', '', '', '在家', '家里', '睡', '了', '一天']
# 精确匹配 默认模式
seg_list = jieba.cut("今天哪里都没去，在家里睡了一天", cut_all=False)
print(list(seg_list))  # ['今天', '哪里', '都', '没', '去', '，', '在', '家里', '睡', '了', '一天']
# 精确匹配
seg_list = jieba.cut_for_search("今天哪里都没去，在家里睡了一天")
print(list(seg_list))  # ['今天', '哪里', '都', '没', '去', '，', '在', '家里', '睡', '了', '一天']
