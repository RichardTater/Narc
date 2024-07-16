import sqlite3
import pandas as pd

def execute_sql_insert(conn: sqlite3.Connection, sql: str, obj: dict):
    """
    Executes a SQL insert statement.

    Args:
        conn (sqlite3.Connection): connection to the database
        sql (str): insert SQL statement
        obj (dict): the parameters to the SQL statement

    Returns:
        The id of the inserted row. 
    """
    cur = conn.cursor()
    cur.execute(sql, obj)
    conn.commit()
    return cur.lastrowid

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
    return execute_sql_insert(conn, sql, narc)

def add_offender(conn: sqlite3.Connection, offender: dict):
    """
    Adds a offender record to the offender table in the database.

    Args:
        conn (sqlite3.Connection): connection to the database
        offender (dict): dictionary of offender data

    Returns:
        The id of the inserted offender. 
    """
    sql = '''   
            INSERT INTO offender(plate_number, plate_state, make, model, color)
            VALUES (:plate_number, :plate_state, :make, :model, :color)
          '''
    return execute_sql_insert(conn, sql, offender)

def add_offence(conn: sqlite3.Connection, offence: dict):
    """
    Adds a offence record to the offence table in the database.

    Args:
        conn (sqlite3.Connection): connection to the database
        offence (dict): dictionary of offence data

    Returns:
        The id of the inserted offence. 
    """
    offence['date'] = offence['date'].strftime('%Y-%m-%d')
    offence['time'] = offence['time'].strftime('%H:%M')
    sql = '''   
            INSERT INTO offence(narc_id, offender_id, date, time, state, city, note)
            VALUES (:narc_id, :offender_id, :date, :time, :state, :city, :note)
          '''
    return execute_sql_insert(conn, sql, offence)

try:
    with sqlite3.connect('narc.db') as conn:
        all_sheets = pd.read_excel('seed_data.xlsx', sheet_name=None)
        for sheet_name, sheet in all_sheets.items():
            for row_number, row_data in sheet.iterrows():
                id = 0
                if sheet_name == "narc":
                    id = add_narc(conn, row_data.to_dict())
                elif sheet_name == "offender":
                    id = add_offender(conn, row_data.to_dict())
                elif sheet_name == "offence": 
                    id = add_offence(conn, row_data.to_dict())
                print(f'Created {sheet_name} with the id {id}')
except sqlite3.Error as e:
    print(e)
