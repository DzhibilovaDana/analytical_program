"""
Файл: get_from_ini.py
Авторы: Игошина Дарья Дмиртриевна, Джибилова Дана Аслановна

Этот модуль получает данные из конфигурационного файла settings.ini,
считывает базы данных из файлов формата .csv c помощью библиотеки pandas.
"""
import configparser
import pandas as pd

# создание объекта парсера
config = configparser.ConfigParser()
config.read('settings.ini')

# чтение баз данных из файлов .csv
data_frame_1 = pd.read_csv(config["datas"]["data_1"], delimiter=",", encoding="utf-8",
                           dtype='O')
data_frame_1 = data_frame_1.astype({"Стоимость блюда": int})
data_frame_2 = pd.read_csv(config["datas"]["data_2"], delimiter=",", encoding="utf-8",
                           dtype='O')
data_frame_2 = data_frame_2.astype({"Кол-во посещений": int})

# деномарлизация базы даннных
denorm = pd.merge(data_frame_1, data_frame_2, on='День недели')

# получение настроек интерфейса
root_size = config["settings"]["size"]
light_col = config["settings"]["light_col"]
dark_col = config["settings"]["dark_col"]

# получение пути к изображениям для настройки интерфейся
sun = config["images"]["sun"]
moon = config["images"]["moon"]

# получение путей файлов для экспорта
export_simp_1_xlsx = config["export"]["export_simp_1_xlsx"]
export_simp_1_csv = config["export"]["export_simp_1_csv"]
export_simp_1_pkl = config["export"]["export_simp_1_pkl"]

export_simp_2_xlsx = config["export"]["export_simp_2_xlsx"]
export_simp_2_csv = config["export"]["export_simp_2_csv"]
export_simp_2_pkl = config["export"]["export_simp_2_pkl"]

export_stat_xlsx = config["export"]["export_stat_xlsx"]
export_stat_csv = config["export"]["export_stat_csv"]
export_stat_pkl = config["export"]["export_stat_pkl"]

export_sum_xlsx = config["export"]["export_sum_xlsx"]
export_sum_csv = config["export"]["export_sum_csv"]
export_sum_pkl = config["export"]["export_sum_pkl"]

graf_1_png = config["graf"]["graf_1_png"]
graf_2_png = config["graf"]["graf_2_png"]
graf_3_png = config["graf"]["graf_3_png"]
graf_4_png = config["graf"]["graf_4_png"]
