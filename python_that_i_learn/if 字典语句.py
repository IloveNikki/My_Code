age=22
if age<4:
    print("Your admission cost 0.")
elif age<18:
    print("Your admission cost 10.")
else:
    print("Your admission cost 20.")


age=22
if age<4:
    price=0
elif age<18:
    price=10
else:
    price=20
print("Your admission cost",price)

age=66
if age<4:
    price=0
elif age<65:
    price=10
else:
    price=5
print("Your admission cost",price)

alien_color='green'
if alien_color=='green':
    print("You gain 5 dots.")
else:
 print("You lose.")

alien_color='red'
if alien_color=='green':
    print("You gain 5 dots.")
elif alien_color=='red':
 print("You lose.")

alien_color='red'
if alien_color=='green':
    print("You gain 5 dots.")
else:
 print("You gain 10 dots.")

 alien_color='green'
 if alien_color=='green':
     print("You gain 5 dots.")
 elif alien_color=='red':
     print("You gain 10 dots.")

alien_color='green'
if alien_color=='green':
    print("You gain 5 dot")
elif alien_color=='yellow':
    print("You gain 10 dots.")
elif alien_color=='red':
    print("You gain 15 dot")

alien_color='red'
number=0
if alien_color=='green':
   number=5
elif alien_color=='yellow':
   number=10
elif alien_color=='red':
  number=15
print("You gain ",number," dots.")

age=17
if age<2:
    print("You are baby.")
elif age<4:
    print("You are learning to walking.")
elif age<13:
    print("You are a child.")
elif age<20:
    print("You are a teenager.")
elif age<65:
    print("You are a adult.")
else:
    print("You are an elder.")

fruits=['apple','banana','orange','strawberry','watermelon']
if 'apple' in fruits:
    print("Your favorite fruit is apple.")
if 'banana' in fruits:
    print("Your favorite fruit is banana.")
if 'orange' in fruits:
    print("Your favorite fruit is orange.")


# 使用多个列表
# 这个是例子
# users=['armin','base','nace','tony','uni']
users=[]
if users==[]:
    print("We need to find some users!")

# for user in users:
#     if user=='armin':
#         print("Hello Armin,would you like to see a status report?")
#     else:
#         print("Hello,"+user.title()+" thank you for logging in again.")
#

current_users=['armin','base','nace','tony','uni']
new_users=['armin','jack','nor']
for new_user in new_users:
    if new_user in current_users:
        print("Please reinput other name.")
    else:
       print("This name is not used.")


numbers=list(range(1,10))
for number in numbers:
    if number==1:
        print("1st")
    elif number==2:
        print("2nd")
    elif number==3:
        print("3rd")
    else:
        print(f"{number}th")



numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# for number in numbers:
#
#
#     if number == '1':
#         print(number + "st")
#     elif number == '2':
#         print(number + "nd")
#     elif number== '3':
#         print(number + "rd")
#     else:


# friend={'frist_name':'shining','last_name':'nikki','city':'shanghai','age':18}
# print(friend['first_name'])
# print(friend['last_name'])
# print(friend['age'])
# print(friend['city'])


# 字典内有列表
nums={'armin':[1,4,3,2,5],
      'base':[3,2,1],
      'nace':[4,7,6]}
# print(nums['armin'],'armin'.title())
for name,num in nums.items():
    print("\n"+name.title()+"'s favorite number is :")
    for num in num:
        print(num)

words={'print':'打印',
       'input':'输入',
       'output':'输出'}

print(words)
words['int']='定义'
print(words)
# print("print :\n",words['print'])
# print("input:\n",words['input'])
for key,value in words.items():
    print("\nKey: "+key)
    print("Value: "+value)

rivers={'huang he':'china','nile':'egypt','changjiang':'china'}
for key,value in rivers.items():
    print("The "+key.title()+" runs through  "+value.title()+".")
    print("\nKey: "+key.title())
    print("Value: "+value.title())

favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
friends=['armin','base','nace','jen']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Thank you!")
    else:
        print(name.title()+"Please get involve in survey.")


people=['armin','base','nace','jen','jack','non']
friend_1={'frist_name':'shining','last_name':'nikki','city':'shanghai','age':18}
friend_2={'frist_name':'infinity','last_name':'nikki','city':'shanghai','age':19}
friend_3={'frist_name':'miracle','last_name':'nikki','city':'shanghai','age':17}
friends=[friend_1,friend_2,friend_3]
for friend in friends:
    print(friend)

dog={'name':'shining','hoster_name':'uni','age':2}
cat={'name':'jack','hoster_name':'nikki','age':3}
rabit={'name':'mike','hoster_name':'anny','age':1}
pets=[dog,cat,rabit]
for pet in pets:
    print(pet)

favorite_places={
    'armin':['beijing','shanghai','ezhou'],
    'base':['guangzhou','shenzhen'],
    'nace':['wuhan','huanggang']
}
print('\tarmin'.title()+"'s favorite places:")

# for armin in favorite_places['armin']:
#     print("\t"+armin.title())
#
# for favorite_place in favorite_places:
#     print("\t"+favorite_place.title())
#

for name,place in favorite_places.items():
    print("\n"+name.title()+"'s favorite places are:")
    for place in place:
        print("\t"+place.title())

# 字典里有字典
cities={'wuhan':{
    'country':'china',
    'population':50000,
    'fact':'changjiang'
            },
    'beijing':{
    'country':'china',
     'population':50000,
        'fact':'tian an door'
    }
}
for city,city_info in cities.items():
    print(city.title()+" :")
    country=city_info['country']
    population=city_info['population']
    fact=city_info['fact']
    print(country.title())
    print(population)
    print(fact.title())


