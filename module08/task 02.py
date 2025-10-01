import mysql.connector

def country_name(country_code):
    sql = f"SELECT country.name FROM country WHERE iso_country ='{country_code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for i in result :
            print(f"{i[0]} has ")

    return

def small_airports(country_code):
    sql = f"SELECT airport.type,count(*) FROM airport WHERE airport.iso_country = '{country_code}' AND airport.type = 'small_airport' GROUP BY airport.type"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for i in result:
            print(i[0] , i[1])
    return

def large_airports(country_code):
    sql = f"SELECT airport.type,count(*) FROM airport WHERE airport.iso_country = '{country_code}' AND airport.type = 'large_airport' GROUP BY airport.type"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for i in result:
            print(i[0] , i[1])
    return

def medium_airports(country_code):
    sql = f"SELECT airport.type,count(*) FROM airport WHERE airport.iso_country = '{country_code}' AND airport.type = 'medium_airport' GROUP BY airport.type"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for i in result:
            print(i[0] , i[1])
    return

def heli_airports(country_code):
    sql = f"SELECT airport.type,count(*) FROM airport WHERE airport.iso_country = '{country_code}' AND airport.type = 'heliport' GROUP BY airport.type"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for i in result:
            print(i[0] , i[1])
    return

connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='new_flight',
    user='root',
    password='maria1321',
    autocommit=True

)

country_code = str(input("enter country code : "))
country_name(country_code)
small_airports(country_code),large_airports(country_code),medium_airports(country_code),
heli_airports(country_code)





