#Введи пароль
p=int(input())
if p<8:
    print('Слишком короткий пароль')
if p>=8:
    print('Пароль принят')

status=input()
if status=='online':
    print('Связь установлена')
else:
    if status=='offline':
        print('Связь потеряна')

level=int(input('Уровень угрозы'))
if  level>=1 and level<=30:
          print('Низкий уровень угрозы')
elif level>=31 and level<=70:
    print('Средний уровень угрозы')
elif  level>=71 and level<=100:
    print('Критический  уровень угрозы')
else:
    print('Ошибка ввода')

# Даны две контрольные суммы
checksum_original = input("Введите оригинальную контрольную сумму: ")
checksum_current = input("Введите текущую контрольную сумму: ")
# Используем тернарный оператор
status = "Файл не изменён" if checksum_original == checksum_current else "Файл повреждён"
# Выводим результат
print(status)        


# Ввод кода события
event_code = input("Введите код события: ")
# Обработка с помощью match-case
match event_code:
    case "ERR":
        print("Ошибка системы")
    case "WRN":
        print("Предупреждение")
    case "INF":
        print("Информационное сообщение")
    case _:
        print("Неизвестный код события")
