"""
Файл: text_information.py
Авторы: Игошина Дарья Дмиртриевна, Джибилова Дана Аслановна

Данный файл содержит функции для для получения следующих текстовых отчетов:
поиск самых популярных блюд (простой текстовый отчет 1)
поиск самых дешевых блюд (простой текстовый отчет 2), статистический отчет,
сводная таблица
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from common_functions import cnv_configure
from common_functions import refresh
from get_from_ini import *

from get_from_ini import denorm


def refresh1(window, d_f):
    """
    Данная функция выводит на экран реализованную сводную таблицу.
    """
    l_1_dict = dict(zip(d_f.index, d_f.values))
    l_1_list = list(l_1_dict.keys())
    l_1 = list(d_f)
    l_1.insert(0, 'День недели')
    r_set = d_f.to_numpy().tolist()  # create list of list using rows
    need = 0
    for i in r_set:
        i.insert(0, l_1_list[need])
        need += 1
    trv = ttk.Treeview(window, selectmode='browse', height=6,
                       show='headings', columns=l_1)
    trv.place(x=0, y=0, width=1100, height=800)
    for i in l_1:
        trv.column(i, width=150)
        trv.heading(i, text=str(i))
    for dif_t in r_set:
        value = list(dif_t)
        trv.insert("", 'end', iid=value[0], values=value)


def simp_report_1():
    """
    Данная функция реализует простой текстовый отчет:
    поиск самых популярных блюд.
    """

    def export(out, k):
        """
        Функция осуществяет экспорт отчета в выбранный файл (.xlsx/.csv/.pkl)
        """
        if k == 0:
            out.to_excel(export_simp_1_xlsx, index=True)
        elif k == 1:
            out.to_csv(export_simp_1_csv, index=True)
        elif k == 2:
            out.to_pickle(export_simp_1_pkl, index=True)

    def win():
        try:
            visits = int(txt1.get())
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Пожалуйста,"
                                                 " введите корректное"
                                                 " количество посещений (число).")
            return

        type_dish = txt2.get()
        if type_dish not in ['Комплекс', 'Бизнес', 'Ничего']:
            messagebox.showerror("Ошибка ввода", "Пожалуйста,"
                                                 " введите корректный тип"
                                                 " блюда (комплекс, бизнес, ничего).")
            return
        visits = int(visits)
        type_dish = txt2.get()
        menu = tk.Menu(window)
        window.config(menu=menu)

        # Создание меню для экспорта
        exp = tk.Menu(menu, tearoff=0)
        exp.add_command(label="Cохранить как .xlsx",
                        command=lambda: export(simp_1, 0))
        exp.add_command(label="Cохранить как .csv",
                        command=lambda: export(simp_1, 1))
        exp.add_command(label="Cохранить как .pkl",
                        command=lambda: export(simp_1, 2))
        menu.add_cascade(label="Экспорт", menu=exp)
        k = (denorm["Кол-во посещений"] >= visits) & (denorm["КБН"] == type_dish)
        simp_1 = denorm.loc[k, ["Название блюда", "День недели"]]
        dish_name = simp_1.get("Название блюда")
        dish_day = simp_1.get("День недели")

        frame = Frame(window)
        frame.grid()

        table = ttk.Treeview(frame)

        table['columns'] = ('name', 'day')

        table.column("#0", width=0, stretch=NO)
        table.column("name", anchor=CENTER, width=100)
        table.column("day", anchor=CENTER, width=80)

        table.heading("#0", text="", anchor=CENTER)
        table.heading("name", text="Название блюда", anchor=CENTER)
        table.heading("day", text="День недели", anchor=CENTER)
        table.pack()
        a_1 = 0
        for row in dish_name:
            print(row)
            a_2 = 0
            for i in dish_day:
                if a_2 == a_1:
                    print(i)
                    table.insert(parent='', index='end', text='', values=(row, i))
                a_2 += 1
            a_1 += 1

    # создание нового окна с помощью tkinter
    window = Tk()
    window.title("Текстовая информация")
    window.geometry("430x300")
    window["bg"] = "dark sea green"
    lb1 = Label(window, text="Поиск самых популярных блюд", bg='dark sea green')
    lb1.configure(font=("Courier", 16))
    lb1.grid(column=0, row=0)
    lb2 = Label(window, text="Количество посещений", bg='dark sea green')
    lb2.grid(column=0, row=1)
    lb3 = Label(window, text="Тип блюда(Комплекс/Бизнес/Ничего)", bg='dark sea green')
    lb3.grid(column=0, row=3)
    txt1 = Entry(window, width=50, bg='grey')
    txt1.grid(column=0, row=2)
    txt2 = Entry(window, width=50, bg='grey')
    txt2.grid(column=0, row=4)
    bt1 = Button(window, text="Найти", bg='grey', command=win)
    bt1.grid(column=1, row=5)

    window.mainloop()


def simp_report_2():
    """
    Данная функция реализует простой текстовый отчет:
    поиск самых популярных блюд.
    """

    def export(out, k):
        """
        Функция осуществяет экспорт отчета в выбранный файл (.xlsx/.csv/.pkl)
        """
        if k == 0:
            out.to_excel(export_simp_2_xlsx, index=True)
        elif k == 1:
            out.to_csv(export_simp_2_csv, index=True)
        elif k == 2:
            out.to_pickle(export_simp_2_pkl, index=True)

    def most_cheap_dish():

        day = txt1.get()
        if day not in ['Понедельник', 'Вторник', 'Среда',
                       'Четверг', 'Пятница', 'Суббота', 'Воскресенье']:
            messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректный день недели.")
            return

        try:
            price = int(txt2.get())
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Пожалуйста,"
                                                 " введите корректную стоимость блюда (число).")
            return
        # Создание меню для экспорта
        menu = tk.Menu(window)
        window.config(menu=menu)
        exp = tk.Menu(menu, tearoff=0)
        exp.add_command(label="Cохранить как .xlsx",
                        command=lambda: export(simp_2, 0))
        exp.add_command(label="Cохранить как .csv",
                        command=lambda: export(simp_2, 1))
        exp.add_command(label="Cохранить как .pkl",
                        command=lambda: export(simp_2, 2))
        menu.add_cascade(label="Экспорт", menu=exp)
        k = (denorm["День недели"] == day) & (denorm["Стоимость блюда"] <= price)
        simp_2 = denorm.loc[k, ["Название блюда", "Тип блюда"]]
        dish_name = simp_2.get("Название блюда")
        type_dish = simp_2.get("Тип блюда")
        dish_type = simp_2.get("Тип блюда")
        print(dish_type)
        print(dish_name)

        frame = Frame(window)
        frame.grid()

        table = ttk.Treeview(frame)

        table['columns'] = ('name', 'type')

        table.column("#0", width=0, stretch=NO)
        table.column("name", anchor=CENTER, width=100)
        table.column("type", anchor=CENTER, width=80)

        table.heading("#0", text="", anchor=CENTER)
        table.heading("name", text="Название блюда", anchor=CENTER)
        table.heading("type", text="Тип блюда", anchor=CENTER)
        table.pack()

        a_1 = 0
        for row in dish_name:
            print(row)
            a_2 = 0
            for i in type_dish:
                if a_2 == a_1:
                    print(i)
                    table.insert(parent='', index='end', text='', values=(row, i))
                a_2 += 1
            a_1 += 1

    # создание нового окна с помощью tkinter
    window = Tk()
    window.title("Текстовая информация")
    window.geometry("430x300")
    window["bg"] = "dark sea green"
    lb1 = Label(window, text="Поиск самых дешевых блюд", bg='dark sea green')
    lb1.configure(font=("Courier", 16))
    lb1.grid(column=0, row=0)
    lb2 = Label(window, text="День недели", bg='dark sea green')
    lb2.grid(column=0, row=1)
    lb3 = Label(window, text="Стоимость блюда", bg='dark sea green')
    lb3.grid(column=0, row=3)
    txt1 = Entry(window, width=50, bg='grey')
    txt1.grid(column=0, row=2)

    txt2 = Entry(window, width=50, bg='grey')
    txt2.grid(column=0, row=4)

    bt1 = Button(window, text="Найти", bg='grey', command=most_cheap_dish)
    bt1.grid(column=1, row=5)

    window.mainloop()


def stat_report():
    """
    Данная функция реализует статистический текстовый отчет по атрибутам:
    'Стоимость блюда', 'Количество посещений'.
    """

    def export(out, k):
        """
        Функция осуществяет экспорт отчета в выбранный файл (.xlsx/.csv/.pkl)
        """
        if k == 0:
            out.to_excel(export_stat_xlsx, index=True)
        elif k == 1:
            out.to_csv(export_stat_csv, index=True)
        elif k == 2:
            out.to_pickle(export_stat_pkl, index=True)

    # создание нового окна с помощью tkinter
    window = tk.Toplevel()
    window.geometry("1100x200")

    # Создание меню для экспорта
    menu = tk.Menu(window)
    window.config(menu=menu)
    exp = tk.Menu(menu, tearoff=0)
    exp.add_command(label="Cохранить как .xlsx",
                    command=lambda: export(table_stat, 0))
    exp.add_command(label="Cохранить как .csv",
                    command=lambda: export(table_stat, 1))
    exp.add_command(label="Cохранить как .pkl",
                    command=lambda: export(table_stat, 2))
    menu.add_cascade(label="Экспорт", menu=exp)
    window.title("Формирование сводной таблицы")
    window.resizable(False, False)
    window.title("Статистический отчет по атрибутам: Стоимость блюда, Количество посещений")
    canvas = tk.Canvas(window, borderwidth=0)
    frame = tk.Frame(canvas)
    scroll_ver = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
    scroll_hor = tk.Scrollbar(window, orient="horizontal", command=canvas.xview)
    canvas.configure(yscrollcommand=scroll_ver.set)
    scroll_ver.grid()
    canvas.configure(xscrollcommand=scroll_hor.set)
    canvas.grid()
    canvas.create_window((1, 1), window=frame, anchor="nw")
    frame.bind("<Configure>", lambda event, cnv=canvas: cnv_configure(canvas))

    table_stat = pd.DataFrame()
    table_stat["Значения"] = ["Стоимость блюда", "Кол-во посещений"]
    table_stat["Максимальное значение"] = [denorm["Стоимость блюда"].max(
    ), denorm["Кол-во посещений"].max()]
    table_stat["Минимальное значение"] = [denorm["Стоимость блюда"].min(
    ), denorm["Кол-во посещений"].min()]
    table_stat["mean"] = [denorm["Стоимость блюда"].mean(
    ), denorm["Кол-во посещений"].mean()]
    table_stat["Дисперсия"] = [
        denorm["Стоимость блюда"].var(), denorm["Кол-во посещений"].var()]
    table_stat["Стандартное отклонение"] = [
        denorm["Стоимость блюда"].std(), denorm["Кол-во посещений"].std()]

    refresh(window, table_stat)


def summary_table():
    """
    Данная функция реализует сводную таблицу по атрибутам:
    'Стоимость блюда', 'Количество посещений',
    по индексу 'День недели'.
    """
    # Получение сводной таблицы
    sum_table = pd.pivot_table(denorm, index="День недели",
                               values=["Стоимость блюда", "Кол-во посещений"])

    def export(out, k):
        """
        Функция осуществяет экспорт отчета в выбранный файл (.xlsx/.csv/.pkl)
        """
        if k == 0:
            out.to_excel(export_sum_xlsx, index=True)
        elif k == 1:
            out.to_csv(export_sum_csv, index=True)
        elif k == 2:
            out.to_pickle(export_sum_pkl, index=True)

    # создание нового окна с помощью tkinter
    window = tk.Toplevel()
    window.geometry("1120x300")
    menu = tk.Menu(window)
    window.config(menu=menu)

    # Создание меню для экспорта
    exp = tk.Menu(menu, tearoff=0)
    exp.add_command(label="Cохранить как .xlsx",
                    command=lambda: export(sum_table, 0))
    exp.add_command(label="Cохранить как .csv",
                    command=lambda: export(sum_table, 1))
    exp.add_command(label="Cохранить как .pkl",
                    command=lambda: export(sum_table, 2))
    menu.add_cascade(label="Экспорт", menu=exp)
    window.title("Формирование сводной таблицы")
    canvas = tk.Canvas(window, borderwidth=0)
    frame = tk.Frame(canvas)
    scroll_ver = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
    scroll_hor = tk.Scrollbar(window, orient="horizontal", command=canvas.xview)
    canvas.configure(yscrollcommand=scroll_ver.set)
    scroll_ver.pack(side="right", fill='y')
    canvas.configure(xscrollcommand=scroll_hor.set)
    scroll_hor.pack(side="bottom", fill='x')
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((1, 1), window=frame, anchor="nw")
    frame.bind("<Configure>", lambda event, cnv=canvas: cnv_configure(canvas))
    refresh1(window, sum_table)
