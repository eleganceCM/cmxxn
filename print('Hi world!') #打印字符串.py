print('Hi world!') #打印字符串
print("Hi world!")
print(","*80)
print("我喜欢你！")
print("Everybody should learn how to become  a  good people, because it is important  for himself!")
print("加：",3+6) 
print("减：",5-1)
print("乘：",3*6)
print("除：", 3/7)
print("整除：", 9//2)
print("余数：", 3%1)
print("幂：",3**4)
x=7
func=3*x+8 #当程序逐行从上至下运行时，注意变量定义的顺序
print(func)
x=4.0
monadic_equation=4*x+3
print("monadic_equation=",monadic_equation)
print("monadic_equation=%.2f"%monadic_equation) #%字符串格式化方法
print("monadic_equation={:.2f}".format(monadic_equation)) #format()字符串格式化方法
city_name="Beijing"
coordinate_longitude=115.7
coordiante_latitude=39.4
print("The longitude of the Beijing coordinate is {lon:.2f}, and the latitude is {lat}.".format(lon=coordinate_longitude,lat=coordiante_latitude))
x,y,b=3,4,8 #unpacking 序列解包。尝试，x,y,*z=0,1,2,3,4,5,6; x,y,*z=0,1; (x,y),(a,b)=(0,1),(2,3)
func_2=3*x+2*y+b
print("func_2={}".format(x,y,b,func_2))
list_n=list(range(9,18,7)) #建立列表。range(start,stop,[,step])建立区间。
print(list)
print("The list length={}".format(len(list_n)))
print("Maximum value={}".format(max(list_n)))
print("Minimum value={}".format(min(list_n)))
list_s=list(map(chr,range(88,99)))
print(list_s)
print("."*30)
print("[3:6]->{}".format(list_s[3:6]))
print("[-3:-1]->{}".format(list_s[-3:-1]))
print("[-3:]->{}".format(list_s[-3:]))
print("[:3]->{}".format(list_s[:3]))
print("[:]->{}".format(list_s[:]))
help(func) #用help()方法查看说明
print(list_s)
print(","*48)
print("[0:10:2]->{}".format(list_s[0:10:2]))
print("[::3]->{}".format(list_s[::3]))
print("[9:3:-2]->{}".format(list_s[9:3:-2]))
print("[20:3:-2]->{}".format(list_s[20:3:-2]))
print("[7::-2]->{}".format(list_s[7::-2]))
print("[:3:-2]->{}".format(list_s[:3:-2]))
print(list_s)
print("_"*50)
list_s[5]=66 #元素赋值
print("list_s[5]=99->{}".format(list_s))
list_none=list_s+[None]*6
print("list_s+[None]*6->{}".format(list_none))
list_none[13]=2018
print("list_none[13]=2015->{}".format(list_none))
list_none[-6:-3]=list(range(100,104,2)) #分片赋值
print("list_none[-6:-3]=list(range(100,104,2))->{}".format(list_none))
list_none[1:1]=[0,0,0,14]
print("list_none[1:1]=[0,0,0,12]->{}".format(list_none))
del list_none[-2:] #删除元素
print("del list_none[-2:]->{}".format(list_none))
list_s_2=list(map(chr,range(100,105)))
print(list_s_2)
print("_"*50)
list_s_2.append(99)
print("list_s_2.append(99)->{}".format(list_s_2))
list_s_2.append(list(range(50,80,5)))
print("list_s_2.append(list(range(50,80,5)))->{}".format(list_s_2))
list_spechars=['*',')','*']
list_s_2.extend(list_spechars)
print("list_s_2.extend(list_spechars)->{}".format(list_s_2))
print("list_s_2.count('*')={}".format(list_s_2.count('*')))
print("list_s_2.index('e')={}".format(list_s_2.index('e')))
list_s_2.insert(2,[1000,1200,1500])
print("list_s_2.insert(2,[1000,1200,1500])->{}".format(list_s_2))
print("list_s_2.pop(7)_popup->{}".format(list_s_2.pop(7)))
print("list_s_2.pop(7)_retention->{}".format(list_s_2))
list_s_2.remove('*')
print("list_s_2.remove('*')_retention->{}".format(list_s_2))
list_n_2=[2,42,6,95,4,3]
list_n_2.sort()
print("list_n_2.sort()->{}".format(list_n_2))
tuple_1=4,5,6,
print("tuple_1=2,3,5,->{}".format(tuple_1))
print("2*(25*7,)->{}".format(5*(24*3,)))
print("tuple((5,8,9))->{}".format(tuple((5,8,9)))) #用()
print("tuple([5,8,9])->{}".format(tuple([5,8,9]))) #用[]
import random
items=[(0,[i for i in range(5)]),(1,[random.sample(list(range(85,250,2)),3)]),(2,'python')] #[i for i in range(5)] 为列表推导式 list comprehension/derivation
print("items->{}".format(items))
dic=dict(items)
print("dic=dict(items)->{}".format(dic))
print("dic[1]->{}".format(dic[1]))
print("len(dic)->{}".format(len(dic)))
dic[3]=(random.random(),random.uniform(200,300))
print("dic[3]=(random.random(),random.uniform(200,300))->{}".format(dic))
del dic[1]
print("del dic[1]->{}".format(dic))
print("4 in dic->{}".format(4 in dic))
print("6 in dic->{}".format(6 in dic))
print("dic.keys()->{}".format(dic.keys())) #应该放在字典的方法一节里
print("dic.values()->{}".format(dic.values()))
print("dic.items()->{}".format(dic.items()))
print(";"*50)
print("list(dic.keys())->{}".format(list(dic.keys())))
for l,m in enumerate(dic.items()): #for循环在后文
    print(l,m)
lst_A=list(range(5,18,4))
lst_B=list(range(100,150,15))
print("lst_A={},lst_B={}".format(lst_A,lst_B))
dic_2={0:lst_A,1:lst_B}
print("dic_2={}".format(dic_2))
print(";"*50)
dic_assignment=dic_2
print("dic_assignment={}".format(dic_assignment))
dic_2.clear()
print("dic_2.clear()->{}".format(dic_2))
print("dic_assignment={}".format(dic_assignment))
dic_2[5]=list(range(1,9,2))
print("dic_2[5]=list(range(1,9,2))->{}".format(dic_2))
dic_copy=dic_2.copy()
print("dic_copy=dic_2.copy()->{}".format(dic_copy))
dic_2[8]=[5,7]
print("dic_2[8]=[5,7]->{}".format(dic_2))
print("dic_copy={}".format(dic_copy))
dic_copy[5].remove(5)
print("dic_copy[5].remove(5)->{}".format(dic_copy))
dic_copy.setdefault(6,[77,99]) #返回指定键的值，如果不存在该键，则字典增加新的键/值对
print("dic_copy.setdefault(6,[77,99])->{}".format(dic_copy))
dic_2.pop(5) #移除指定键/值，并返回该值
print("dic_2.pop(5)->{}".format(dic_2))
dic_update={8:[5,7,6,3,2],9:[3,2,33,55,66]}
print("dic_update={}".format(dic_update))
dic_2.update(dic_update) #更新字典
print("dic_2.update(dic_update->{}".format(dic_2))
print("dic_2.get(9)->{}".format(dic_2.get(9)))
dic_2.popitem() #随即弹出一对键/值，并在该字典中移除
print("dic_2.popitem()->{}".format(dic_2))

dic_3={}.fromkeys([0,1,2,3,4,'A']) #给定键，建立值为空的字典
print("dic_3={}"+".fromkeys([0,1,2,3,4,'A'])->{}".format(dic_3)) #找下escape characters 脱字符
list_s_3=list("Hello Python!")
print("list_s_3=list(\"Hello Python!\")->{}".format(list_s_3)) #"\" escape character
print("\"Hellow\"+\" Python!\"->{}".format("Hellow"+" Python!"))
print("\"+\".join(str(123456))->{}".format("+".join(str(123456))))
print("len(\"Hellow Python!\")->{}".format(len("Hellow Python!")))
coordinates="120.132007,30.300508,9.7"
print("coordinates.split(\",\")->{}".format(coordinates.split(",")))
print("eval(coordinates)->{}".format(eval(coordinates))) #通常用eval()方法将字符串，转换为对应数值形式；
print("\"Hello Python!\".lower()->{}".format("Hello Python!".lower()))
print("\"Hello Python!\".upper()->{}".format("Hello Python!".upper()))
print("\"Hello Python!\"[6:]->{}".format("Hello Python!"[6:]))
print("\"    Hello Python!    \".strip()->{}".format("    Hello Python!    ".strip()))
print("\"Hello Python!\".replace(\"Python\",\"Grasshopper\")->{}".format("Hello Python!".replace("Python","Grasshopper")))
hello_list=list("Hello Python!")
hello_list.sort()
print("Hello Python!sort()>{}".format("Hello Python!".upper()))
print("\"Hello Python!\".find(\"Py\")->{}".format("Hello Python!".find("Py")))
format_str="Hello,%s and %s!"
values=("Python","Grasshopper")
new_str=format_str % values
print("new_str=format_str % values->{}".format(new_str))

format_str_2="Pi with three decimals:%.3f,and enter a value with percent sign:%.2f %%" #如果字符串里包含实际的%，则通过%%即两个百分号进行转义

from math import pi
new_str_2=format_str_2 % (pi,7.685)
print("new_str_2=format_str_2 % (pi,7.685)->{}".format(new_str_2))
format_str_3="%10f,%10.2f,%.2f,%.5s,%.*s,%d,%x,%f"
new_str_3=format_str_3%(pi,pi,pi,"Hello Python!",5,"Hello Python!",48,48,pi)
print("{}".format(new_str_3))
from string import Template
s_template_1=Template("$x,glorious,$x!")
s_1=s_template_1.substitute(x="Python")
print("s_1=s_template_1.substitute(x=\"Python\")->{}".format(s_1))
s_template_2=Template("${x}thon is complicate!")
s_2=s_template_2.substitute(x="py")
print("s_2=s_template_2.substitute(x=\"py\")->{}".format(s_2))
s_template_3=Template("$x and $y are both complicate!")
substitute_dict=dict([('x','Python'),('y','Grasshopper')])
print("substitute_dict={}".format(substitute_dict))
s_3=s_template_3.substitute(substitute_dict)
print("s_3=s_template_3.substitute(substitute_dict)->{}".format(s_3))
import re
pattern_1='world'
text="Hello world!"
print("re.findall(pattern_1,text)->{}".format(re.findall(pattern_1,text)))
pattern_2='world'
print("re.findall(pattern_2,text)->{}".format(re.findall(pattern_2,text)))
print("re.findall('.ython','Hello world!')->{}".format(re.findall('.ython','Hello world!')))
print("re.findall('.ython','Hello school!')->{}".format(re.findall('.ython','Hello school!')))
print("re.findall('.ython','Hello boy!')->{}".format(re.findall('.ython','Hello boy!')))
print("re.findall('.ython','Hello girl!')->{}".format(re.findall('.ython','Hello girl!')))
print("re.findall(r'w?cadesign\.cn,w+\.cadesign\.cn','cadesign.cn,www.cadesign.cn')->{}".format(re.findall(r'w?cadesign\.cn,w+\.cadesign\.cn','cadesign.cn,www.cadesign.cn')))
print("re.findall(r'w{4}"+"\.cadesign\.cn','www.cadesign.cn')->{}".format(re.findall(r'w{4}\.cadesign\.cn','www.cadesign.cn')))
print("re.findall(r'w{2,5}"+"\.cadesign\.cn','www.cadesign.cn')->{}".format(re.findall(r'w{2,5}\.cadesign\.cn','www.cadesign.cn')))
print("re.findall('[b]*oy!','Hello boy!')->{}".format(re.findall('[b]*oy!','Hello boy!')))
print("re.findall('[b]*oy!','Hello boy!')->{}".format(re.findall('[b]*oy!','Hello boy!')))
print("re.findall('[b]*oy!','Hello boy!')->{}".format(re.findall('[b]*oy!','Hello boy!')))
print("re.findall('[b]*oy!','Hello boy!')->{}".format(re.findall('[b]*oy!','Hello boy!')))
print("re.findall('bird|grasshopper','bird')->{}".format(re.findall('bird|grasshopper','bird')))
print("re.findall('bird|grasshopper','grasshopper')->{}".format(re.findall('bird|grasshopper','grasshopper')))
print("re.findall('bird|grasshopper','grasshopper and bird')->{}".format(re.findall('bird|grasshopper','grasshopper and bird')))
print("re.findall('\d','number=8')->{}".format(re.findall('\d','number=8')))
print("re.findall('\D','number=8')->{}".format(re.findall('\D','number=8')))
print("re.findall('[^0-9]','number=8')->{}".format(re.findall('[^0-9]','number=8')))
print("re.findall('[a-z]','python')->{}".format(re.findall('[a-z]','python-3.0')))
print("re.search('[a-z]+','python')->{}".format(re.search('[a-z]+','python')))
if re.search('[a-z]+','python'):
    print("re.search('[a-z]+','python')->found it!")
print("re.split(',','Hello,,,,,,world!')->{}".format(re.split(',','Hello,,,,,,world!')))
print("re.sub('Python','Grasshopper','Hello Python!')->{}".format(re.sub('Python','Grasshopper','Hello Python!')))

pattern_compile=re.compile('Python')
print("pattern_compile.findall('Hello,,,,,,world!')->{}".format(pattern_compile.findall('Hello,,,,,,world!')))

if re.match('p','python'):
    print("re.match('p','python')->found it!")
print("\'python\'.find(\'py\')->{}".format('python'.find('py')))
print("\'python\'.find(\'on\')->{}".format('python'.find('on')))
print("\'python\'.find(\'n\')->{}".format('python'.find('n')))
print("\'p\' in \'python\'->{}".format('p' in 'python'))
print("\'Hello,,,,,,world!\'.split(',')->{}".format( 'Hello,,,,,,world!'.split(',')))
print("\'Hello world!\'.replace(\'world\',\'Grasshopper\')->{}".format( 'Hello world!'.replace('world','Grasshopper')))
match_1=re.match(r'www\.(.*)\..{3}','www.python.org')
print("match_1.gourp(1)->{}".format(match_1.group(1)))
print("match_1.start(1)->{}".format(match_1.start(1)))
print("match_1.end(1)->{}".format(match_1.end(1)))
print("match_1.span(1)->{}".format(match_1.span(1)))
match_2=re.match(r'www\.(.*)\.(.{3})','www.python.org')
print("match_2.group(1)->{}".format(match_2.group(1)))
print("match_2.group(2)->{}".format(match_2.group(2)))
lst_1=list(range(21,15,6))
print("lst_1={}".format(lst_1))
print("_"*50)
print("for i in lst_1:")
for i in lst_1:
    print(i)
print("for i in range(len(lst_1)):")
for i in range(len(lst_1)):
    print("idx={},val={}".format(i,lst_1[i]))
print("+"*50)   
dic_4=dict(a=2,b=3,c=6,d=0)
print("dic_4={}".format(dic_4))
print("_"*50)
print("for k in dic_4:")
for k in dic_4:
    print(k)
print("for k,v in dic_4.items():")
for k,v in dic_4.items():
    print("key={},val={}".format(k,v))
x=1
while x<=80:
    print("x={}".format(x))
    x+=10 #增量赋值; x*=3     
x=1
while x<=99:
    print("x={}".format(x))
    x+=10 
    if x>=40:break    
    
import sys
print("sys.maxsize={}".format(sys.maxsize))
for i in range(sys.maxsize):
    print("i={}".format(i))  #?
    i+=10
    if i>=100:break
list_a=[0,1,2,3]
list_b=['point_a','point_b','point_c','point_d']
zip_list=zip(list_a,list_b) #The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
print("zip_list=zip(list_a,list_b)->{}".format(zip_list))
print("dict(zip_list)->{}".format(dict(zip_list)))

zip_list=zip(list_a,list_b) #迭代对象临时存储，读取完后为空
for a,b in zip_list:
    print(a,b)
    
zip_list=zip(list_a,list_b)
a,b=zip(*zip_list)
print("a={},b={}".format(a,b))
list_c=['point_a','point_b','point_c','point_d']
dic_4={}
for idx,value in enumerate(list_c):
    dic_4[idx]=value
print("dic_4={}".format(dic_4))
print("dict((i,v) for i,v in enumerate(lst_c))->{}".format(dict((i,v) for i,v in enumerate(list_c)))) #list comprehension
print("_"*50)
for i,(a,b) in enumerate(zip(list_a,list_b)):
    print('%d:%s,%s'%(i,a,b))
print("[x*x for x in range(4,40,6) if x%2==0]->{}".format([x*x for x in range(4,40,6) if x%2==0]))
print("[(x,y) for x in range(4)for y in range(2)]->{}".format([(x,y) for x in range(4)for y in range(2)]))
print("[(x,y) for x,y in zip(range(4),range(2))]->{}".format([(x,y) for x,y in zip(range(4),range(2))]))
nested_list=[[a for a in range(1,10,3)],2,3,[b for b in range(60,100,7)],[[c for c in range(1000,2000,120)],3,9]]
print("[[a for a in range(1,10,3)],2,3,[b for b in range(60,100,7)],[[c for c in range(1000,2000,120)],3,9]]->{}".format(nested_list)) #嵌套列表推导式

flatten_lst=lambda lst: [m for n_lst in lst for m in flatten_lst(n_lst)] if type(lst) is list else [lst] #展平列表常用，可以放置到单独的.py文件中调用。lambda函数后文阐述
print("flatten_lst(nested_list)->{}".format(flatten_lst(nested_list)))
x=y=[4,5,7]
z=[4,5,7]
print("x==y->{}".format(x==y))
print("x is y->{}".format(x is y))
print("x==z->{}".format(x==z))
print("x is z->{}".format(x is z))
print("x is not y->{}".format(x is not y))
print("x is not z->{}".format(x is not z))
print("id_x:{};id_y:{};id_z:{}".format(id(x),id(y),id(z))) #Memory Location

del x[2]
print("x={},y={},z={} after del x[2]".format(x,y,z))
x=[4,5,7]
print("3 in x->{}".format(3 in x))
print("0 in x->{}".format(0 in x))
print("3 not in x->{}".format(3 not in x))
print("0 not in x->{}".format(0 not in x))
a,b,c=2,5,9
if c>a and c<b:
    print('a<c<b')
else: print('a<c<b kidding!!!')
def function(arguments):
    statement
    ...
    return values 
def simple_func(x,y):
    z=pow(x,2)+y
    return z
   
print("simple_func(3,7)->{}".format(simple_func(3,7)))
print("simple_func(7,3)->{}".format(simple_func(7,3)))
print("simple_func(y=7,x=3)->{}".format(simple_func(y=7,x=3)))
def fibonacci(s,count): #定义fib函数的方法较笨
    fib_list=[0,1]
    fib_part=[]
    if s==0 or s==1:
        fib_part[:]=fib_list
        for i in range(count-2):
            fib_part.append(fib_part[-1]+fib_part[-2])
    else:
        while True:
            fib_list[:]=[fib_list[1],fib_list[0]+fib_list[1]]
            #print(fib_lst)
            if fib_list[1]-s>=0:break
        fib_part[:]=fib_list
        if abs(fib_list[0]-s)>=abs(fib_list[1]-s):
            for i in range(count-1):
                fib_part.append(fib_part[-1]+fib_part[-2])
            fib_part.pop(0)
        else:
            for i in range(count-2):
                fib_part.append(fib_part[-1]+fib_part[-2])
    return fib_part

print("fibonacci(6,9)->{}".format(fibonacci(6,9)))
print("fibonacci(7,9)->{}".format(fibonacci(7,9)))
def factorial(n):
    if n==2:
        return 2
    else:
        return n*factorial(n-1)
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(7))
class Bird:
    fly='Whirring' #美 /wɜːr/ 
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry=False
        else:
            print('No.Thanks!')

