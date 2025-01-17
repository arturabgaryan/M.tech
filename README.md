# M.tech тестовое задание

## SQL task:

https://pastebin.com/C8Vqp8FW


## DS task, описание решения:

**Загрузка и предобработка данных:**

 - Загружаем CSV-файл с данными сотрудников.
 
 - Разделяем сотрудников на группы по полу (мужчины и женщины) и возрасту (старше 35 лет и младше 35 лет). Для этого создается новый столбец с возрастными категориями.
 
**Визуализация данных:**

 - Используем графики для наглядного представления данных:
 
   - Violin plot показывает распределение пропусков по болезни среди мужчин и женщин, а также среди возрастных групп (старше и младше 35 лет).
   
**Проверка гипотез с помощью t-теста:**

 - Для обеих гипотез используем t-тест для независимых выборок, чтобы проверить, есть ли значимые различия между средними значениями пропусков рабочих дней по группам.
 
 - Рассчитываем t-статистику и p-значение для каждой гипотезы:
 
   - Гипотеза 1: Сравниваем пропуски по болезни среди мужчин и женщин.
   
   - Гипотеза 2: Сравниваем пропуски по болезни среди работников старше и младше 35 лет.
   
 - P-значение используется для принятия решения:
 
   - Если p-значение меньше 0.05, отвергаем нулевую гипотезу, что означает, что есть значимые различия между группами.
   
   - Если p-значение больше 0.05, нулевая гипотеза не отвергается, и мы считаем, что различий между группами нет.
   
**Выводы:**

 - По результатам проверки гипотез приложение выводит заключения:
 
   - Если p-значение меньше 0.05, то делается вывод, что мужчины (или сотрудники старше 35 лет) действительно пропускают больше рабочих дней по болезни, чем женщины (или сотрудники младше 35 лет).
   
   - Если p-значение больше 0.05, выводится заключение, что нет значимых различий между группами.
  

 ## Запуск докера
```
 docker build -t mtech https://github.com/arturabgaryan/M.tech.git
 docker run -p 8501:8501 mtech
```
