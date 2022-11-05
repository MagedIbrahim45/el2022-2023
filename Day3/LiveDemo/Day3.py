#int float string bool complex
#list tuple dictionary
#collection of values differernt type accessed by key
d={'id':1,'name':'ahmed','level':3,'GPA':3.9,
   'courses':['python','db fundamentals']
   ,'grades':(88,100)}
for key,value in d.items():
    print(key,value)
'''
for x in d:
    print(x,'====>',d[x])
d1={'id':100,'location':'assuit'}
d1.update(d)
print(d)
print(d1)
print(d+d1)#error
print(d1*2)#error{'id':1}
d['id']=100#update
d['plpla']='plpa'#insert
print(type(d),d)
x,y=(1,2)
l=[1,1.1,'one']
for index,value in enumerate(l):#[(),()]
    #print('index',iteam[0],'value=',iteam[1],type(iteam))
    print('index',index,'value=',value)

#tuple colllection of values different data type
t=1.1,
print(type(t))
x,y=1,'one'
print(x)
print(y)
t=1,1.1
print(type(t))
t=(1,1.1,'onr',True,[3,4],(1,3))

for x in enumerate(t):
    print(x)
t2=('username','password')

print(t+t2)
print(t*2)
print(t,t2)
print(t[0:3])
print(type(t),t)
#list collection of values different datatype
lang=[2,'c#','c++','C','C',True]
opensource=['python','java']
lang.extend(opensource)
print(lang)
print(opensource)
print(lang.index('C'))
print(len(lang))
print(lang.count('C'))


lang.remove(True)
print(lang)
print(lang.remove('c#'))
print(lang.pop(0))
lang.insert(0,'C')
lang.append('C')
lang.append(1)
print(lang+opensource)
print(lang*2)
print(lang)
print(opensource)

l=[1,1.1,'one',True,1+1j,[3,4]]
for item in enumerate(l):
    print(item,type(item))
l[0]=1000
print(l)
print(l[1:3])
print(type(l[5]))
print(l,type(l))
#controls   if for while

#while
flag=1
while(flag!='e'):
    print('hello fci')
    flag=input('enter e to exit else press anykey')

flag=input('enter n for new operarion else o')
while(flag!='o'):
    x=input('enter number')
    print(x)
    flag = input('enter n for new operarion else o')

#for
for x in range(5):
    if(x==2):
        continue
    print(x) #0,1,2,3,4

#range([start=0],end,[setp=1])
print(range(1,13,1))
for days in range(13):
    print(days)
range(1,13,1)
range(1,13)
range(13)

name='ahmed ali'
print(type(enumerate(name)))#[(0,a),(8,i)]
print(enumerate(name))
for char in enumerate(name):
    print(char[0],char[1])


num1=float(input('enter number1'))
num2=float(input('enter number2'))

if(num2!=0 and num2>0):
    print(num1/num2)
elif(num2!=0 and num2<0):
    print('cant divide by -')
else:
    print('you cant divide by zero')
'''
