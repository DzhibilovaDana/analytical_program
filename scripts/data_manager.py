"""
Файл: data_manager.py
Авторы: Игошина Дарья Дмиртриевна, Джибилова Дана Аслановна

Этот модуль реализует вывод справочников на экран, возможность редактирования,
добавления, удаления
"""
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from get_from_ini import data_frame_1, data_frame_2
from common_functions import cnv_configure


class DF1(tk.Tk):
    """
    В данном классе реализован вывод справочника 1 в отдельное окно,
    а также он содержит функции ручной модификации файла, ручного добавления и удаления
    """

    def __init__(self):
        """Создание отдельного окна с выведенным справочником 1,
         а также прописано меню этого окна"""
        super().__init__()
        self.resizable(width=False, height=False)
        self.configure(bg="dark sea green")
        self.geometry("1100x800")
        mainmenu = Menu(self)
        self.config(menu=mainmenu)
        self.resizable(True, True)
        self.title("Cправочник 1")
        canvas = tk.Canvas(self, borderwidth=0)
        frame = tk.Frame(canvas)
        scroll_ver = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scroll_hor = tk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        canvas.configure(yscrollcommand=scroll_ver.set)
        scroll_ver.grid()
        canvas.configure(xscrollcommand=scroll_hor.set)
        scroll_hor.grid()
        canvas.grid()
        canvas.create_window((1, 1), window=frame, anchor="nw")
        frame.bind("<Configure>", lambda event, cnv=canvas: cnv_configure)
        actionmenu = Menu(mainmenu, tearoff=0)

        def add_win():
            """Создание окна 'Добавление', содержащее два поля ввода данных, а также кнопку"""
            window = Tk()
            window.resizable(width=False, height=False)
            window.title("Добавление")
            window["bg"] = "dark sea green"
            text = tk.Label(master=window, text="Справочник 1")
            text.grid(column=0, row=0)

            def add_row():
                """Функция добавления полученных в полях ввода данных."""
                day_text = day.get()
                quantity_text = quantity.get()
                data_frame_2 = pd.read_csv("./data/Posecheniya.csv",
                                           delimiter=",", encoding="utf-8", dtype='O')
                data_frame_2.loc[len(data_frame_2) + 1] = [day_text, quantity_text]
                data_frame_2.sort_index()
                data_frame_2.to_csv("./data/Posecheniya.csv")
                exclude_column = ""
                data_frame_2 = data_frame_2.loc[:, data_frame_2.columns != exclude_column]
                data_frame_2.to_csv("./data/Posecheniya.csv", index=False, sep=',')
                messagebox.showinfo("Успех", "Строка успешно добавлена")
                refresh(self, data_frame_2)

            tx1 = tk.Label(master=window, text="День недели")
            tx1.grid(row=1)
            tx2 = tk.Label(master=window, text="Количество посещений")
            tx2.grid(row=2)
            day = tk.Entry(master=window, bg='pink3')
            day.grid(row=1, column=1, sticky=tk.W)
            quantity = tk.Entry(master=window, bg='pink3')
            quantity.grid(row=2, column=1, sticky=tk.W)
            btn_submit = tk.Button(master=window, text="Добавить", bg='grey', command=add_row)
            btn_submit.grid(column=0, row=3)

        def edit():
            """Создание окна 'Редактирование' с тремя полями ввода и одной кнопкой"""
            window = Tk()
            window.resizable(width=False, height=False)
            window.title("Редактирование")
            window["bg"] = "dark sea green"
            text = tk.Label(master=window, text="Справочник 1")
            text.grid(column=0, row=0)
            text_1 = tk.Label(master=window, text="Введите номер строки")
            text_1.grid(row=1)
            text_2 = tk.Label(master=window, text="Введите номер столбца")
            text_2.grid(row=2)
            text_3 = tk.Label(master=window, text="Введите новое значение ячейки")
            text_3.grid(row=3)
            row_num = tk.Entry(master=window, bg='pink3')
            row_num.grid(row=1, column=1, sticky=tk.W)
            column_num = tk.Entry(master=window, bg='pink3')
            column_num.grid(row=2, column=1, sticky=tk.W)
            new_value = tk.Entry(master=window, bg='pink3')
            new_value.grid(row=3, column=1, sticky=tk.W)

            def cell_change():
                """Функция добавления полученных в полях ввода данных в заданную ячейку"""
                row_num_text = row_num.get()
                row_num_text = int(row_num_text)
                column_num_text = column_num.get()
                column_num_text = int(column_num_text)
                new_value_text = new_value.get()
                data_frame_2 = pd.read_csv("./data/Posecheniya.csv", delimiter=",",
                                           encoding="utf-8", dtype='O')
                data_frame_2.iloc[row_num_text - 1, column_num_text - 1] = new_value_text
                data_frame_2.to_csv("./data/Posecheniya.csv", index=False, sep=',')
                messagebox.showinfo("Успех", "Строка успешно изменена")
                refresh(self, data_frame_2)

            button = tk.Button(window, text="Редактировать", command=cell_change)
            button.grid(column=0, row=4)

        def delete_row(entry, window):
            """Функция проверяет введенное число на соответствие необходимым
             параметрам, а также удаляет нужную строку.

            На вход принимает переменные:
            window - окно с полем введения номера удаляемой строки
            enrty - поле ввода данных
            """
            data_frame_2 = pd.read_csv("./data/Posecheniya.csv", delimiter=",", encoding="utf-8",
                                       dtype='O')
            # получаем введенное значение из текстового поля
            row_num = entry.get()

            # проверяем, что введено число
            if row_num.isdigit() == False:
                messagebox.showerror("Ошибка", "Пожалуйста, введите число")
                return
            row_num = int(row_num)

            # Проверяем, что введенное число соответствует диапазону индексов строк DataFrame
            if row_num < 0 or row_num >= len(data_frame_2):
                messagebox.showerror("Ошибка", "Недопустимый номер строки")
                return
            else:
                # Удаляем строку из DataFrame
                data_frame_2 = data_frame_2[data_frame_2.index != row_num]
                data_frame_2.to_csv("./data/Posecheniya.csv", index=False)

                messagebox.showinfo("Успех", "Строка успешно удалена")
                window.destroy()
                refresh(self, data_frame_2)

        def delete_window():
            """
            Создание окна 'Удаление строки'.
            Содержит одно поле ввода, а также одну кнопку
            """
            # Создаем графический интерфейс
            window = tk.Toplevel()
            window.title("Удаление строки")

            # Создаем метку и текстовое поле
            label = tk.Label(window, text="Введите номер строки:")
            label.grid(column=0, row=0)
            entry = tk.Entry(window)
            entry.grid(column=0, row=1)

            def delete_row_without_traceback():
                """Функция вызывает delete_row без получения ошибки Tracebask"""
                delete_row(entry, window)

            # Создаем кнопку для удаления строки
            button = tk.Button(window, text="Удалить", command=delete_row_without_traceback)
            button.grid(column=0, row=2)

        actionmenu.add_command(label="Редактирование", command=edit)
        actionmenu.add_command(label="Удаление", command=delete_window)
        actionmenu.add_command(label="Добавление", command=add_win)
        mainmenu.add_cascade(label="Редактировать", menu=actionmenu)

        def refresh(window, data):
            """
            Функция обновляет данные в окне с выведенным справочнииком 1

            На вход получает переменные:
            window - окно с выведенным сравочником
            data_frame_2 - DataFrame, содержащий считанный файл формата .csv"""
            list1 = list(data)
            r_set = data.to_numpy().tolist()  # create list of list using rows
            trv = ttk.Treeview(window, selectmode='browse', height=6,
                               show='headings', columns=list1)
            trv.place(x=0, y=0, width=1100, height=800)
            for i in list1:
                trv.column(i, width=150)
                trv.heading(i, text=str(i))
            for dif_t in r_set:
                value = list(dif_t)
                trv.insert("", 'end', iid=value[0], values=value)

        refresh(self, data_frame_2)


