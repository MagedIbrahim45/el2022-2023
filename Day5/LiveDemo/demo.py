from mymath import sum
sum(1,2)
'''
import mymath
num1=float(input('enter num1'))
num2=float(input('enter num2'))
operation=(input('enter operation + * -'))
if(operation=='+'):
    res=mymath.sum(num2,num1)
    print(mymath.sum(num2,num1))
print(mymath.pi)





num1=input('enter num1')
try:
    float(num1)
    print(1/0)
except ValueError:
    print('error')
except ZeroDivisionError:
    print('cannt divid by zero0')
except :
    print('call sys admin')
#print 'jjllj'
num2=input('enter nuandm2')
def dosum(n1,n2):
    if(n1.isdigit() and n2.isdigit() ):
        print(float(n1)+float(n2))
    else:
        print('n1,n2 must be digit')
dosum(num2,num1)

name='global'#'inner'
def final():
    #name='final'
    def outer():
       # name='outer'
        def innner():
           # nonlocal name
            #name = 'inner'
            print(name)
        innner()
        print(name)
    outer()
final()
print(name)

def dosum(n1,n2):
    nonlocal num2
    num2+=2
    return num1+num2
num1=float(input('enter num1'))
num2=float(input('enter num2'))
print(dosum(num1,num2))


vstr='aioeu'
if('a' in vstr):
    print('found')

vl=['a','i','e']
if('a' in vl):
    print('found')

d={'id':1,
   'name':'ali'}
if('id' in d):
    print('founded')
'''