class Apodidae(Bird):  #/'æpədədi:/
    def __init__(self):
        super(Apodidae,self).__init__()
        self.sound='Squawk!' #美 /skwɔːk/ 
    def sing(self):
        print(self.sound)
swift=Apodidae()
print("swift.fly->{}".format(swift.fly))
print("swift.eat()->")
swift.eat()
print("swift.eat()->")
swift.eat()
print("swift.sing()->")
swift.sing()
blackswift=Apodidae()
scarceswift=Apodidae()
print("blackswift.sing()->")
blackswift.sing()
print("scarceswift.sing()->")
scarceswift.sing()
print("blackswift.fly->{}".format(blackswift.fly))
blackswift.fly='humming' #重新赋予实例的属性
print("blackswift.fly after redefining the blackswif's attribute->{}".format(blackswift.fly))
print("scarceswift.fly->{}".format(scarceswift.fly))
blackswift.sing()
help(Bird)
help(Apodidae)
class Fibs():
    def __init__(self):
        self.a=0
        self.b=1
    def next(self):  #实现迭代器的next方法
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self): #实现迭代方法
        return self
f=Fibs()
fa=[]
fb=[]
for i in range(9):
    fa.append(f.next())
print("fa={}".format(fa))
for i in range(5):
    fb.append(f.next())
