"""
This is our first program
Developer : Nilesh Rathore
Purpose : This is to write Basic ppython
Param :
Var1 :
var2 :
"""
import time

"""

"""
# import math
from Demo1.funDemo import carss
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome()
# driver=webdriver.Chrome(service=Service("C:\\Users\\USER\\Desktop\\Day2\\chromedriver.exe"))
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")

actions = ActionChains(driver)

print(driver.title)

driver.implicitly_wait(10)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
elementListByTagName = driver.find_elements(By.TAG_NAME, "td")
length2 = len(elementListByTagName)
driver.find_element(By.XPATH, carss.ob["fname"]).send_keys("hello")
x= driver.find_element(By.XPATH, carss.ob["select"])
actions.move_to_element(x)
time.sleep(5)
driver.find_element(By.XPATH, carss.ob["select"]).click()
print(driver.find_element(By.XPATH, carss.ob["select"]).is_selected())
driver.find_element(By.XPATH, carss.ob["fname"]).clear()
# print(carss.a)
# carss.sumNum(2,5)
# print(math.sqrt(100))

# print("Hello world!!")
# print(1234)
#
# a=10
# b=20
# print(a+b)
#
# a = "Vaibhavi"
# b = 40.6
# print(type(b))
# print(a + "  " + str(b))

# A= "10"
# B= "15"
# # print("addition of " + str(A) + " & " + str(B) + " is " + str(A+B))
# print(f'addition of {A} and {B} is ' + str(int(A)+int(B)))
#
# a,b,c,d=1,2,3,4
#
# a=b=c=10
# print(b)
#
# print(d)

# a = int(input("Enter number 1 "))
#
# b = int(input("enter number 2"))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
#
# print(100//3)
# print(100 % 3)
# print(2**5)
#

# a = "I am Nilesh"
# b = "I am Nilesh"
#
#
# print(a.upper())
# a = input("enter your loging ID")
# print(len(a))
# z = b.replace("Nilesh", "xyz")
# print(z)

"""
==
<=
>=
<
>
!=
"""

# print((2+4)*4/2)

# print(5!=6)
# print (5==10 or 5==5)
"""
True or true > true
True or false > true
false or fALSE > false

true and true  >> true
true and false >> false 
false and false >> false

true not true >>false




"""

# a = [1,2,3,4]
# print(a[0])
#
# a.append(6)
# print(a)
#
# print(a[1])
#
# a  = {"Login_ID": "xpath", "login_PWD":"*****", "login_butto":"xpath"}
# print(a["Login_ID"])
# print(a.values())
# print((a.keys()))
# print(a)
# print("*"*20)
# print(a.items())
# a.pop()
# print(a.pop("login_butto"))
# print(a)
# print(a.items())
#
# if 100 ==10:
#     print("This if got selected")
# elif(100!=10):
#     print("else if")
# else:
#     print("else")
#

# a = int(input(("enter Variable 1 ")))
# b = int(input(("Enter Variable 2 ")))
# UserOp=input(("Enter user operation"))
#
# if UserOp =="+":
#     print("Addition is : " + str(a+b))
# elif UserOp =="-":
#     print(a-b)
# elif UserOp =="*":
#     print(a*b)
# elif UserOp =="/":
#     print(a/b)
# else:
#     print("user input is invalid")
#

# a = "10"* "10"
# print(str(a))
#
# x = 0
# temp=0
# while x<10:
#     x+=1
#     temp=temp+x
#     print(temp)
#     while temp <22
#
#
# # 1,3,6,10,15,21
# i = 1
# j =2
# while col < 6:
#     col += 1
#     while roww< 6:
#         print(str(col) + " " + str(roww))
#         roww+=1


# for i in range(1,5):
#     for j in range(2,5):
#         if i =3:
#             sheet1.cells(i,j)=="6"
#
#         print(str(i) + " " + str(j))
#

# a= [1,2,3,5]
#
# for i in range(5,10,2):
#     print(i,end=" ")
#
# a=10
#
# def sum_num():
#     global a
#     print(a)
#     a=5
#     print(a)
#
#
#
#
# sum_num()
# print(a)


# a = 10
#
# def test_method():
#     global a
#     print("Value of 'a' inside the method is: " + str(a))
#     a = 2
#     print("New value of 'a' inside the method is changed to: " + str(a))
#
# print("Value of global a is: " + str(a))
# test_method()
# print("Did the value of global 'a' change? " + str(a))
#
#
#
# def Maax_Num(*a):
#     print(max(a))
# Maax_Num(3,8,9,66)
#
#
# class Cars():
#     def __init__(self):
#         print("called")
#
#     def sum_num(self, abc, b):
#         return (abc + b)
#
#
# c1 = Cars()
#
# class Car(Cars):
#
#     def __init__(self):
#         Cars.__init__(self)
#         print("You just created the car instance")
#
#     def drive(self):
#         print("Car started...")
#
#     def stop(self):
#         print("Car stopped")
#
# c = Car()
# c.sum_num(3,5)
# a.remove(3)
# # a.pop(4)
# print(a)
# a.pop()
# print(a)
#
#

# a = "happy"
# print(a[0])
#
# for i in a:
#     print(i)

# try:
#     c = 10 + 7 / 10
#     print(c)
# except:
#     print("we are in except block")
# else:
#     print("Wr are good to go we are Pass")
# finally:
#     print("always get executed")

# demo = open("nilesh.txt","w")
# demo.write("I am nilesh" + "\n")
# demo.write("I like to type")
# demo.close()
#
# demo=open("nilesh.txt","r")
# rl =demo.readlines()
# for i in rl:
#     print(i)

# for i in range(1,6):
#
#     for k in range(1,i):
#         print(" ",end=" ")
#     for j in range(i,6):
#         print("*",end=" ")
#     print("")