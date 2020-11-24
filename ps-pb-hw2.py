# Обработка словарей и списков

# Объявление переменных типа словарь
account1 = { 'login': 'ivan', 'password': 'q1'}
account2 = { 'login': 'petr', 'password': 'q2'}
account3 = { 'login': 'olga', 'password': 'q3'}
account4 = { 'login': 'anna', 'password': 'q4'}

user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

# Добавление списка состоящего из словарей usern и accountn
user_list = [user1, user2, user3, user4]
account_list = [account1, account2, account3, account4]

# Получение информации о пользователях по ключу

# Ввод ключа. Проверка правильности ввода. Вывод согласно запросу.
try:
    search_key = input ("Введите ключ (name или account): ")
    print ("значение ключа " + search_key + " для юзера 1 = ", user1[search_key.lower()])
    print ("значение ключа " + search_key + " для юзера 2 = ", user2[search_key.lower()])
    print ("значение ключа " + search_key + " для юзера 3 = ", user3[search_key.lower()])
    print ("значение ключа " + search_key + " для юзера 4 = ", user4[search_key.lower()])
except KeyError:
    print ("Введенный ключ не найден")
except:
    print ("Возникла какая то неизвестная ошибка")

# Получение информации о пользователе по порядковому номеру

# Ввод порядового номера. Проверка правильности ввода. Вывод согласно запросу.
try:
    serial_number = int(input("Введите порядковый номер:")) 
    serial_number1 = int (str((serial_number - 1) ** (serial_number-1))) # Проверка на ввод 0 и отрицательного значения
    usern = user_list[serial_number-1] # Переменная для хранения пользователя согласно порядковому номеру
    accountn = account_list[serial_number-1]# Переменная для хранения аккаунта согласно порядковому номеру
    print ("Данные по юзеру № " + str(serial_number) + ":" + '\n' + "имя: " + usern['name'])
    print ("возраст: " + str(usern['age']) + '\n' + "логин: " + accountn['login'] + '\n' + "пароль: " + accountn['password'])
except ValueError:
    print ("Пользователь с таким порядковым номером отсутствует")
except IndexError:
    print ("Пользователь с таким порядковым номером отсутствует")
except:
    print ("Возникла какая то неизвестная ошибка")

# Перемещение пользователя в конец списка

# Ввод порядового номера. Проверка правильности ввода. Вывод списка согласно запросу.
try:
    serial_number = int(input("Введите порядковый номер пользователя, которого нужно переместить в конец: ")) 
    serial_number1 = int (str((serial_number - 1) ** (serial_number-1))) # Проверка на ввод 0 и отрицательного значения
    usern = user_list[serial_number-1] # Переменная для хранения пользователя согласно порядковому номеру
    print ("Список до изменения:")
    print (user_list)
    user_list.remove (user_list[serial_number-1]) # Удаление пользователя
    user_list.append (usern) # Добавление пользователя
    print ("Пользователь с именем " + usern['name'] + " перемещен в онец списка")
    print ("Список после изменения:")
    print (user_list)
    print ("Средний возраст пользователей: ", str((user1['age']+user2['age']+user3['age']+user4['age'])/4))
except ValueError:
    print ("Пользователь с таким порядковым номером отсутствует")
except IndexError:
    print ("Пользователь с таким порядковым номером отсутствует")
except:
    print ("Возникла какая то неизвестная ошибка")
 