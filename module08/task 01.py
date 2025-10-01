import mysql.connector

def airport_name(icao):
    sql = (f"SELECT airport.name,country.name FROM airport,country WHERE airport.iso_country = country.iso_country AND airport.ident = '{icao}'")

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0 :
        for i in result:
            print(f"airport name is {i[0]} and country name is {i[1]}")
    return
connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='new_flight',
    user='root',
    password='maria1321',
    autocommit=True

)
icao = str(input("enter ICAO code : "))
airport_name(icao)

