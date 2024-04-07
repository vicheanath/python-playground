from app.use_cases.user_management import UserManagement
from app.interfaces.database.postgres_adapter import PostgresAdapter
from app.interfaces.database.mysql_adapter import MySQLAdapter
from app.interfaces.database.sqlite_adapter import SQLiteAdapter
from app.frameworks_drivers.database.postgres_driver import PostgresDriver
from app.frameworks_drivers.database.mysql_driver import MySQLDriver
from app.frameworks_drivers.database.sqlite_driver import SQLiteDriver

import logging
import sys

def setup_logging():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    # Add file handler if needed
    file_handler = logging.FileHandler("app.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_handler)

def main():
    setup_logging()

    # Configurations
    postgres_config = {
        "host": "localhost",
        "user": "postgres",
        "password": "password",
        "database": "app"
    }
    mysql_config = {
        "host": "localhost",
        "user": "root",
        "password": "password",
        "database": "app"
        
    }
    sqlite_config = {
        "database": "db.sqlite"
    }

    # Initialize drivers
    postgres_driver = PostgresDriver(postgres_config)
    mysql_driver = MySQLDriver(mysql_config)
    sqlite_driver = SQLiteDriver(sqlite_config)

    # Initialize adapters
    postgres_adapter = PostgresAdapter()
    mysql_adapter = MySQLAdapter()
    sqlite_adapter = SQLiteAdapter()

    # Inject database dependencies into use cases
    postgres_user_management = UserManagement(postgres_adapter)
    mysql_user_management = UserManagement(mysql_adapter)
    sqlite_user_management = UserManagement(sqlite_adapter)

   
if __name__ == "__main__":
    main()