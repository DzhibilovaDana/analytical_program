"""
Файл: main.py
Авторы: Игошина Дарья Дмиртриевна, Джибилова Дана Аслановна

Этот модуль реализует графический пользовательский интерфейс
главного окна приложения для работы с базами данных.
"""

import tkinter as tk
from tkinter import *
import os
import sys
from data_manager import DF1, DF2
from graf_information import graf_report_1, graf_report_2, graf_report_3, graf_report_4
from text_information import stat_report, simp_report_1, simp_report_2, summary_table
from get_from_ini import root_size, light_col, dark_col, sun, moon

# Добавляем директорию с проектом в путь
os.chdir('/work')
sys.path.append('/work')

# Создаем главное окно
root = Tk()
root.title("Итоговый проект")
root.geometry(root_size)
root["bg"] = light_col
root.resizable(width=False, height=False)

# Инициализация изображений для переключения тем
light = PhotoImage(file=sun)
dark = PhotoImage(file=moon)

switch_value = BooleanVar(value=True)


def switch_theme():
    """
    Данная функция реализует изменение графического интерфейса
    (светлая и темная тема)
    """
    if switch_value.get():
        switch.config(image=dark, bg=dark_col,
                      activebackground=dark_col)
        # Изменение на темную тему
        root.config(bg=dark_col)
        switch_value.set(False)
    else:
        switch.config(image=light, bg=light_col,
                      activebackground=light_col)
        # Изменение на светлую тему
        root.config(bg=light_col)
        switch_value.set(True)


# Создание кнопки для переключения между светлой и темной темой
switch = Button(root, image=light,
                bd=0, bg=light_col,
                activebackground=light_col,
                command=switch_theme)
switch.place(relx=0.9, rely=0.85)


def go_box_1(_):
    """
    Функция реализует работу listbox под кнопкой 'Список'
    """
    lb_course_selection = Lb1.curselection()
    print(lb_course_selection)
    for lst in lb_course_selection:
        if lst == 0:
            DF1()
        elif lst == 1:
            DF2()


# Создание листбокса 'Список'
Lb1 = Listbox(selectbackground='pink3', height=4, width=20)
Lb1.insert(0, 'Cписок 1')
Lb1.insert(1, 'Список 2')
Lb1.bind('<Double-Button-1>', go_box_1)
Lb1.grid()


def lb1():
    """
    Данная функция вызывает listbox по кнопке 'Список'
    """
    Lb1.grid(column=0, row=1)
    Lb1.grid()


def go_box_2(_):
    """
    Функция реализует работу listbox под кнопкой 'Текстовая информация'
    """
    lb_course_selection = Lb2.curselection()
    print(lb_course_selection)
    for lst in lb_course_selection:
        if lst == 0:
            simp_report_1()
        elif lst == 1:
            simp_report_2()
        elif lst == 2:
            stat_report()
        elif lst == 3:
            summary_table()


# Создание листбокса 'Текстовая информация'
Lb2 = Listbox(selectbackground='pink3', height=4, width=45)
Lb2.insert(0, 'Поиск самых популярных блюд')
Lb2.insert(1, 'Поиск самых дешевых блюд')
Lb2.insert(2, 'Статистический отчет')
Lb2.insert(3, 'Сводная таблица')
Lb2.bind('<Double-Button-1>', go_box_2)


def lb2():
    """
    Данная функция вызывает listbox по кнопке 'Текстовая информация'
    """
    Lb2.grid(column=1, row=1)
    Lb2.grid()


def go_box_3(_):
    """
    Функция реализует работу listbox под кнопкой 'Графическая информация'
    """
    lb_course_selection = Lb3.curselection()
    for lst in lb_course_selection:
        if lst == 0:
            graf_report_1()
        elif lst == 1:
            graf_report_2()
        elif lst == 2:
            graf_report_3()
        elif lst == 3:
            graf_report_4()


# Создание листбокса 'Графическая информация'
Lb3 = Listbox(selectbackground='pink3', height=4, width=45)
Lb3.insert(0, 'График 1. Гистограмма')
Lb3.insert(1, 'График 2. Столбчатая диаграмма')
Lb3.insert(2, 'График 3. Диаграмма Бокса-Вискера')
Lb3.insert(3, 'График 4. Диаграмма рассеивания')


def lb3():
    """
    Данная функция вызывает listbox по кнопке 'Графическая информация'
    """
    Lb3.grid(column=2, row=1)
    Lb3.bind('<Double-Button-1>', go_box_3)
    Lb3.grid()


# Создание кнопки 'Список'
b1 = tk.Button(root, text='Список', bg='grey', height=5,
               width=20, command=lb1, font=("Arial Bold", 9))


def on_enter_3(_):
    """
    Данная функция изменяет цвет кпопки 'Список' при наведении курсора 
    """
    b1['background'] = 'pink3'


def on_leave_3(_):
    """
    Данная функция изменяет цвет кпопки 'Список' при выводе курсора 
    из поля кнопки
    """
    b1['background'] = 'grey'


b1.bind("<Enter>", on_enter_3)
b1.bind("<Leave>", on_leave_3)

# Создание кнопки 'Текстовая информация'
b2 = tk.Button(root, text='Текстовая информация', bg='grey', height=5,
               width=40, command=lb2, font=("Arial Bold", 9))


def on_enter_1(_):
    """
    Данная функция изменяет цвет кпопки 'Текстовая информация' при наведении курсора 
    """
    b2['background'] = 'pink3'


def on_leave_1(_):
    """
    Данная функция изменяет цвет кпопки 'Текстовая информация' при выводе курсора 
    из поля кнопки
    """
    b2['background'] = 'grey'


b2.bind("<Enter>", on_enter_1)
b2.bind("<Leave>", on_leave_1)

# Создание кнопки 'Графическая информация'
b3 = tk.Button(root, text='Графическая информация', bg='grey',
               height=5, width=40, command=lb3, font=("Arial Bold", 9))


def on_enter_2(_):
    """
    Данная функция изменяет цвет кпопки 'Графическая информация' при наведении курсора 
    """
    b3['background'] = 'pink3'


def on_leave_2(_):
    """
    Данная функция изменяет цвет кпопки 'Графическая информация' при выводе курсора 
    из поля кнопки
    """
    b3['background'] = 'grey'


b3.bind("<Enter>", on_enter_2)
b3.bind("<Leave>", on_leave_2)

# Вызов и расположение кнопок
b1.grid(column=0, row=0)
b2.grid(column=1, row=0)
b3.grid(column=2, row=0)

root.mainloop()
