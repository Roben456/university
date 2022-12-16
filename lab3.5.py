firstname = input("Введите Имя: ")
lastname = input("Введите Фамилия: ")
group = input("Введите группу: ")

print("Привет, %s %s из группы %s!" % firstname, lastname, group)
email = input("Введите электронную почту: ")

sipher = (lastname[:5] + firstname[:5] * 2 + email[:5] * 3).lower()