import mysql.connector as sql
from common.config import AppConfig

def create_connection():
    connection = sql.connect(
        host="localhost",
        user="root",
        password=AppConfig.PASSWORD,
        database="firma"
    )

    return connection

def create_weather_table():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        CREATE TABLE IF NOT EXISTS weather(
            id CHAR(36) NOT NULL PRIMARY KEY DEFAULT(UUID()),
            place VARCHAR(255),
            temp FLOAT,
            feels_like FLOAT, 
            wind FLOAT,
            timestamp TIMESTAMP,
            sunrise TIME 
       );
    """

    cursor.execute(query)
    connection.commit()
    connection.close()

def insert_weather(data):
    print(data)
    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO weather(place,temp,feels_like,wind,timestamp,sunrise) 
            VALUES (%s,%s,%s,%s,%s,%s);
        """
        values = (
            data["place"],
            data["temp"],
            data["feels_like"],
            data["wind"],
            data["timestamp"],
            data["sunrise"]
        )

        cursor.execute(query, values)

        connection.commit()
        connection.close()
        print("Zapisano dane w MySQL")

    except Exception as e:
        print(e)


