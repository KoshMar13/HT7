import csv_cr
# import inp_mod as im
import random
# import xlsx_cr
import txt_cr


def start():
    mod = int(input(
        'Введите режим работы. 1 - экспорт в csv; 2 - импорт из csv; 3 - экспорт в txt; 4 - импорт из txt: '))
    if mod == 1:
        n = int(input('Insert phonebook lenght: '))
        res = list()
        for i in range(n):
            pers = list(
                map(str, input('Insert name, phone number, note: ').split()))
            pers.insert(0, random.randint(1000, 9999))
            res.append(pers)
        csv_cr.exportCsv(res)

    elif mod == 2:
        book = csv_cr.csvImp()
        for i in book:
            print(i)

    elif mod == 3:
        n = int(input('Insert phonebook lenght: '))
        res = list()
        for i in range(n):
            pers = list(
                map(str, input('Insert name, phone number, note: ').split()))
            pers.insert(0, random.randint(1000, 9999))
            res.append(pers)
        txt_cr.imp_txt(res)

    else:
        res = txt_cr.exp_txt()
        # def show_menu():
        #     print("\n" + "=" * 20)
        #     print("Выберите необходимое действие")
        #     print("1. Найти сотрудника")
        #     print("2. Сделать выборку сотрудников по должности")
        #     print("3. Сделать выборку сотрудников по зарплате")
        #     print("4. Добавить сотрудника")
        #     print("5. Удалить сотрудника")
        #     print("6. Обновить данные сотрудника")
        #     print("7. Экспортировать данные в формате json")
        #     print("8. Экспортировать данные в формате cmv")
        #     print("9. Закончить работу")
        #     a = int(input("Введите номер необходимого действия: "))

        #     if a == 1:
        #         name = inp.last_name()
        #         findemployee.PersonFinder(name)
        #         logg.log_info(name)
        #     elif a == 2:
        #         job = inp.PostJob()
        #         findemployee.PersonFinder(job)
        #         logg.log_info(job)
