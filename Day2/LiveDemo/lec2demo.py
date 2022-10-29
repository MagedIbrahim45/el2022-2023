#prop & methods
name="fci information information"
print(name.replace('f','F'))
print(name.replace('f','F',1))
print(name.split(' ')[2].replace('f','F'))
print(name.split(' ')[0]+' '+name.split(' ')[1]+' '+name.split(' ')[2].replace('f','F'))

'''
myerror= """
high level error
number {number}  message {msg}
{msg}
"""
print(myerror)
print(myerror.format( msg='msg1',number='test1'))

name=input('enter name ')
names=name.split(' ')
print(name,names)

num=input('enter numbrer')
num.isdigit()# return true or false

num=float(num)

name="fci information information"
name=name.replace('f','F')
print(name.replace('f','F'))
print(name)
print('asd'*4)
print(type('asdf'))
#mult values seperated with , sep=' ' ,end=\n
print('asd',1,1.1,False,(),sep='&',end=' ')
print('test')
n1=float(input('enter num1'))
n2=float(input('enter num2'))
print('sum =',n1+n2)
print('sum=',end= ' ')
print(n1+n2)
print('sum=')

print('sum='+str(n1+n2))# str+str
name='ali ahmed'
#slice
print(type(name))
print(name[5])
print(name[1:6]) # end-1  start:end
print(name[1:])
print(name[1:-1])
print(name[:5])
#demha ila



#unpacking
n1,n2,n3=1,2.0,'one'
min(1,2,3,4,5,7)
min(4,5,7)
min(4,5,7,3,3,5,78,3,6,2,8,1.1)


number=1
print(type(int))
number=2.3
print(type(number))
#1+1j--->c++ + - *
number=1+2j
number2=2+3j
print(number2+number)
print(type(number))



print({}==True)

num1=10
num2=20
print(num1==num2)
print(num1!=num2)
print(num1>=num2)

print(16/5)
print(16//5)
print(2**3)

num=input('enter number') # return as string
num=int(num)
print(type(num))
'''


"""
num1=1
num1=2.2
num1='one'

str1="sdsd" #single line string
#multi line string ''' ''' or  """ """
bio='''my name is ali 
my age =19'''
print(bio)
"""

'''
number=1
Number=1.1
if True:
    print('skdkjsadl')
    print('sdjslkd')
else:
    print('jsdkjsdl')

number=1 #object class int
print(type(number))
number=1.1 #object class float
print(type(number))
'''