import mysql.connector
from geopy.distance import geodesic

def get_codes1(icao1):
    sql = f" SELECT latitude_deg,longitude_deg FROM airport WHERE ident = 'icao1' "
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_codes2(icao2):
    sql = f" SELECT latitude_deg,longitude_deg FROM airport WHERE ident = 'icao2' "
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result2 = cursor.fetchall()
    return result2



connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='new_flight',
    user='root',
    password='maria1321',
    autocommit=True
)

icao1 = str(input("enter ICAO 1: "))
icao2 = str(input("enter ICAO 2: "))


def distance():
    pr1 = get_codes1(icao1)
    pr2 = get_codes2(icao2)
    distance_km = float(geodesic(pr1, pr2).kilometers)
    print(f"\nDistance between {icao1} and {icao2}: {distance_km:.2f} km")

distance()