# message=input("Enter the type of car you like:")
# print("Let me see if I can find you a "+message+".")



# 注意要对input前的变量名进行int化
# number="How many people on here to have food?"
# number+="Enter the number of people:"
# messages=input(number)
# messages=int(messages)
# if messages>=8:
#     print("No empty seat to have.")
# else:
#     print("Please have food.")

# 判断是否是10的整数倍。
# number=input("Enter the number:")
# number=int(number)
# if number%10==0:
#     print("True!")
# else:
#     print("False!")

# prompt="\nTell me something ,ang I will repeat it back to you.:"
# prompt+="\nEnter the 'quit' to end the program"
# message=""
# while message!='quit':
#     message=input(prompt)
#
#     if message !='quit':
#         print(message)

# prompt="\nTell me something ,ang I will repeat it back to you.:"
# prompt+="\nEnter the 'quit' to end the program"
# active=True
# while active:
#     message=input(prompt)
#     if message=='quit':
#         active=False
#     else:
#         print(message)


# prompt=input("Please enter the city you want to go:")
# while True:
#
#     if prompt=='quit':
#         break
#     else:
#         print("I want to go to "+prompt.title())
#         break

# break的作用
# prompt="Please enter the city you want to go；"
# while True:
#     city=input(prompt)
#     if city=='quit':
#         break
#     else:
#         print("I want togo to "+city.title()+".")

# continue的作用
# number=0
# while number<10:
#     number+=1
#     if number%2==0:
#         continue
#     else:
#         print(number)



# 这两种方法相同，都是打印数字
# x=1
# while x<=5:
#     print(x)
#     x+=1
#
# for value in range(1,6):
#     print(value)

# 题目
# foods="Enter the food to add in the pizza:"
# while True:
#     food=input(foods)
#     if food=='quit':
#         break
#     else:
#         print("We will add in the pizza.")


# food=input("Enter the food to add in the pizza:")
# while True:
#     if food=='quit':
#         break
#     else:
#         print("We will add in the pizza.")
#         break


# food=input("Enter the food to add in the pizza:")
# active=True
# while active:
#     if food == 'quit':
#         active=False
#         break
#     else:
#         print("We will add in the pizza.")
#         active=False
#         break



# age=input('please enter your age:')
# while True:
#     age=int(age)
#     if age<=3:
#         print("No money to pay!")
#         break
#     elif age <=12:
#         print("Please pay for 10 dollars.")
#         break
#     else:
#         print("Please pay for 15 dollars.")
#         break

# word="Please enter your age:"
# while True :
#     age=input(word)
#     age=int(age)
#     if age<=3:
#         print("No money to pay！")
#
#     elif age<=12:
#         print("Please pay for 10 dollars.")
#
#     else:
#         print("Please pay for 15 dollars.")
# # 注意，每个print后面加break 可以只运行

# word="Please enter your age:"
# active=True
# while active :
#     age=int(input("Please enter your age:"))
#     if age <= 3:
#         print("No money to pay！")
#         active=False
#         break
#     elif age<=12:
#         print("Please pay for 10 dollars.")
#         active = False
#         break
# else:
#         print("Please pay for 15 dollars.")
#         active = False

# 无限循环
# food=input("Enter the food to add in the pizza:")
# while True:
#     if food=='quit':
#        break
#     else:
#         print("We will add in the pizza.")

# # 题目！！！！！！11！1！11！11!!!
# sandwich_orders=['potato-sandwich','been-sandwich','tomato-sandwich']
# finished_sandwiches=[]
# for sandwich in sandwich_orders:
#     print("I mand your "+sandwich.title()+".")
#
# # 其中的while的作用是把所有的元素添加到空列表中
# while sandwich_orders:
#     currant_sandwich=sandwich_orders.pop()
#     finished_sandwiches.append(currant_sandwich)
#
# print("The finished sandwiches are:")
# for finished_sandwich in finished_sandwiches:
#     print("\t"+finished_sandwich.title())

# sandwich_orders=['potato','pastrami','pastrami','pastrami','been','tomato']
# finished_sandwiches=[]
# # 卖完了的三明治
# print("Pastrami sandwiches are sold.")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print(sandwich_orders)
# # 先打印要制作的三明治
# for sandwich in sandwich_orders:
#     print("I mand your "+sandwich.title()+"sandwich.")
#
# # 其中的while的作用是把所有的元素添加到空列表中
# while sandwich_orders:
#     currant_sandwich=sandwich_orders.pop()
#     finished_sandwiches.append(currant_sandwich)
#
# print("The finished sandwiches are:")
# for finished_sandwich in finished_sandwiches:
#     print("\t"+finished_sandwich.title()+" sandwich")

# 使用用户输入来填充字典
# 这是例子
# responses={}
# active=True
# while active:
#     name=input("Please enter your name: ")
#     response=input("Which mountain would you like to climb? ")
#     responses[name]=response
#     repeat=input("Would you like to let another person respond?(yes/no) ")
#     if repeat=='no':
#         active=False
# print("\n---Poll Result---")
# for name,response in responses.items():
#     print(name+" would like to climb "+response.title()+".")


# 例题
# places={}
# active=True
# while active:
#     name=input("Please enter your name: ")
#     response=input("If you could visit one place in the world,where would you go?")
#     places[name]=response
#     repeat=input("Would you like to let another person respond?(yes/no)")
#     if repeat=='no':
#         active=False
# print("This is answer.")
# for name,place in places.items():
#     print(name.title()+" would like to go to  "+place.title()+".")





