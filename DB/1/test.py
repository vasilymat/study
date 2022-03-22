#import sys
#sys.path.append('c:/users/lab/anaconda3/lib/site-packages')
#
#import psycopg2

#В папке находятся 3 таблицы. 
#Необходимо создать свой проект Google BigQuery, загрузить туда эти таблицы и 
#решить задачу: В таблице webinar.csv находится список посетителей вебинара,
#который прошел 1 апреля 2016 г. Нужно вывести на экран тех посетителей, кто
#впервые зарегистрировался в еЛаме (users.csv) после вебинара,и для каждого
#из них посчитать сумму его пополнений в системе (transactions.csv).
#Под посетителем вебинара мы понимаем одного человека, то есть один email.
#
#Ответ представить в виде: текст SQL запроса + скриншот с результатом выполнения запроса.


con = psycopg2.connect(
  database="test1", 
  user="postgres", 
  password="anels6bg", 
  host="127.0.0.1", 
  port="5432"
)

cur = con.cursor()

cur.execute("""
            DROP TABLE users;
            """)

cur.execute("""CREATE TABLE users(
               id SERIAL,
               user_id  INTEGER,
               email    VARCHAR(255),
               date_reg TIMESTAMP,
               PRIMARY KEY (id)
               );
            """)


csv_path = 'C:/MatkivskiyV/study/DB/1/users.csv'

cur.execute("""
            COPY users (user_id,email,date_reg)
            FROM 'C:/MatkivskiyV/study/DB/1/users.csv'
            DELIMITER ','
            CSV HEADER;
             """)

cur.execute


cur.execute("""
            SELECT * FROM users;
               """)
print(cur.fetchone())

con.commit()
cur.close()
con.close()