
def add():

    import sqlite3

    conn = sqlite3.connect('1bd.db')
    cursor = conn.cursor()

    cursor.execute('''create table if not exists test1 (
    id integer PRIMARY KEY AUTOINCREMENT , 
    vopros varchar(20),
    spisok_otvetov varchar(100),
    otvet varchar(20))
    
    
    ''')

    conn.commit()

    cursor.execute(
        '''insert into test1 (vopros,spisok_otvetov,otvet) values ('Административный центр Владимирской области?','Брянск; Липецк; Орёл; Владимир','d')''')
    cursor.execute(
        '''insert into test1 (vopros,spisok_otvetov,otvet) values ('Административный центр Смоленской области?','Смоленск; Москва; Тула;Тверь','a')''')
    cursor.execute(
        '''insert into test1 (vopros,spisok_otvetov,otvet) values ('Административный центр Ярославской области области?','Иваново; Белгород; Красногорск; Ярославль','d')''')
    cursor.execute(
        '''insert into test1 (vopros,spisok_otvetov,otvet) values ('Административный центр Республики Бурятия?','Улан-Удэ; Элиста; Ростов; Пермь','a')''')


    # cursor.execute('''insert into test1 (vopros,spisok_otvetov,otvet) values ('Административный центр Владимирской области?','ответы через; ','ответ')''')
    # cursor.execute('''insert into test1 (vopros,spisok_otvetov,otvet) values ('Административный центр Смоленской области?','max1;vit1;ilya;petya','max1')''')
    conn.commit()



    cursor.execute('''select * from test1''')
    m = cursor.fetchall()
    # for i in m:
    #     print(i)

    cursor.execute('''drop table test1''')
    conn.commit()
    conn.close()
    return m