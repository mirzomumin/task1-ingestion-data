import json
import re
from db import connection

def main():
    filename = './task1_d.json'
    data = read_data(filename)
    formatted_data = format_data(data)
    books = convert_data(formatted_data)
    try:
        write_data_into_db(books)
    except Exception as e:
        print("Error while writing data into database:", e)


def read_data(filename: str) -> str:
    # read data from file
    with open(filename, 'r') as f:
        data = f.read()
    return data


def format_data(data: str) -> str:
    # Convert :key=>value into "key": value and deserialize
    data = re.sub(r':([a-zA-Z]*)\s*=>', r'"\1":', data)
    return json.loads(data)


def convert_data(data: list[dict]) -> list[tuple]:
    # Convert dict items of list into tuple
    return [
        (
            str(item["id"]),
            item["title"],
            item["author"],
            item["genre"],
            item["publisher"],
            item["year"],
            item["price"],
        )
        for item in data
    ]


def write_data_into_db(books: list[tuple]) -> None:
    batch_size = 1000
    sql = """INSERT INTO books (id, title, author, genre, publisher, year, price)
         VALUES (%s, %s, %s, %s, %s, %s, %s)"""

    with connection:
        with connection.cursor() as cursor:
            for i in range(0, len(books), batch_size):
                batch = books[i:i+batch_size]
                cursor.executemany(sql, batch)
            connection.commit()


if __name__ == "__main__":
    main()
