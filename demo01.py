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
'''
a=input()
b=input()
print(len(a+b))
'''
'''
#元组,下标从0开始
a=(1,2,3,4,"哈哈","嘻嘻",True)
print(a[5])
print(a.index("嘻嘻"))
#下标可以倒着数
print(a[-1])
#切片
print(a[0:4]) #左闭右开
print(a[:4]) #等价于print(a[0:4])，若左侧为元组中的第一个数，可省略不写
print(a[4:]) #等价于print(a[4:7])，
print(a[4:7])
#二维元组
#b=(a,"哈哈","嘻嘻")
#print(b[1])
# print(b[0][3])
'''
'''
#数组 元组写好过后，不可修改，数组可以修改
a=[1,2,3,4,"哈哈","嘻嘻",True]
a.append("append") #往数组中追加数据
#print(a)
#print(a.index("哈哈"))
#print(a.count("嘻嘻"))
#a.insert(0,"insert") #在数组的任意位置中插入数据
print(a)
#a.pop() #剪切的作用
b=a.pop(3) #括号里的内容为下标
print(b)
c=a.pop(2)
print(b+c)
#a.clear() #清空数组
#xx=["你好","在的"]
#a.extend(xx) #合并数组
#print(a)
#print(a+xx)
#a.remove("你好") #删除
#print(a)

#True=1
#False=0
#xx=[0,1,False,True]
#print(xx.count(0))
'''
#########
#所有的方法都是小括号结尾。比如，print(),input(),len()
#元组，数组，字典的取值，都是用中括号，比如a[0]
#元组、数组以及字典的定义分别是(),[],{}
###############

###################字典############################
#字典的特点：
#1.字典中的值没有顺序
#2.字典的结构必须是键值对的结构。key:value
#3.字典是通过key值取的value
#任何地方的字符串都是需要加引号的，除了update(),例如a.update(name=3333)，a.update(name="哈哈")把name当作一个变量
'''
a={"name":"zhanhsan",
    0:"哈哈",
   "age":25}
#取值
print(a["name"])
#新增
a["high"]="183cm"
print(a)
#修改
a["name"]="李四"
print(a)

# get
b=a.get("name")
print(b)
#pop 
b=a.pop("name")
print(b)
print(a)
print("--------------------------------")
# update
a.update(name=3333)  #若key存在，则实现修改功能，若key不存在则实现新增功能
print(a)
print("--------------------------------")
#数组和字典的删除
del a["name"]
print(a)

del a[0]
'''
'''
练习：
获取用户输入的个人信息，并且存储到字典中。
个人信息包括：name，age，sex

a=input("请输入你的姓名：")
b=input("请输入你的年龄：")
c=input("请输入你的性别：")
#d={}
#d.update(name=a,age=b,sex=c)
#d["name"]=a
#d["age"]=b
#d["sex"]=c
d={"name":a,"age":b,"sex":c}
print(d)
'''




