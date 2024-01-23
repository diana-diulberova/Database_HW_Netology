import psycopg2


# Функция, создающая структуру БД (таблицы).

def create_tables(cur):

    cur.execute("""
        CREATE TABLE IF NOT EXIST clients(
        client_id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        surname VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXIST phones(
        phone_id SERIAL PRIMARY KEY,
        client_id SERIAL REFERENCES clients(Client_id),
        phone VARCHAR(100) NOT NULL UNIQUE
        );
    """)


# Функция, позволяющая добавить нового клиента.

def add_client(cur, name, surname, email):
    cur.execute("""
    INSERT INTO clients(name, surname, email) VALUES(%s, %s, %s);
    """, (name, surname, email))



# Функция, позволяющая добавить телефон для существующего клиента.

def add_phone(cur, client_id, phone):
    cur.execute("""
    INSERT INTO phones(client_id, phone) VALUES(%s, %s);
    """, (client_id, phone))



# Функция, позволяющая изменить данные о клиенте.

def change_client(cur, client_id, name=None, surname=None, email=None, phone=None):
    if not name:
        name = '%'
    if not surname:
        surname = '%'
    if not email:
        email = '%'
    if phone:
        cur.execute("""
        SELECT client_id FROM phones
        WHERE client_id = %s;
        """, (client_id,))
        if cur.fetchall():
            cur.execute("""
            UPDATE phones
            SET phone=%s
            WHERE client_id=%s;
            """, (phone, client_id))
        else:
            add_phone(cur, client_id, phone)
    cur.execute("""
    UPDATE clients
    SET name=%s, surname=%s, email=%s
    WHERE client_id=%s;
    """, (name, surname, email, client_id))

    cur.execute("""
    SELECT * FROM clients
    LEFT JOIN phones ON clients.client_id = phones.client_id;
    """)

    return cur.fetchall()



# Функция, позволяющая удалить телефон для существующего клиента.

def del_phone(cur, client_id, phone):
    if phone:
        cur.execute("""
        DELETE FROM phones
        WHERE client_id = %s AND phone = %s
        """, (client_id, phone))
    else:
        cur.execute("""
        DELETE FROM phones
        WHERE client_id = %s
        """, (client_id,))

    cur.execute("""
    SELECT * FROM phones
    """)
    return cur.fetchall()



# Функция, позволяющая удалить существующего клиента.

def del_client(cur, client_id):
    del_phone(cur, client_id, None)
    cur.execute("""
    DELETE FROM clients
    WHERE client_id = %s
    """, (client_id,))
    cur.execute("""
    SELECT * FROM clients;
    """)
    return cur.fetchall()



# Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.

def find_client(cur, name=None, surname=None, email=None, phone=None):
    if not name:
        name = '%'
    if not surname:
        surname = '%'
    if not email:
        email = '%'
    if not phone:
        cur.execute("""
        SELECT client_id, name, surname, email FROM clients
        LEFT JOIN phones ON clients.client_id = phones.client_id
        WHERE name LIKE %s AND surname LIKE %s AND
        email LIKE %s;
        """, (name, surname, email))
    else:
        cur.execute("""
        SELECT client_id, name, surname, email FROM clients
        LEFT JOIN phones ON clients.client_id = phones.client_id
        WHERE phone = %s;
        """, (phone,))
    return cur.fetchall()



def main():
    conn = psycopg2.connect(database='netology_db', user='postgres', password='21km14Km')

    with conn.cursor() as cur:
        create_tables(cur)
        add_client(cur, "Ivan", "Ivanov", "sffzvdf@g.com")
        add_client(cur, "Petr", "Petrov", "zdfbdbf@g.com")
        add_client(cur, "Ann", "Kozlova", "jzfbzdfbzfb@g.com")
        add_client(cur, "Elena", "Sidorova", "zdbffgxh@g.com")
        add_client(cur, "Semen", "Semenov", "zfdfdgz@g.com")
        add_phone(cur, 1, "121212")
        add_phone(cur, 2, "434343")
        add_phone(cur, 3, "565656")
        add_phone(cur, 4, "898989")
        add_phone(cur, 4, "787878")
        add_phone(cur, 5, "232323")
        change_client()
        del_phone()
        del_client()
        find_client()

        conn.commit()

    conn.close()


if __name__ == '__main__':
      main()
