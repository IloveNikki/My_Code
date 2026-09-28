print("Hello from PyCharm!")
message="Hello from PyCharm!"
print(message)
first_name="chen"
last_name="yu"
full_name=first_name+" "+last_name
print(full_name)
message="A person tried anything new."
words="Albert said,"+message
print(words)
print("Name:\nchen kexing\nis ")
n=3
n+=2
print(
n)
print("5+3\n2+2*3\n5+6/2\n1+7")

num="1,2,3"
print("%d",num)
names=['chen ke xin','chen zao xin','liu jia li','liu  jia cen']
message='Hello,'+names[1].title()+'.'
print(message)
ways=['motorcycle','bicycle','car']
message='I would like to own a '+ways[0]+'.'
messages='I would like to own a '+ways[1]+'.'
word='I would like to own a '+ways[2]+'.'
print(message)
print(messages)
print(word)

people=['xiao ming','xiao hong','xiao ling']
message='I would like to invite '+people[2].title()+'.'
print(people)
print(message)
people[2]='xiao yu'
messages='I would like to invite '+people[2].title()+'.'
print(people)
print(messages)

people.append('xiao li')
print(people)
people.insert(0,'xiao yue')
print(people)
people.insert(2,'xiao te')
print(people)
people.append('xiao wu')
print(people)
message='I would like to invite '+people[1].title()+'.'
print(message)
del people[1]
del people[0]
print(people)
popped_people=people.pop()
words='Sorry,I could not invite you'
print(words)
print(people)
popped_people=people.pop()
words='Sorry,I could not invite you'
print(words)
print(people)
popped_people=people.pop()
words='Sorry,I could not invite you'
print(words)
print(people)


places=['beijing','yunnan','hubei','jiangsu','jiangxi']
print(places)


print(sorted(places))
places.sort(reverse=True)
print(places)
places.reverse()
print(places)
print(places[-1])

foods=['green pizza','pink pizza','black pizza']
for food in foods:
    print('I like '+food)
print("I really like pizza!")
friends_foods=foods[:]
print(friends_foods)
friends_foods.append("pizza")
print(friends_foods)
foods.append("blue pizza")
print(foods)

print("My favorite foods are: ")
for food in foods:
    print(food.title())

print("My friends favorite foods are: ")
for food in friends_foods:
    print(food.title())
















animals=['dog','cat','bird','dog']
for animal in animals:
    print('A '+animal+' would make a great pet!')
print("Any of this animals would make a great pet!")


foods=('green been','pink been','black been')
for food in foods:
    print(food)
foods=('green been','pink been')
for food in foods:
    print(food)


age=12
if age>=18:
    print('You are old enough to vote!')
else :
    print('You are  enough to vote!')

