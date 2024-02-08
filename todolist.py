from datetime import date

def create_list():
    current_date = date.today()
    filename = f"{current_date}.txt"
    file = open(filename, 'w')

    
    while True:
        task = input("Введите задачу (для завершения введите '-done'):\n")
        if task == "-done":
            break
        else:
            file.write(task + "\n")
    file.close()
    print(f"Создан файл {filename}")


create_list()