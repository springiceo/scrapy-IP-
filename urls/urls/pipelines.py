# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# import os
# import codecs
# import json
#
#
class UrlsPipeline(object):
#     count=0
#     def __init__(self):
#         # 必须使用 w+ 模式打开文件，以便后续进行 读写操作（w+模式，意味既可读，亦可写）
#         # 注意：此处打开文件使用的不是 python 的 open 方法，而是 codecs 中的 open 方法
#         self.json_file = codecs.open('url_51job.json', 'w+', encoding='UTF-8')
#
#     # 爬虫开始时执行的方法
#     def open_spider(self,spider):
#         # 在爬虫开始时首先写入一个[号，构造一个jspn数组
#         # 使json文件具有更高的易读性，每次换行
#         self.json_file.write('[\n')
#
#     # 爬虫pipeline接收到scrapy引擎发送的item数据时执行
#     def process_item(self, item, spider):
#         # 将item转换为字典类型，并编码为json字符串，写入文件
#         # 为使json易读,输出\t和\n
#         item_json = json.dumps(dict(item),ensure_ascii=False)
#         self.json_file.write('\t' + item_json + ',\n')
#         count=self.count+1
#         print('正在写入第'+count+'条')
#         return item
#
#     # 爬虫结束时执行方法
#     def close_splider(self,spider):
#         # 在结束后，需要对 process_item 最后一次执行输出的 “逗号” 去除
#         # 当前文件指针处于文件尾，我们需要首先使用 SEEK 方法，定位到文件尾前的两个字符（一个','(逗号), 一个'\n'(换行符)）的位置
#         self.json_file.seek(-2,os.SEEK_END)
#         # 使用 truncate() 方法，将后面的数据清空
#         self.json_file.truncate()
#         # 重新输出'\n'，并输出']'，与 open_spider(self, spider) 时输出的 '[' 相对应，构成一个完整的数组格式
#         self.json_file.write('\n]')
#         # 关闭文件
#         self.json_file.close()

    def process_item(self, item, spider):
        return item
