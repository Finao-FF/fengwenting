"""
print("hello word!") #字符串
print(23333) #整数
print(2.333) #小数
print(True) #布尔值 True False
print(()) #元组
print([]) #数组
print({}) #字典
锄禾日当午
汗滴禾下土
print("hello word!",23333)
print("哈哈"+"嘻嘻") #字符串的拼接
print("哈哈"*100) 
print(((1+2)*100-9.9)/2)
print(2>3)
a="张三" #把张三这个值赋给变量
print(a)

a=input("请输入：") #通过input输入的，均当作字符串处理了，故a+b的结果为10099
b=input("请输入：")
print("input获取的内容：",a+b)
"""
#数据格式的转换
# type() 读取数据的格式
# print(type(2333))
# print(type("哈哈"))
# print(type(2.333))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))

#a=int("23333")
#print(type(a))

#数据格式转换规则
#任何数据都可以转换为字符串
#整数和小数可以互相转换
#字符串转换为其它类型数据，必须满足【长得像】这个规律
#例如，把a=int("一")转换为int是不能实现的。但a=int("23333")是可以实现的

'''
a=input("请输入：") 
b=input("请输入：")
print("input获取的内容：",int(a)+int(b))

# a=float(input("请输入：")) 
# b=float(input("请输入："))
# print("input获取的内容：",a+b)
'''
#len()用于获取字符串、数组、元组、字典的长度
# a="asdfghjkl dfghjkldfghj " #也可以是单引号
# print(len(a))
#通过代码获得两段内容，并且计算他们的长度和
a=input()
b=input()
print(len(a+b))
