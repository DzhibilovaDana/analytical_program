"""
Файл: common_functions.py
Авторы: Игошина Дарья Дмиртриевна, Джибилова Дана Аслановна

Этот модуль содержит функции, которые могут быть использованы в других проектах
и не адаптированы под данное приложение.
"""
from tkinter import ttk


def cnv_configure(cnv):
    """
    Функция создает фигуру для вставки таблицы.
    """
    cnv.configure(scrollregion=cnv.bbox("all"))


def refresh(window, fl1):
    """
    Данная функция осуществляет вывод справочника/таблицы на экран,
    обновление данных таблиц.
    """
    l1 = list(fl1)
    r_set = fl1.to_numpy().tolist()  # create list of list using rows
    trv = ttk.Treeview(window, selectmode='browse', height=6,
                       show='headings', columns=l1)
    trv.place(x=0, y=0, width=1100, height=800)
    for i in l1:
        trv.column(i, width=150)
        trv.heading(i, text=str(i))
    for dt in r_set:
        v = [r for r in dt]
        trv.insert("", 'end', iid=v[0], values=v)
