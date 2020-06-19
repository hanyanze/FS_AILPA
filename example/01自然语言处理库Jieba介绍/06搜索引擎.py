import os
import shutil

from whoosh.fields import *
from whoosh.index import create_in
from whoosh.qparser import QueryParser
from jieba.analyse import ChineseAnalyzer


analyzer = ChineseAnalyzer()

schema = Schema(title=TEXT(stored=True),
                path=ID(stored=True),
                content=TEXT(stored=True,
                             analyzer=analyzer))
if not os.path.exists("test"):
    os.mkdir("test")
else:
    # 递归删除目录
    shutil.rmtree("test")
    os.mkdir("test")

idx = create_in("test", schema)
writer = idx.writer()

writer.add_document(
    title=u"document1",
    path="/tmp1",
    content=u"Tracy McGrady is a famous basketball player, the elegant basketball style of him attract me")
writer.add_document(
    title=u"document2",
    path="/tmp2",
    content=u"Kobe Bryant is a famous basketball player too , the tenacious spirit of him also attract me")
writer.add_document(
    title=u"document3",
    path="/tmp3",
    content=u"LeBron James is the player i do not like")

writer.commit()
searcher = idx.searcher()
parser = QueryParser("content", schema=idx.schema)

for keyword in ("basketball", "elegant"):
    print("searched keyword ",keyword)
    query= parser.parse(keyword)
    results = searcher.search(query)
    for hit in results:
        print(hit.highlights("content"))
    print("="*50)
