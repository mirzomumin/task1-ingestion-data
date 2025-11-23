import os
import pymysql

from dotenv import load_dotenv


load_dotenv()


environment = os.environ

try:
    # Connect to the database
    connection = pymysql.connect(
        host=environment.get('DB_HOST'),
        user=environment.get('DB_USER'),
        password=environment.get('DB_PASS'),
        database=environment.get('DB_NAME'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
except Exception as e:
    print("Error while connecting to database:", e)
    exit(1)



if __name__ == "__main__":
    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = """
            CREATE TABLE books (
                id VARCHAR(20) PRIMARY KEY,
                title VARCHAR(255),
                author VARCHAR(255),
                genre VARCHAR(100),
                publisher VARCHAR(255),
                year INT,
                price VARCHAR(20)
            );
            """
            try:
                cursor.execute(sql)
            except Exception as e:
                print("Error while creating table:", e)

        # Commit the changes
        connection.commit()
