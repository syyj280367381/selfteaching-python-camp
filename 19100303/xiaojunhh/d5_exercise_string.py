# 原始文本
text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

# 将全部better变换为worse 第一次以为要从本地txt文件中修改
text1 = text.replace("better","worse")
# 大写字母转换成小写，小写转换成大写
text2=text1.swapcase()
print(text2)
# 剔除标点，将所有单词按a…z升序排列，同时转换为列表
list2=text2.split()


# 剔除包含‘ea’的英文单词，同时将列表转换为字符串
for i in list2:
    if "EA" in i:
        del i
print(list2)
list2.sort()
print(list2)