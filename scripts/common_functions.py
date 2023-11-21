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


def refresh(window, file):
    """
    Данная функция осуществляет вывод справочника/таблицы на экран,
    обновление данных таблиц.
    """
    l_1 = list(file)
    r_set = file.to_numpy().tolist()
    tree_v = ttk.Treeview(window, selectmode='browse', height=6,
                          show='headings', columns=l_1)
    tree_v.place(x=0, y=0, width=1100, height=800)
    for i in l_1:
        tree_v.column(i, width=150)
        tree_v.heading(i, text=str(i))
    for dif_t in r_set:
        value = list(dif_t)
        tree_v.insert("", 'end', iid=value[0], values=value)
