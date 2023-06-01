
#Принять у пользователя логин и дату рождения
#Вывести логин пользователя и его ГОД РОЖДЕНИЯ

print("\nEnter your credentials")

print("\t", end='')
userLogin = input("Login: ")

print("\n\tBirthday")

print("\t\t", end='')
userYear = int(input("Year: "))
print("\t\t", end='')
userMonth = int(input("Number of Month: "))
print("\t\t", end='')
userDay = int(input("Number of day: "))

print("\nCredentials:")
print("\tLogin:\t\t\t", userLogin)
print("\tYear birthday:\t", userYear)