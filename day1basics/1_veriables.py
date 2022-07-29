import day1basics
import keyword
print(keyword.kwlist)
a="10"
b="20"
print(f"sum of {a}  and {b} is " + str(int(a)+int(b)))
a= "Nilesh"
a=6.6
print(a)
print(type(a))

"""
this we can use for details about your test
"""
a=b=c=8
a,b,c=6,7,8.56
print(c)
print(b+c)
expo=2**5
print(expo)
print(100%3)
print(100//3)
c+=2
c-=2
c*=2
c/=2
print(c)
print('hello \ni am "nilesh"')
print("hello \"ggg\"")
"""
len())
uppper
lower
replace

"""

a = "nilesh Rathre"
print(a[1:7])
print(a[1:])
print(a[1:7:2])
print(a[::2])
print(a[::-1])#reverce string
print(a[-3])
print(a[1:-2])
b=a[0:6]
print(b[::-1])
x=9
z = 8
if x == 5:
    print("im in if block")
    if z == 7:
        print("we are inZ")

elif x == 7:
    print("i m in else")
else:
    print("full else")

while z<16:
    print(z)
    z += 1

for i in range(6):
    print(i)
z="nilesh"
for i in z:
    print(i)

car=["baleno", "bmw", "farari"]
for i in car:
    print(i, end=" ")
text={"mode":"Balemo","brand":"sizuki"}
print(text["mode"])
print(text["brand"])
d={}
d['one'] = 1
d['two'] = 2




print(d)

car = {'make': 'bmw', 'model': '550i', 'year': 2016}
print(car)
print(car.keys())
print(car.values())
print(car.items())
print(car.pop("make"))
print(car)
