import sqlite3


class TestDB:
    def test_db_create(self):
        try:
            with sqlite3.connect('db/database.db') as db:
                cursor = db.cursor()
                query = """CREATE TABLE IF NOT EXISTS expenses (id INTEGER, name TEXT)"""
                cursor.execute(query)

                data = [
                    (1, 'Коммунальные платежи'),
                    (2, 'Продукты'),
                    (3, 'Развлечения')
                ]
                cursor.executemany("""INSERT INTO expenses (id, name) VALUES (?, ?)""", data)
                db.commit()
                db.close()

        except:
            pass

    def test_table_exists(self):

        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            table_name = 'expenses'
            cursor.execute(""" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='expenses' """)
            if cursor.fetchone()[0] == 1:
                print('Table exists.')
            else:
                print('Table does not exist.')

            db.close()
