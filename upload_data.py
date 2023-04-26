import datetime
import os
from tkinter import Button, Entry, Frame, Label, StringVar, Tk, messagebox

import pandas as pd
import psycopg2
from dotenv import load_dotenv
from psycopg2 import Error

load_dotenv()


def upload_data():
    date_start = date_start_tf.get()
    date_end = date_end_tf.get()

    date_today = datetime.datetime.today().strftime('%Y%m%d')

    query = os.getenv('QUERY')

    try:
        connection = psycopg2.connect(user=os.getenv('USER'),
                                      password=os.getenv('PASSWORD'),
                                      host=os.getenv('HOST'),
                                      port=os.getenv('PORT'),
                                      database=os.getenv('DATABASE'))
        cursor = connection.cursor()
        cursor.execute(query, (date_start, date_end))
        result = cursor.fetchall()
    except (Exception, Error) as error:
        messagebox.showinfo('Упс!', f'Ошибка при работе с БД: {error}.')
    else:
        messagebox.showinfo(
            'Хорошие новости',
            'Выгрузка успешно завершена!\nСоединение с БД закрыто.'
        )
    finally:
        if connection:
            cursor.close()
            connection.close()

    data_to_xml = pd.DataFrame(
        {
            'ls': [x[0] for x in result],
            'date': [x[1] for x in result],
            'pok1': [x[2] for x in result],
            'pok2': [x[3] for x in result],
            'f_sendmail': 'false',
            'email': None,
        }
    ).to_xml(index=False, root_name='VFPData', row_name='exp_ch99')

    with open(f'telegram_{date_today}.xml', 'w') as file:
        file.write(data_to_xml)


window = Tk()
window.title('Чат-бот: выгрузка показаний')
window.geometry('300x150')

frame = Frame(
   window,
   padx=10,
   pady=10
)
frame.pack(expand=True)

date_start_lb = Label(
   frame,
   text='Дата начала:'
)
date_start_lb.grid(row=3, column=1)

date_end_lb = Label(
   frame,
   text='Дата конца:',
)
date_end_lb.grid(row=4, column=1)

year_month = datetime.datetime.today().strftime('%Y-%m')

date_start = StringVar(window, value=f'{year_month}-20')
date_start_tf = Entry(frame, textvariable=date_start)
date_start_tf.grid(row=3, column=2, pady=5)

date_end = StringVar(window, value=f'{year_month}-25')
date_end_tf = Entry(frame, textvariable=date_end)
date_end_tf.grid(row=4, column=2, pady=5)

upload_btn = Button(
   frame,
   text='Выгрузить показания',
   command=upload_data
)
upload_btn.grid(row=5, column=2)

window.mainloop()
