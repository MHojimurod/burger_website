from django.db import connection
from contextlib import closing



def get_header_info():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM burger_head """)
        header = dict_fetchall(cursor)
        return header
def get_ourrecipes():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM burger_ourrecipes """)
        header = dict_fetchall(cursor)
        return header

def get_ourfood():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM burger_aboutourfood """)
        header = dict_fetchall(cursor)
        return header


def get_ourblog():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM burger_ourblog """)
        header = dict_fetchall(cursor)
        return header

def get_clients():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM burger_clients """)
        header = dict_fetchall(cursor)
        return header

def get_questions():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM burger_questions """)
        header = dict_fetchall(cursor)
        return header

def get_register():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM burger_register """)
        header = dict_fetchall(cursor)
        return header

def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
