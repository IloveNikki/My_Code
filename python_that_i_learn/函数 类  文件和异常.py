def display_message():
    """"显示简单的问候语"""
    print("I learn function in this chapter.")
display_message()

def favorite_book(book_name):
    """"显示一段语句"""
    print("One of my favorite books is "+book_name.title()+".")
favorite_book('alice in wonderland')

def make_shirt(size,logo='I love Python'):
    """"显示一段尺码和字样"""
    print("The size of T-shirt is  "+size+".")
    print("The logo of T-shirt is  "+logo+".")
make_shirt('L','snow')
make_shirt('S',)
make_shirt(size='T',logo='snow')

# def describe_city(city_name,city_country='united states' ):
#     """显示一段信息"""
#     print(city_name.title()+"'s country is "+city_country.title()+".")
# describe_city('wu han','china')
# describe_city('new york')

def city_country(city,country):
    """返回整洁的信息"""
    full_message=city.title()+','+country.title()
    return full_message
messages=city_country('wu han','china')
print(messages)

# def describe_city(city_name,city_country='united states' ):
#     """显示一段信息"""
#     print(city_name.title()+"'s country is "+city_country.title()+".")
# describe_city('wu han','china')
# describe_city('new york')

# def make_album(singer_name,song,number=''):
#     """返回一个字典，其中包含歌手名字和歌曲"""
#     album={'singer':singer_name,'song':song}
#     if number:
#         album['number']=number
#     return album
#
# while True:
#     singer_name=input("Enter the name:")
#     song=input("Enter the song:")
#     if singer_name=='q':
#         break
#     elif song=='quit':
#         break
# for singer_name,song in make_album(singer_name,song).items():
#     print(singer_name+','+song)



# person1=make_album('jimi','shang hai',number=2)
# print(person1)


def show_magicians(names):
 """"显示魔术师的名字"""
 print("There are magician's name:")
 for name in names:
    print("The Great "+name.title())

name=['mike','duck','lucy']
for n in name:
    print("The Great " + n.title())
show_magicians(name)



def sandwich(*toppings):
    """打印顾客所需的一系列食物"""
    print("You order sandwiches are:")
    for topping in toppings:
        print(toppings)
sandwich('potatoes')
sandwich('been','tomatoes','milk')

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('chen', 'yu',
                             location='china',
                             field='physics')
print(user_profile)

# def car(type,maker,color):
#     car_information={}
#     car_information['car_type'] = type
#     car_information['car_maker'] = maker
#     car_information['car_color'] = color
#     for key,value in user_information.items():
#         car_information[key] = value
#     return car_information
# user_information=car('mercedes','sun','black')
# print(user_information)
# 报错的一个代码


# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # 模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

























































































































































































































































