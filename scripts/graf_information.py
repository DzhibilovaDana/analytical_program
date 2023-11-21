"""
Файл: graf_information.py
Авторы: Игошина Дарья Дмиртриевна, Джибилова Дана Аслановна

Этот модуль реализует cоздание графических отчетов.
"""
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from get_from_ini import denorm, graf_1_png, graf_2_png, graf_3_png, graf_4_png


def graf_report_1():
    """
    Создание гистограммы по атрибуту 'Стоимость блюда'.
    """

    def export():
        """
        Экспорт гистограммы в формат .png.
        """
        fig.savefig(graf_1_png)

    # создание нового окна с помощью tkinter
    window = tk.Tk()
    window.title('Гистограмма по атрибуту: стоимость блюда')
    # создание меню для экспорта
    menu = tk.Menu(window)
    window.config(menu=menu)
    menu.add_cascade(label="Экспорт", command=export)
    # создание фигуры для графика
    fig = Figure(figsize=(5, 4), dpi=100)
    # добавление подграфика в фигуру
    plot = fig.add_subplot(1, 1, 1)
    # отрисовка столбчатого графика
    plot.hist(denorm['Стоимость блюда'], color='pink', edgecolor='black',
              bins=int(180 / 5))
    plot.set_title("Гистограмма", fontsize=25, color="black")
    plot.set_ylabel('Количество блюд')
    plot.set_xlabel('Стоимость')
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()


def graf_report_2():
    """
    Создание столбчатой диаграммы по атрибутам 'Стоимость блюда', 'День недели'.
    """

    def export():
        """
        Экспорт гистограммы в формат .png.
        """
        fig.savefig(graf_2_png)

    # создание нового окна с помощью tkinter
    window = tk.Tk()
    window.title('Столбчатая диаграмма по атрибутам: стоимость блюда, день недели')
    menu = tk.Menu(window)
    window.config(menu=menu)
    menu.add_cascade(label="Экспорт", command=export)
    # создание фигуры для графика
    fig = Figure(figsize=(5, 4), dpi=100)
    # добавление подграфика в фигуру
    plot = fig.add_subplot(1, 1, 1)
    # отрисовка столбчатого графика
    plot.bar(denorm['День недели'], denorm['Стоимость блюда'], color='pink')
    plot.set_xlabel("День недели")
    plot.set_ylabel("Стоимость блюда")
    plot.set_title("Столбчатая диаграмма")
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()


def graf_report_3():
    """
    Создание диаграммы Бокса-Вискера по атрибуту: 'Стоимость блюда'.
    """

    def export():
        """
        Экспорт гистограммы в формат .png.
        """
        fig.savefig(graf_3_png)

    # создание нового окна с помощью tkinter
    window = tk.Tk()
    window.title('Диаграмма Бокса-Вискера по атрибуту: cтоимость блюда')
    menu = tk.Menu(window)
    window.config(menu=menu)
    menu.add_cascade(label="Экспорт", command=export)
    # создание фигуры для графика
    fig = Figure(figsize=(5, 4), dpi=100)
    # добавление подграфика в фигуру
    plot = fig.add_subplot(1, 1, 1)
    # отрисовка столбчатого графика
    data = denorm['Стоимость блюда']
    plot.set_title("Диаграмма Бокса-Вискера: cтоимость блюда")
    plot.boxplot(data)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()


def graf_report_4():
    """
    Создание диаграммы рассеивания по атрибутам 'Стоимость блюда', 'Количество посещений'.
    """

    def export():
        """
        Экспорт гистограммы в формат .png.
        """
        fig.savefig(graf_4_png)  # создание нового окна с помощью tkinter

    window = tk.Tk()
    window.title('Диаграмма рассеивания по атрибутам: кол-во посещений, стоимость блюда')
    menu = tk.Menu(window)
    window.config(menu=menu)
    menu.add_cascade(label="Экспорт", command=export)
    # создание фигуры для графика
    fig = Figure(figsize=(5, 4), dpi=100)
    # добавление подграфика в фигуру
    plot = fig.add_subplot(1, 1, 1)
    # отрисовка столбчатого графика
    plot.scatter(denorm['Кол-во посещений'], denorm['Стоимость блюда'], color='pink')
    plot.set_xlabel("Количество посещений")
    plot.set_ylabel("Стоимость блюда")
    plot.set_title("Диаграмма рассеивания")
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
