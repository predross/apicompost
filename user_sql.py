import psycopg2
from psycopg2.extras import DictCursor

def get_connection():
    return psycopg2.connect(
        host = '127.0.0.1',
        port = '5432',
        user = 'postgres',
        password = '123456',
        database = 'celepar'
    )

def list_user():
    with get_connection() as conn:
        cur = conn.cursor(cursor_factory = DictCursor)
        cur.execute("SELECT * FROM swf_user")
        rows = cur.fetchall()
        cur.close()
        data = [row_to_dict(x) for x in rows]
        return data

def save_user(user):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""INSERT INTO swf_user 
                        (id, name, email, active) VALUES (%s, %s, %s, %s)""", 
                    (user[0], user[1], user[2], user[3],))
        conn.commit()
        cur.close()

def find_by_name(name):
    with get_connection() as conn:
        cur = conn.cursor(cursor_factory = DictCursor)
        name = '%'+name+'%'
        cur.execute("SELECT * FROM swf_user WHERE name ilike %s", (name,))
        rows = cur.fetchall()
        cur.close()
        data = [row_to_dict(x) for x in rows]
        return data

def update(user):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""UPDATE swf_user SET name = %s, email = %s, active = %s WHERE id = %s""", (user[1], user[2], user[3], user[0]))
        conn.commit()
        cur.close()

def delete(uuid):
    with get_connection() as conn:
        cur = conn.cursor()
        print(uuid)
        cur.execute("""DELETE FROM swf_user WHERE id = %s""", (uuid,))
        conn.commit()
        cur.close()

def row_to_dict(row):
    return dict({
        'id' : row['id'],
        'name' : row['name'],
        'email' : row['email'],
        'active' : row['active']
    })
    
