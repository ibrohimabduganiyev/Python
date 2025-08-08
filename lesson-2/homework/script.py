car = 'MsaatmiazD'
car[0::2]

###

txt = "I'am John. I am from London"
txt_words = txt.split()
country = txt_words[5]
print(country)

###

msg = input("matn kiriting, men uni teskari qilib ko'rsataman: ")
text = msg[::-1]
print(f"teskari yozuv: {text}")

###

palindrom = input('matn kiriting men uni palindrom ekanligini tekshiraman')
if palindrom ==palindrom[::-1] : print("palindrom")
else : print("palindrom emas")


###

fruits = ['apple', 'banans', 'grapes', 'melon', 'strawberry']
fruit = fruits[2]
print(fruit)


###

numbers1 = [1, 2, 3, 4, 5]
numbers2=[6, 7, 8, 9, 10]
numbers1.extend(numbers2)

print(numbers1)

###

first = numbers1[0]
middle=numbers1[len(numbers1)//2]
last=numbers1[-1]

new_ls=[first, middle, last]

print(new_ls)

###

countries = ['london', 'parij', 'manchester', 'barcelona']

if 'parij' in countries : print("parij bu ro'yxatda bor")
else : print("parij bu ro'yxatda yo'q")

###

num = [1,2,3]
nums = num*2
print(nums)

###

data = [1,2,3,4,5]
first_num = data[0]
data[0] = data[-1]
data[-1]=first_num
print(data)