print("fb={}".format(fb))
lst_e=[list(range(3,20,3)),[3,7,67,list(range(5)),89]]
print("lst_e={}".format(lst_e))
print(","*50)
flatten_lst=[]
for v_1 in lst_e:
    try:
        for v_2 in v_1:
            try:
                for v_3 in v_2:
                    flatten_lst.append(v_3)
            except TypeError:
                flatten_lst.append(v_2)
    except TypeError:
        flatten_lst.append(v_1)
print("flatten_lst={}".format(flatten_lst))
def flatten(lst): #定义生成器（包含yield语句的函数）
    try: #使用语句try\except捕捉异常        
        for n_lst in lst:  #循环列表            
            for m in flatten(n_lst): #使用递归的方法循环子列表                
                yield m  #使用yield语句，每次产生多个值，当返回一个值时函数就会被冻结，当再次激活时，从停止的那点开始执行
    except TypeError:  #当函数被告知展开一个元素时，引发TypeError异常，生成器返回一个值
        yield lst #生成器返回引发异常的一个值        
print("list(flatten(lst_e))->{}".format(list(flatten(lst_e))))
flatten_lst=lambda lst:[m for n_lst in lst for m in flatten_lst(n_lst)] if type(lst) is list else [lst] #lambda 生成器方法
def infinite():
    n=0
    while True:
        yield 'num#'+str(n)
        n+=2
