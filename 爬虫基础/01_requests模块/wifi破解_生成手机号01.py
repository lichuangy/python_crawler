import itertools as its
import datetime

# 记录程序运行时间
start = datetime.datetime.now()

words = '1234567890abcdefghijklmnopqrstuvwxyz'  # 这里可以加入字母和其他字符，使用string包更方便
# 生成密码的位数
r = its.product(words, repeat=8)  # 密码位数为9
dic = open(r"pwd.txt", 'a')
for i in r:
    dic.write(''.join(i))
    dic.write(''.join('\n'))
    print(i)

dic.close()
print('密码本生成好了')
end = datetime.datetime.now()
print("生成密码本一共用了多长时间：{}".format(end - start))