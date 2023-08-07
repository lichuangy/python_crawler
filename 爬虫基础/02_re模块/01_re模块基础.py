"""

Python中的re模块提供了正则表达式的各种操作函数,常见和常用的方法包括:
- re.match - 从字符串开头匹配正则表达式,返回匹配对象
- re.search - 在字符串中搜索匹配正则表达式的第一个位置,返回匹配对象
- re.findall - 查找字符串中所有的匹配,返回列表
- re.split - 根据正则表达式分割字符串,返回列表
- re.sub - 在字符串中替换匹配正则表达式的内容
- re.compile - 编译正则表达式字符串,返回正则表达式对象
- re.fullmatch - 完全匹配整个字符串,返回匹配对象
- re.finditer - 查找字符串中所有的匹配,返回迭代器
- re.purge - 清空正则表达式的缓存
- re.escape - 将特殊字符转义,用于匹配字符串字面值
此外,匹配对象也有一些常用的方法:
- group() - 返回匹配内容
- start() - 返回匹配内容在原字符串的开始索引
- end() - 返回匹配内容在原字符串的结束索引
- span() - 返回匹配内容在原字符串的开始和结束索引

"""
import re

string = 'Hello World!'

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~match 规则：从字符串开头匹配正则表达式,返回匹配对象~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
pattern = r"Hello"
# 情况1:正则匹配字符串开头,匹配成功
m1 = re.match(pattern,string)

# 情况2:正则不匹配字符串开头,匹配失败
m2 = re.match(r"World",string)

# 情况3:正则匹配字符开头0次或者多次,匹配成功
m3 = re.match(r"\w*",string)

# 情况4:^正则匹配开头,匹配成功
m4 = re.match(pattern, string)

print(m4)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~search 规则：在字符串中搜索匹配正则表达式的第一个位置,返回匹配对象~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# 情况1:正则匹配字符串中间部分,成功匹配
s1 = re.search(r"World",string)

# 情况2:正则模式匹配字符串开头,也能成功匹配
s2 = re.search(pattern,string)

# 情况3:使用^锚定开头,匹配失败
pattern = r"^World"
s3 = re.search(pattern,string)

# 情况5:正则匹配字符串末尾,匹配成功
s4 = re.search(r'!',string)

# 情况6:使用$锚定结尾,匹配成功
s5 = re.search(r'!$',string)

print(s5)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~findall 规则：查找字符串中所有的匹配,返回列表~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

string = 'Hello Hello World'
# 情况1:正常匹配,返回列表
fa1 = re.findall(r'Hello',string)

# 情况2:正则没有匹配,返回空列表
pattern = r'abc'
fa2 = re.findall(pattern, string) # []

# 情况3:使用*重复匹配,返回列表
pattern = r'Hel*o'
fa3 = re.findall(pattern, string) # ['Hello', 'Hello']

# 情况4:正则包含组,(())分组匹配
pattern = r'(Hello) World'
fa4 = re.findall(pattern, string) # ['Hello']

print(fa4)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~split, sub~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

string = 'Hello World! 123 456'

# split - 根据正则表达式分割字符串,返回列表
print(re.split(r'\s+', string))
# ['Hello', 'World!', '123', '456']

# sub - 在字符串中替换匹配正则表达式的内容
print(re.sub(r'\d+', 'number', string))
# Hello World! number number
