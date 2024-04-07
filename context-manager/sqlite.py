import sqlite3
import logging
from contextlib import contextmanager

# Create a context manager for SQLite
class SQlite:
    def __init__(self, filename: str):
        self.filename = filename
        self.connection = sqlite3.connect(self.filename)
        
    def __enter__(self):
        """ Return a cursor to the database """
        logging.info('Called __enter__')
        return self.connection.cursor()
    
    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        """ Commit and close the connection """
        logging.info('Called __exit__')
        self.connection.commit()
        self.connection.close()
        if exc_type:
            logging.error(f'Error: {exc_type}, {exc_value}')
            return False
        return True

#  Create a context manager for SQLite using contextmanager
@contextmanager
def sqlite(filename: str):
    """ Context manager for SQLite by using contextmanager decorator """
    connection = sqlite3.connect(filename)
    try:
        yield connection.cursor()
    except sqlite3.DatabaseError as e:
        logging.error(f'Error: {e}')
        raise
    finally:
        connection.commit()
        connection.close()
    
def main():
    logging.basicConfig(level=logging.INFO)
    with sqlite('test.db') as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)')
        cursor.execute('INSERT INTO test (name) VALUES (?)', ('test',))
        cursor.execute('SELECT * FROM test')
        print(cursor.fetchall())
    logging.info('Done')
    
    
if __name__ == '__main__':
    main()