n=infinite()
print("next(n)->{}".format(next(n)))
print("next(n)->{}".format(next(n)))
print("next(n)->{}".format(next(n)))
print("[next(n) for i in range(5)]->{}".format([next(n) for i in range(5)]))
n=3
print("[[(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n)]->{}".format([[(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n)]))
print(";"*50)
print("([(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n))->{}".format(([(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n))))
gen=([(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n))
print("next(gen)->{}".format(next(gen)))
print("next(gen)->{}".format(next(gen)))
def f_convert_a(x):
    try:
        return float(x)
    except:
        return x
print("f_convert_a('3.1415')->{}".format(f_convert_a('3.1415')))    
print("f_convert_a('string')->{}".format(f_convert_a('string')))  
print("f_convert_a(3,6,7)->{}".format(f_convert_a((3,6,7))))  
def f_convert_b(x):
    try:
        return float(x)
    except:
        return x
print("f_convert_b('3.1415')->{}".format(f_convert_b('3.1415')))    
print("f_convert_b('string')->{}".format(f_convert_b('string')))  
print("f_convert_b(3,6,7)->{}".format(f_convert_b((3,6,7))))  
def f_convert_c(x):
    try:
        return float(x)
    except ValueError:
        return x
    except TypeError:
        print(x,'TypeError')
print("f_convert_c('3.1415')->{}".format(f_convert_c('3.1415')))    
print("f_convert_c('string')->{}".format(f_convert_c('string')))  
print("f_convert_c(3,6,7)->{}".format(f_convert_c((3,6,7))))         
def f_convert_d(x):
    try:
        return float(x)
    except (ValueError,TypeError):
        print(x,'ValueError or TypeError')
print("f_convert_d('3.1415')->{}".format(f_convert_d('3.1415')))    
print("f_convert_d('string')->{}".format(f_convert_d('string')))  
print("f_convert_d(3,6,7)->{}".format(f_convert_d((3,6,7)))) 
def f_convert_e(x):
    try:
        return float(x)
    except (ValueError,TypeError) as e:
        return print(x,e)
print("f_convert_e('3.1415')->{}".format(f_convert_e('3.1415')))    
print("f_convert_e('string')->{}".format(f_convert_e('string')))  
print("f_convert_e(3,6,7)->{}".format(f_convert_e((3,6,7))))    
def f_convert_f(x):
    try:
        return float(x)
    except (ValueError,TypeError) as e:
        pass
print("f_convert_f('3.1415')->{}".format(f_convert_f('3.1415')))    
print("f_convert_f('string')->{}".format(f_convert_f('string')))  
print("f_convert_f(3,6,7)->{}".format(f_convert_f((3,6,7))))     
def f_open_a(fp):
    try:
        f=open(fp,'r')
    except IOError as e:
        print('Unable to open',fp,':%s\n' %e)
    else:
        data=f.read()
        f.close
        return data
tryException_content=f_open_a("./data/tryException.txt")   
print("tryException_content->{}".format(tryException_content))
f_open_a("./data/tryException_.txt")
def f_open_b(fp):
    try:
        f=open(fp,'r')
    except IOError as e:
        print('Unable to open',fp,':%s\n' %e)
    else:
        data=f.read()
        f.close()
        return data
    finally:
        print('done!')
f_open_b("./data/tryException.txt")        
raise Exception #没有任何有关错误信息的普通异常
class some_custom_exception(Exception):pass #
raise some_custom_exception
x=20
assert x>0 #为真则不做任何事情
assert x<0 #为假则引发AssertionError异常




