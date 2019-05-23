user_age = int(input('Введите ваш возраст: '))

def age_determination(user_age):

    if user_age >= 25:
       return('Добро пожаловать в рабство!')
    elif user_age >= 18:
         return('Вы учитесь в университете')
    elif user_age >= 7:
         return('Ты школьник')
    elif user_age < 7:
         return('Приходи через год, мал ещё')

#print(age_determination(user_age)) - таким вариантом тоже работает

total = age_determination(user_age)
print(total)
   
