'''
sum = 0
count = 0
while True:
    a = input()
    if a == 'stop':
        break;
    else:
        b = float(a)
        count += 1
        sum += b
'''
'''
g=input('введи свое имя')
print('привет,',g)
'''
'''
d=int(input())
if d>=18:
    print('вы можете голосовать')
else:
    print('вы не можете голосовать')
'''
'''
for i in range(0,11,1):
    print(i)
'''
'''
g=int(input())
g*=5
print(g)
'''
'''
def print_name_message(g):
    print('привет,',g)

print_name_message("hi")
'''
'''
f=int(input())
for i in range(0,f,2):
    print(i)
'''
'''
x=-1
f=['apple','potato','bath']
for i in range(0,len(f),1):
    print(f[x])
    x-=1
'''
'''
check=0
def check_number(num):
    if num<=2:
        return False
    for i in range(num-1,2,-1):
        print(i)
        if num%i==0:
            return False
    return True
            
num=int(input())
print(check_number(num))
'''
'''
fruits=['apple','grape','kiwi']
fruits_1=input('введите фрукт')
fruits.insert(0,fruits_1)
print(fruits)        
'''
'''
d=input()
print(d.upper())
'''
'''
d=int(input())
d*=d
print(d)
'''
'''
c=int(input())
c=(c*9//5)+32
print(c)
'''
'''
c=int(input())
if c<=2:
    print('не сдал')
else:
    print('сдал')
'''
'''
def sum_two_nums(x,y):
    x+=y
    print(x)
x=int(input())
y=int(input())
sum_two_nums(x,y)
'''

g=-1
d=int(input())
x=int(input())
b=int(input())
list=(d,x,b)
for i in range(-1,len(list),-1):
    print(list[i])
    g-=1












































