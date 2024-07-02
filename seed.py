import sqlite3

def add_narc(conn: sqlite3.Connection, narc: dict):
    """
    Adds a narc record to the narc table in the database.

    Args:
        conn (sqlite3.Connection): connection to the database
        narc (dict): dictionary of narc data

    Returns:
        The id of the inserted narc. 
    """
    sql = '''   
            INSERT INTO narc(email, first_name, last_name, password)
            VALUES (:email, :first_name, :last_name, :password)
          '''
    cur = conn.cursor()
    cur.execute(sql, narc)
    conn.commit()
    return cur.lastrowid


try:
    with sqlite3.connect('narc.db') as conn:
        # add a new narc
        narc = {
            'email': 'Jim@dundermifflin.com',
            'first_name': 'Jim',
            'last_name': 'Halpert',
            'password': 'JimHalpertpassword'
        }
        narc_id = add_narc(conn, narc)
        print(f'Created a narc with the id {narc_id}')


except sqlite3.Error as e:
    print(e)
