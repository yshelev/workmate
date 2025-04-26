# logs Parser
Парсинг передаваемых в программу параметров, парсинг данных файлов, написание тестов

## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
- [Команда проекта](#команда-проекта)


## Технологии
Парсинг данных производился с помощью встроенных в python инструментов, создание тестов с помощью библиотеки pytest

## Использование
1. Склонируйте репозиторий:
   ```sh
   git clone https://github.com/yshelev/workmate.git
   cd workmate
   ```
2. Создайте и активируйте виртуальное окружение: 
   ```sh
   python3 -m venv .venv
   .venv/Scripts/activate
   ```
3. Установите необходимые зависимости:  	
   ```sh
   pip install -r requirements.txt
   ```
4. В директорию logs поместите логи (допустимые разрешения: *.log)
5. Запустите программу:
   ```sh
   python main.py [paths to files] --report [report name] 
   ```
Пример работы программы:
![image](https://github.com/user-attachments/assets/2a5917ef-321f-4747-82be-7bb69c74d38e)

Для запуска тестов: 
1. Перейдите в директорию tests:
   ```sh
     cd tests
   ```
2. Запустите тесты:
   ```sh
     pytest .
   ```
3. Для получения процента покрытия кода тестами:
   ```sh
     pytest --cov
   ```
Покрытие тестами: 
![image](https://github.com/user-attachments/assets/4b501d37-c172-49ed-ae65-d8ea28831472)


## Команда проекта

- [Шелевой Ярослав](https://github.com/yshelev) — Backend developer