class DF2(tk.Tk):
    """
    Создание отдельного окна с выведенным справочником 2,
    а также тут прописано меню этого окна
    """

    def __init__(self):
        super().__init__()
        self.resizable(width=False, height=False)
        self.configure(bg="dark sea green")
        self.geometry("1100x800")
        mainmenu = Menu(self)
        self.config(menu=mainmenu)
        self.resizable(True, True)
        self.title("Cправочник 2")
        canvas = tk.Canvas(self, borderwidth=0)
        frame = tk.Frame(canvas)
        scroll_ver = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scroll_hor = tk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        canvas.configure(yscrollcommand=scroll_ver.set)
        scroll_ver.grid()
        canvas.configure(xscrollcommand=scroll_hor.set)
        scroll_hor.grid()
        canvas.grid()
        canvas.create_window((1, 1), window=frame, anchor="nw")
        frame.bind("<Configure>", lambda event, cnv=canvas: cnv_configure)
        actionmenu = Menu(mainmenu, tearoff=0)

        def add_win():
            """Создание окна 'Добавление', содержащее семь полей ввода данных, а также кнопку"""
            window = Tk()
            window.resizable(width=False, height=False)
            window.title("Добавление")
            window["bg"] = "dark sea green"
            label = tk.Label(master=window, text="Справочник 1")
            label.grid(column=0, row=0)

            def add_row():
                """Функция добавления полученных в полях ввода данных в виде новой строки"""
                name_text = name.get()
                day_text = day.get()
                cost_text = cost.get()
                dish_type_text = dish_type.get()
                vegan_text = vegan.get()
                heft_text = heft.get()
                kbn_text = kbn.get()
                data_frame_1 = pd.read_csv("./data/StolovoyaMIEM.csv",
                                           delimiter=",", encoding="utf-8", dtype='O')
                data_frame_1.loc[len(data_frame_1)] = [name_text, day_text, cost_text,
                                                       dish_type_text, vegan_text, heft_text, kbn_text]
                data_frame_1.sort_index()
                data_frame_1.to_csv("./data/StolovoyaMIEM.csv")
                exclude_column = ""
                data_frame_1 = data_frame_1.loc[:, data_frame_1.columns != exclude_column]
                data_frame_1.to_csv("./data/StolovoyaMIEM.csv", index=False, sep=',')
                messagebox.showinfo("Успех", "Строка успешно добавлена")
                refresh(self, data_frame_1)

            tx1 = tk.Label(master=window, text="Название блюда")
            tx1.grid(row=1)
            tx2 = tk.Label(master=window, text="День недели")
            tx2.grid(row=2)
            tx3 = tk.Label(master=window, text="Стоимость блюда")
            tx3.grid(row=3)
            tx4 = tk.Label(master=window, text="Тип блюда")
            tx4.grid(row=4)
            tx5 = tk.Label(master=window, text="Подходит ли блюдо вегатерианцам")
            tx5.grid(row=5)
            tx6 = tk.Label(master=window, text="Вес/объем одной порции(г/мл)")
            tx6.grid(row=6)
            tx7 = tk.Label(master=window, text="Комплекс/бизнес/ничего")
            tx7.grid(row=7)
            name = tk.Entry(master=window, bg='pink3')
            name.grid(row=1, column=1, sticky=tk.W)
            day = tk.Entry(master=window, bg='pink3')
            day.grid(row=2, column=1, sticky=tk.W)
            cost = tk.Entry(master=window, bg='pink3')
            cost.grid(row=3, column=1, sticky=tk.W)
            dish_type = tk.Entry(master=window, bg='pink3')
            dish_type.grid(row=4, column=1, sticky=tk.W)
            vegan = tk.Entry(master=window, bg='pink3')
            vegan.grid(row=5, column=1, sticky=tk.W)
            heft = tk.Entry(master=window, bg='pink3')
            heft.grid(row=6, column=1, sticky=tk.W)
            kbn = tk.Entry(master=window, bg='pink3')
            kbn.grid(row=7, column=1, sticky=tk.W)
            btn_submit = tk.Button(master=window, text="Добавить", bg='grey', command=add_row)
            btn_submit.grid(column=0, row=8)

        def edit():
            """Создание окна 'Редактирование' с тремя полями ввода и одной кнопкой"""
            window = Tk()
            window.resizable(width=False, height=False)
            window.title("Редактирование")
            window["bg"] = "dark sea green"
            tx = tk.Label(master=window, text="Справочник 2")
            tx.grid(column=0, row=0)
            tx1 = tk.Label(master=window, text="Введите номер строки")
            tx1.grid(row=1)
            tx2 = tk.Label(master=window, text="Введите номер столбца")
            tx2.grid(row=2)
            tx3 = tk.Label(master=window, text="Введите новое значение ячейки")
            tx3.grid(row=3)
            row_num = tk.Entry(master=window, bg='pink3')
            row_num.grid(row=1, column=1, sticky=tk.W)
            column_num = tk.Entry(master=window, bg='pink3')
            column_num.grid(row=2, column=1, sticky=tk.W)
            new_value = tk.Entry(master=window, bg='pink3')
            new_value.grid(row=3, column=1, sticky=tk.W)

            def cell_change():
                """Функция добавления полученных в полях ввода данных в заданную ячейку"""
                row_num_text = row_num.get()
                row_num_text = int(row_num_text)
                column_num_text = column_num.get()
                column_num_text = int(column_num_text)
                new_value_text = new_value.get()
                data_frame_2 = pd.read_csv("./data/StolovoyaMIEM.csv", delimiter=",",
                                           encoding="utf-8", dtype='O')
                data_frame_2.iloc[row_num_text - 1, column_num_text - 1] = new_value_text
                data_frame_2.to_csv("./data/StolovoyaMIEM.csv", index=False, sep=',')
                messagebox.showinfo("Успех", "Строка успешно изменена")
                refresh(self, data_frame_2)

            button = tk.Button(window, text="Редактировать", command=cell_change)
            button.grid(column=0, row=4)

        def delete_row(entry, window):
            """
            Функция проверяет введенное число на соответствие
            необходимым параметрам, а также удаляет нужную строку.

            На вход принимает переменные:
            window - окно с полем введения номера удаляемой строки
            enrty - поле ввода данных
            """
            data_frame_1 = pd.read_csv("./data/StolovoyaMIEM.csv", delimiter=",", encoding="utf-8",
                                       dtype='O')

            # Получаем введенное значение из текстового поля
            row_num = entry.get()

            # Проверяем, что введено число'
            if not row_num.isdigit():
                messagebox.showerror("Ошибка", "Пожалуйста, введите число")
                return
            row_num = int(row_num)

            # Проверяем, что введенное число соответствует диапазону индексов строк DataFrame
            if row_num < 0 or row_num >= len(data_frame_1):
                messagebox.showerror("Ошибка", "Недопустимый номер строки")
                return
            else:
                # Удаляем строку из DataFrame
                print(data_frame_1)

                data_frame_1 = data_frame_1[data_frame_1.index != row_num]
                print(data_frame_1)
                data_frame_1.to_csv("./data/StolovoyaMIEM.csv", index=False)

                messagebox.showinfo("Успех", "Строка успешно удалена")
                window.destroy()
                refresh(self, data_frame_1)

        def delete_window():
            """
            Создание окна 'Удаление строки'.
            Содержит одно поле ввода, а также одну кнопку
            """
            # Создаем графический интерфейс
            window = tk.Toplevel()
            window.title("Удаление строки")

            # Создаем метку и текстовое поле
            label = tk.Label(window, text="Введите номер строки:")
            label.grid(column=0, row=0)
            entry = tk.Entry(window)
            entry.grid(column=0, row=1)

            def delete_row_without_traceback():
                """
                Функция вызывает delete_row без
                получения ошибки Tracebask
                """
                delete_row(entry, window)

            # Создаем кнопку для удаления строки
            button = tk.Button(window, text="Удалить", command=delete_row_without_traceback)
            button.grid(column=0, row=2)

        actionmenu.add_command(label="Редактирование", command=edit)
        actionmenu.add_command(label="Удаление", command=delete_window)
        actionmenu.add_command(label="Добавление", command=add_win)
        mainmenu.add_cascade(label="Редактировать", menu=actionmenu)

        def refresh(window, data_frame_1):  # Refresh the Treeview to reflect changes
            """Функция обновляет данные в окне с выведенным справочнииком 2

           На вход получает переменные:
           window - окно с выведенным сравочником
           data_frame_1 - DataFrame, содержащий считанный файл формата .csv"""
            list1 = list(data_frame_1)
            r_set = data_frame_1.to_numpy().tolist()  # create list of list using rows
            trv = ttk.Treeview(window, selectmode='browse', height=6,
                               show='headings', columns=list1)
            trv.place(x=0, y=0, width=1100, height=800)
            for i in list1:
                trv.column(i, width=150)
                trv.heading(i, text=str(i))
            for dif_t in r_set:
                value = list(dif_t)
                trv.insert("", 'end', iid=value[0], values=value)

        refresh(self, data_frame_1)
