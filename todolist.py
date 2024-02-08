from datetime import date

# Создаем текстовый файл (название файла - текущая дата, установленная на ПК)
current_date = date.today()
filename = f"{current_date}.txt"
file = open(filename, 'w')

# Записываем в файл введённые значения
while True:
    task = input("Введите задачу (для завершения введите '-done'):\n")
    if task == "-done":
        break
    else:
        file.write(task + "\n")

# Завершаем работу с программой
file.close()
print(f"Создан файл {filename}")
