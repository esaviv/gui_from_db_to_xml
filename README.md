# gui_from_db_to_xml
Программа с графическим интерфейсом для выгрузки данных из БД PostgreSQL в формате .xml.

**Стек технологий:** python3.9, python-dotenv, psycopg2, pandas, numpy, lxml

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/esaviv/gui_from_db_to_xml.git
```
```
cd gui_from_db_to_xml
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv | python -m venv venv
```
```
source env/bin/activate | source venv/Scripts/activate
```
```
python3 -m pip install --upgrade pip | python -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Создать .env и заполнить по шаблону .env.template
```
touch .env
```
Переписать ```data_to_xml```, исходя из своих нужд.

Запустить программу:
```
python3 upload_data.py | python uplaod_data.py
```
При необходимости упаковать программу в EXE формат рекомендую использовать [инструкцию](https://dzen.ru/a/YqCdN_1gJkixXCf4).

## Автор
esaviv
